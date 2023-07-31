import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    usb_cam_node = Node(
        package='usb_cam',
        executable='usb_cam_node_exe',
        output='screen',
        # parameters=[param_file]  # You can include other parameters if required
    )

    return LaunchDescription([usb_cam_node])
