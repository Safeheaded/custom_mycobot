import os

from ament_index_python import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    res = []

    model_launch_arg = DeclareLaunchArgument(
        "model",
        default_value=os.path.join(
            get_package_share_directory("mycobot_description"),
            "urdf/mycobot/mycobot_urdf.urdf"
        ),
    )
    res.append(model_launch_arg)

    rvizconfig_launch_arg = DeclareLaunchArgument(
        "rvizconfig",
        default_value=os.path.join(
            get_package_share_directory("mycobot_280"),
            "config/mycobot.rviz"
        ),
    )
    res.append(rvizconfig_launch_arg)

    gui_launch_arg = DeclareLaunchArgument(
        "gui",
        default_value="true",
    )
    res.append(gui_launch_arg)

    num_launch_arg = DeclareLaunchArgument(
        "num",
        default_value="0",
    )
    res.append(num_launch_arg)

    # 	<node name="opencv_camera" pkg="mycobot_280" type="opencv_camera" args="$(arg num)"/>
    mycobot_280_node = Node(
        name="opencv_camera",
        package="mycobot_280",
        executable="opencv_camera.cpp",
        arguments=[LaunchConfiguration("num")]
    )
    res.append(mycobot_280_node)

    mycobot_280_node = Node(
        name="detect_marker",
        package="mycobot_280",
        executable="detect_marker"
    )
    res.append(mycobot_280_node)

    mycobot_280_node = Node(
        name="following_marker",
        package="mycobot_280",
        executable="following_marker"
    )
    res.append(mycobot_280_node)

    return LaunchDescription(res)