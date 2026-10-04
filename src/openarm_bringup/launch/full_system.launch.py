#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openarm_bringup: full_system.launch.py
Mục đích:
- Khởi chạy toàn bộ hệ sinh thái demo: Publisher, Subscriber, Service Server.
- Nạp cấu hình tham số tự động từ file YAML (config/arm_params.yaml).
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    bringup_dir = get_package_share_directory('openarm_bringup')
    param_file = os.path.join(bringup_dir, 'config', 'arm_params.yaml')

    publisher_node = Node(
        package='openarm_demo_py',
        executable='arm_publisher',
        name='arm_joint_publisher',
        output='screen',
        parameters=[param_file]
    )

    subscriber_node = Node(
        package='openarm_demo_py',
        executable='arm_subscriber',
        name='arm_joint_subscriber',
        output='screen'
    )

    service_server_node = Node(
        package='openarm_demo_py',
        executable='arm_service_server',
        name='arm_service_server',
        output='screen'
    )

    return LaunchDescription([
        publisher_node,
        subscriber_node,
        service_server_node
    ])
