from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():
    urdf_path = os.path.join(get_package_share_path('mycobot_description'), 'urdf', '600_urdf', 'mycobot_600_urdf.urdf')

    robot_description = ParameterValue(Command(['xacro ',urdf_path]), value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )
    
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    rivz2_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(get_package_share_path('mycobot_280pi'), 'config', 'config.rviz')]
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rivz2_node
    ])