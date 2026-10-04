#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openarm_bringup: arm_pub_sub.launch.py
Mục đích:
- Minh họa cách viết file Launch trong ROS 2 bằng Python (chuẩn ROS 2).
- Khởi chạy đồng thời 2 Nodes: arm_publisher và arm_subscriber.
- Truyền tham số dòng lệnh thông qua DeclareLaunchArgument và LaunchConfiguration.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # 1. Khai báo các đối số Launch (cho phép người dùng ghi đè khi chạy: ros2 launch ... robot_name:=my_robot)
    robot_name_arg = DeclareLaunchArgument(
        'robot_name',
        default_value='OpenArm_Robot_1',
        description='Tên định danh cho cánh tay robot'
    )

    publish_rate_arg = DeclareLaunchArgument(
        'publish_rate_hz',
        default_value='3.0',
        description='Tần số xuất dữ liệu khớp (Hz)'
    )

    # 2. Định nghĩa Node Publisher
    publisher_node = Node(
        package='openarm_demo_py',
        executable='arm_publisher',
        name='arm_joint_publisher',
        output='screen',
        parameters=[{
            'robot_name': LaunchConfiguration('robot_name'),
            'publish_rate_hz': LaunchConfiguration('publish_rate_hz'),
        }]
    )

    # 3. Định nghĩa Node Subscriber
    subscriber_node = Node(
        package='openarm_demo_py',
        executable='arm_subscriber',
        name='arm_joint_subscriber',
        output='screen'
    )

    # 4. Trả về LaunchDescription gom tất cả các action
    return LaunchDescription([
        robot_name_arg,
        publish_rate_arg,
        publisher_node,
        subscriber_node
    ])
