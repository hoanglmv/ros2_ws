#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openarm_demo_py: topic_subscriber.py
Mục đích:
- Minh họa cách tạo Subscriber trong ROS 2.
- Nhận dữ liệu bất đồng bộ từ các Topic qua hàm Callback.
- Lắng nghe Topic /arm_status và /joint_states.
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from std_msgs.msg import String
from sensor_msgs.msg import JointState


class ArmJointSubscriberNode(Node):
    def __init__(self):
        super().__init__('arm_joint_subscriber')

        # Cấu hình QoS (Quality of Service) chuẩn mực trong ROS 2
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,  # Đảm bảo gói tin không bị rơi rớt
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )

        # 1. Subscriber cho Topic /arm_status
        self.status_sub_ = self.create_subscription(
            String,
            '/arm_status',
            self.status_callback,
            qos_profile
        )

        # 2. Subscriber cho Topic /joint_states
        self.joint_sub_ = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_callback,
            qos_profile
        )

        self.get_logger().info(f'>>> [Node Init] {self.get_name()} sẵn sàng nhận dữ liệu từ các topics!')

    def status_callback(self, msg: String):
        """Callback xử lý tin nhắn trạng thái."""
        self.get_logger().info(f'[Nhận Status]: "{msg.data}"')

    def joint_callback(self, msg: JointState):
        """Callback xử lý dữ liệu góc khớp robot."""
        joint_info = ', '.join([f'{name}: {pos:.3f} rad' for name, pos in zip(msg.name, msg.position)])
        self.get_logger().info(f'[Nhận Joints]: {joint_info}')


def main(args=None):
    rclpy.init(args=args)
    node = ArmJointSubscriberNode()

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
