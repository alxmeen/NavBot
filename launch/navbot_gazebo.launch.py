#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    package_name = 'navbot'
    navbot_launch = IncludeLaunchDescription(
                        PythonLaunchDescriptionSource([os.path.join(
                            get_package_share_directory(package_name), 'launch', 'navbot.launch.py'
                            )]), launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'true'}.items())
    
    declare_world_arg = DeclareLaunchArgument(
        'world',
        default_value='empty.sdf',
        description='SDF world file to load'
    )

    declare_gz_args = DeclareLaunchArgument(
        'gz_args', default_value=['-r -v4 ', LaunchConfiguration('world'), ' --render-engine ogre'],
        description=' Arguments to pass to Gazebo Sim'
    )
    
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
                    launch_arguments={'gz_args': LaunchConfiguration('gz_args'), 'on_exit_shutdown': 'true'}.items()
             )

    spawn_entity = Node(package='ros_gz_sim', executable='create',
                        arguments=['-topic', 'robot_description',
                                   '-name', 'NavBot'], output= 'screen')
    
    return LaunchDescription([navbot_launch, declare_world_arg, declare_gz_args, gazebo, spawn_entity])
