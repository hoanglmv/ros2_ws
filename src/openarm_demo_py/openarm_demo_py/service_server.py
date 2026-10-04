#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openarm_demo_py: service_server.py
Mục đích:
- Minh họa cách tạo Service Server trong ROS 2 (mô hình Request - Response).
- Phục vụ các tác vụ theo lệnh: Bật/Tắt nguồn tay máy (/set_arm_power)
  và tính toán góc mục tiêu (/calc_target_pos).
"""

import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool, AddTwoInts


class ArmServiceServerNode(Node):
    def __init__(self):
        super().__init__('arm_service_server')

        self.power_on = False

        # 1. Tạo Service Bật/Tắt nguồn: /set_arm_power
        self.srv_power = self.create_service(
            SetBool,
            '/set_arm_power',
            self.handle_set_arm_power
        )

        # 2. Tạo Service Tính toán vị trí: /calc_target_pos
        self.srv_calc = self.create_service(
            AddTwoInts,
            '/calc_target_pos',
            self.handle_calc_target_pos
        )

        self.get_logger().info(
            f'>>> [Service Server Init] {self.get_name()} đã khởi động. Các services sẵn sàng:\n'
            '  - /set_arm_power (example_interfaces/srv/SetBool)\n'
            '  - /calc_target_pos (example_interfaces/srv/AddTwoInts)'
        )

    def handle_set_arm_power(self, request, response):
        """Xử lý yêu cầu bật/tắt nguồn motor tay máy."""
        self.power_on = request.data
        if self.power_on:
            response.success = True
            response.message = 'Nguồn động cơ tay máy ĐÃ ĐƯỢC BẬT (Motors Enabled).'
        else:
            response.success = True
            response.message = 'Nguồn động cơ tay máy ĐÃ ĐƯỢC NGẮT (Motors Disabled).'

        self.get_logger().info(f'[Service Call] /set_arm_power: request={request.data} -> {response.message}')
        return response

    def handle_calc_target_pos(self, request, response):
        """Xử lý tính toán cộng hai giá trị (ví dụ toạ độ tương đối)."""
        response.sum = request.a + request.b
        self.get_logger().info(f'[Service Call] /calc_target_pos: a={request.a}, b={request.b} -> sum={response.sum}')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ArmServiceServerNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Dừng node service server (Ctrl+C).')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
