import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():
    param_file = os.path.join(
        get_package_share_directory('actiarobot'), 'config', 'urg.yaml'
    )

    urg_node2_launch_file = os.path.join(
        get_package_share_directory('urg_node2'), 'launch', 'urg_node2.launch.py'
    )

    # tf_odom_to_base_link = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='odom_to_base_broadcaster',
    #     arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link']
    # )

    # tf_map_to_odom = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='map_to_odom_broadcaster',
    #     arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom']
    # )

    return LaunchDescription([
        # tf_odom_to_base_link,
        # tf_map_to_odom,
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(urg_node2_launch_file),
            launch_arguments={'param_file': param_file}.items(),
        )
    ])
