from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera',
            executable='pi_camera',
            name='pi_camera',
            output='screen',
            emulate_tty=True
        )
    ])