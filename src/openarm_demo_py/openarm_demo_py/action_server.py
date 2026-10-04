#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openarm_demo_py: action_server.py
Mục đích:
- Minh họa Action Server trong ROS 2 (cho các tác vụ tốn thời gian như di chuyển quỹ đạo).
- Hỗ trợ gửi Feedback định kỳ về tiến độ.
- Hỗ trợ hủy tác vụ khi cần (Goal Preemption/Cancellation).
- Trả về Result khi hoàn thành.
"""

import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from example_interfaces.action import Fibonacci


class ArmTrajectoryActionServerNode(Node):
    def __init__(self):
        super().__init__('arm_trajectory_action_server')

        # Khởi tạo Action Server với action type Fibonacci (mô phỏng chuỗi toạ độ/bước di chuyển)
        self._action_server = ActionServer(
            self,
            Fibonacci,
            '/execute_trajectory',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )

        self.get_logger().info('>>> [Action Server Init] Sẵn sàng nhận mục tiêu tại action: /execute_trajectory')

    def goal_callback(self, goal_request):
        """Kiểm tra và chấp nhận/từ chối mục tiêu."""
        self.get_logger().info(f'Nhận yêu cầu mục tiêu với order = {goal_request.order}')
        if goal_request.order < 0:
            self.get_logger().warn('Order không hợp lệ (< 0), từ chối goal!')
            return GoalResponse.REJECT
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        """Xử lý yêu cầu hủy mục tiêu từ client."""
        self.get_logger().warn('Nhận tín hiệu hủy (Cancel) từ Client!')
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):
        """Thực thi tác vụ dài hạn và gửi feedback."""
        self.get_logger().info('Bắt đầu thực thi quỹ đạo chuyển động...')

        feedback_msg = Fibonacci.Feedback()
        feedback_msg.sequence = [0, 1]

        order = goal_handle.request.order

        for i in range(1, order):
            # Kiểm tra nếu Client yêu cầu hủy tác vụ
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().warn('Tác vụ đã bị HỦY thành công!')
                result = Fibonacci.Result()
                result.sequence = feedback_msg.sequence
                return result

            # Mô phỏng tính toán và di chuyển từng bước
            feedback_msg.sequence.append(feedback_msg.sequence[i] + feedback_msg.sequence[i - 1])
            self.get_logger().info(f'[Feedback] Bước {i}/{order}: Chuỗi hiện tại = {feedback_msg.sequence}')
            goal_handle.publish_feedback(feedback_msg)

            # Tạm dừng 0.7 giây giả lập thời gian robot chuyển động
            time.sleep(0.7)

        # Đánh dấu tác vụ thành công
        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback_msg.sequence
        self.get_logger().info(f'Hoàn thành quỹ đạo! Kết quả cuối: {result.sequence}')
        return result


def main(args=None):
    rclpy.init(args=args)
    node = ArmTrajectoryActionServerNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
