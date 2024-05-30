import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sam_test',
            namespace='depth2color',
            executable='depth2color',
            # remappings=[('/input_image', '/camera/depth/image_rect_raw')],
        ),
    ])