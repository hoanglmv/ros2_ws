#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openarm_demo_py: service_client.py
Mục đích:
- Minh họa cách viết Service Client trong ROS 2 (Client gọi tới Server).
- Kiểm tra service có tồn tại bằng wait_for_service.
- Gửi Request bất đồng bộ (call_async) và xử lý Response trả về.
"""

import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool


class ArmServiceClientNode(Node):
    def __init__(self):
        super().__init__('arm_service_client')

        # Tạo Client liên kết với service '/set_arm_power'
        self.client_ = self.create_client(SetBool, '/set_arm_power')

        # Chờ Service Server khởi động
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Service /set_arm_power chưa online, đang đợi...')

        self.get_logger().info('Service /set_arm_power đã sẵn sàng!')

    def send_request(self, power_state: bool):
        """Gửi request tới Service Server."""
        request = SetBool.Request()
        request.data = power_state

        self.get_logger().info(f'Đang gửi yêu cầu đặt nguồn thành: {power_state}')
        future = self.client_.call_async(request)
        return future


def main(args=None):
    rclpy.init(args=args)
    client_node = ArmServiceClientNode()

    # Mặc định bật nguồn (True), nếu có tham số dòng lệnh 'false' hoặc '0' thì tắt (False)
    power_state = True
    if len(sys.argv) > 1 and sys.argv[1].lower() in ['0', 'false', 'off']:
        power_state = False

    future = client_node.send_request(power_state)

    # Chờ phản hồi từ Server (spin_until_future_complete)
    rclpy.spin_until_future_complete(client_node, future)

    try:
        response = future.result()
        client_node.get_logger().info(f'>>> Kết quả trả về từ Server:\n  Success: {response.success}\n  Message: "{response.message}"')
    except Exception as e:
        client_node.get_logger().error(f'Lỗi khi gọi service: {e}')

    client_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
