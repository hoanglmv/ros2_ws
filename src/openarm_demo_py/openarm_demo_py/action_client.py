#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openarm_demo_py: action_client.py
Mục đích:
- Minh họa Action Client trong ROS 2.
- Gửi Goal đến Action Server.
- Nhận phản hồi thời gian thực qua feedback_callback.
- Nhận kết quả cuối cùng qua get_result_callback.
"""

import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from example_interfaces.action import Fibonacci


class ArmTrajectoryActionClientNode(Node):
    def __init__(self):
        super().__init__('arm_trajectory_action_client')
        self._action_client = ActionClient(self, Fibonacci, '/execute_trajectory')
        self.get_logger().info('>>> [Action Client Init] Đang tìm kiếm Action Server...')

    def send_goal(self, order=7):
        """Gửi goal và đăng ký các hàm callback tương ứng."""
        self._action_client.wait_for_server()

        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self.get_logger().info(f'Gửi mục tiêu quỹ đạo: order = {order}')

        # Gửi goal kèm feedback callback
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        """Được gọi khi Action Server phản hồi chấp nhận hoặc từ chối Goal."""
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Mục tiêu bị Server TỪ CHỐI!')
            return

        self.get_logger().info('Mục tiêu đã được Server CHẤP NHẬN! Đang thực thi...')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        """Được gọi mỗi khi Action Server gửi cập nhật tiến độ (Feedback)."""
        feedback = feedback_msg.feedback
        self.get_logger().info(f'[Nhận Feedback]: Chuỗi hiện tại -> {feedback.sequence}')

    def get_result_callback(self, future):
        """Được gọi khi Action Server hoàn thành toàn bộ mục tiêu và trả về kết quả."""
        result = future.result().result
        self.get_logger().info(f'>>> [Kết quả Cuối Cùng]: {result.sequence}')
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    action_client = ArmTrajectoryActionClientNode()

    # Nhận order từ đối số dòng lệnh nếu có, mặc định là 6
    order = 6
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        order = int(sys.argv[1])

    action_client.send_goal(order)
    try:
        rclpy.spin(action_client)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
