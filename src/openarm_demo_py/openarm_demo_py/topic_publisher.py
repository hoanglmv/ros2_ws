#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openarm_demo_py: topic_publisher.py
Mục đích:
- Minh họa cách tạo 1 Node trong ROS 2 bằng rclpy.
- Minh họa khai báo và sử dụng Parameter (tham số có thể cấu hình từ bên ngoài).
- Minh họa tạo Publisher và Timer để phát dữ liệu tuần hoàn lên Topic.
- Sử dụng cả std_msgs/String và sensor_msgs/JointState (thực tế cho cánh tay robot).
"""

import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import JointState


class ArmJointPublisherNode(Node):
    def __init__(self):
        # 1. Khởi tạo Node với tên 'arm_joint_publisher'
        super().__init__('arm_joint_publisher')

        # 2. Khai báo Parameters (Tham số cấu hình)
        # Các tham số này có thể thay đổi lúc chạy: ros2 run ... --ros-args -p robot_name:=my_arm
        self.declare_parameter('robot_name', 'openarm_v1')
        self.declare_parameter('publish_rate_hz', 2.0)

        # Lấy giá trị tham số
        self.robot_name = self.get_parameter('robot_name').get_parameter_value().string_value
        self.publish_rate = self.get_parameter('publish_rate_hz').get_parameter_value().double_value

        # 3. Tạo Publishers
        # Publisher 1: Gửi trạng thái văn bản (/arm_status)
        self.status_publisher_ = self.create_publisher(
            msg_type=String,
            topic='/arm_status',
            qos_profile=10  # Queue size (độ sâu hàng đợi)
        )

        # Publisher 2: Gửi góc quay các khớp cánh tay (/joint_states)
        self.joint_publisher_ = self.create_publisher(
            msg_type=JointState,
            topic='/joint_states',
            qos_profile=10
        )

        # 4. Tạo Timer gọi hàm callback định kỳ
        timer_period = 1.0 / self.publish_rate
        self.timer_ = self.create_timer(timer_period, self.timer_callback)

        self.step_counter_ = 0
        self.get_logger().info(
            f'>>> [Node Init] {self.get_name()} đã khởi động! Robot: "{self.robot_name}", Tần số: {self.publish_rate} Hz'
        )

    def timer_callback(self):
        """Hàm callback được gọi tự động theo chu kỳ Timer."""
        now = self.get_clock().now()
        self.step_counter_ += 1

        # --- A. Tạo và phát message String (/arm_status) ---
        status_msg = String()
        status_msg.data = f'[{self.robot_name}] Hệ thống đang hoạt động bình thường, chu kỳ #{self.step_counter_}'
        self.status_publisher_.publish(status_msg)

        # --- B. Tạo và phát message JointState (/joint_states) ---
        joint_msg = JointState()
        joint_msg.header.stamp = now.to_msg()
        joint_msg.header.frame_id = 'base_link'
        joint_msg.name = ['joint_base', 'joint_shoulder', 'joint_elbow', 'joint_wrist']

        # Giả lập vị trí khớp dao động hình sin
        t = self.step_counter_ * 0.1
        joint_msg.position = [
            math.sin(t),
            math.sin(t + 0.5),
            math.cos(t),
            math.sin(2 * t)
        ]
        joint_msg.velocity = [0.1, 0.1, -0.1, 0.2]
        joint_msg.effort = []  # Lực/mô-men xoắn (tùy chọn)

        self.joint_publisher_.publish(joint_msg)

        self.get_logger().info(
            f'Đã phát JointState #{self.step_counter_} -> J1: {joint_msg.position[0]:.2f}, J2: {joint_msg.position[1]:.2f}'
        )


def main(args=None):
    # Khởi tạo thư viện rclpy
    rclpy.init(args=args)

    # Khởi tạo đối tượng Node
    node = ArmJointPublisherNode()

    try:
        # Giữ node chạy và xử lý callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Dừng node theo yêu cầu người dùng (Ctrl+C).')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
