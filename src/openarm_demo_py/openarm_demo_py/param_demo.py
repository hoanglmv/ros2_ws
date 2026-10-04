#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openarm_demo_py: param_demo.py
Mục đích:
- Minh họa cách khai báo và quản lý Parameters (Tham số động) trong ROS 2.
- Lắng nghe sự kiện thay đổi tham số trong thời gian thực bằng callback on_set_parameters.
- Kiểm tra tính hợp lệ của tham số trước khi chấp thuận (parameter validation).
"""

import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult, ParameterDescriptor


class ArmParamDemoNode(Node):
    def __init__(self):
        super().__init__('arm_param_demo')

        # 1. Khai báo các parameters kèm theo mô tả (Descriptor)
        speed_desc = ParameterDescriptor(description='Tốc độ tối đa của cánh tay (0.1 - 2.0 rad/s)')
        self.declare_parameter('max_speed', 1.0, speed_desc)
        self.declare_parameter('arm_mode', 'MANUAL')
        self.declare_parameter('enable_collision_check', True)

        # 2. Đăng ký hàm callback khi có yêu cầu thay đổi parameter từ bên ngoài
        self.add_on_set_parameters_callback(self.parameters_callback)

        # 3. Tạo Timer để in ra giá trị parameters hiện tại mỗi 3 giây
        self.timer = self.create_timer(3.0, self.report_params)

        self.get_logger().info('>>> [Param Demo Init] Node tham số đã chạy.')
        self.report_params()

    def report_params(self):
        max_speed = self.get_parameter('max_speed').value
        arm_mode = self.get_parameter('arm_mode').value
        col_check = self.get_parameter('enable_collision_check').value

        self.get_logger().info(
            f'[Trạng thái Parameters] max_speed={max_speed}, arm_mode="{arm_mode}", enable_collision_check={col_check}'
        )

    def parameters_callback(self, params):
        """Callback kiểm tra tính hợp lệ khi người dùng chạy lệnh 'ros2 param set'."""
        result = SetParametersResult()
        result.successful = True

        for param in params:
            if param.name == 'max_speed':
                # Kiểm tra ràng buộc giá trị tốc độ
                if param.value <= 0.0 or param.value > 2.0:
                    result.successful = False
                    result.reason = 'max_speed phải nằm trong khoảng (0.0, 2.0]!'
                    self.get_logger().warn(f'Từ chối cập nhật max_speed={param.value}: {result.reason}')
                    return result
                else:
                    self.get_logger().info(f'Cập nhật thành công max_speed -> {param.value}')

            elif param.name == 'arm_mode':
                allowed_modes = ['MANUAL', 'AUTO', 'CALIBRATION']
                if param.value not in allowed_modes:
                    result.successful = False
                    result.reason = f'arm_mode phải thuộc {allowed_modes}'
                    self.get_logger().warn(f'Từ chối cập nhật arm_mode: {result.reason}')
                    return result
                else:
                    self.get_logger().info(f'Cập nhật thành công arm_mode -> {param.value}')

        return result


def main(args=None):
    rclpy.init(args=args)
    node = ArmParamDemoNode()

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
