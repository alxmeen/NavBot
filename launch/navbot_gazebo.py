#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, DeclareLaunchArgument, 
                            SetEnvironmentVariable, SetLaunchConfiguration)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, TextSubstitution

def generate_launch_description():

    package_name = 'navbot'
    pkg_ros_gz_sim = get_package_share_directory('')
    navbot_launch = IncludeLaunchDescription(
                        PythonLaunchDescriptionSource([os.path.join(
                            get_package_share_directory(package_name), 'launch', 'navbot.launch.py'
                            )]), launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'true'}.items())