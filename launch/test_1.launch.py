from launch import LaunchDescription
from launch.actions import TimerAction

from launch_ros.actions import Node


def generate_launch_description():

    pub_params = [
        # [frequency, topic_name, message_type]
        [20.0, '/camera', 'Image'],
        [10.0, '/odom', 'Odometry'],
        [5.0, '/filtered_odom', 'Odometry']
    ]

    sub_params = [
        # [topic_name, message_type]
        ['/camera', 'Image'],
        ['/odom', 'Odometry'],
        ['/filtered_odom', 'Odometry']
    ]

    delay_sub_params = [
        # [topic_name, message_type, period]
        ['/camera', 'Image', 10.0],
        ['/odom', 'Odometry', 15.0],
    ]

    pub_nodes = []
    sub_nodes = []
    delay_sub_nodes = []

    for i, params in enumerate(pub_params):
        pub_nodes.append(Node(
            package='dummy_pub_sub',
            executable='dummy_pub_node',
            name=f'dummy_pub_sub_{i}',
            parameters=[{'frequency': params[0]},
                        {'topic_name': params[1]},
                        {'message_type': params[2]}],
            output='screen'
        ))

    for i, params in enumerate(sub_params):
        sub_nodes.append(Node(
            package='dummy_pub_sub',
            executable='dummy_sub_node',
            name=f'dummy_subscriber_{i}',
            parameters=[{'topic_name': params[0]},
                        {'message_type': params[1]}],
            output='screen'
        ))

    for i, params in enumerate(delay_sub_params):
        delay_sub_nodes.append(TimerAction(
            period=params[2],
            actions=[
                Node(
                    package='dummy_pub_sub',
                    executable='dummy_sub_node',
                    name=f'dummy_subscriber_delay_{i}',
                    parameters=[{'topic_name': params[0]},
                                {'message_type': params[1]}],
                    output='screen'
                )
            ]
        ))

    all_nodes = pub_nodes + sub_nodes + delay_sub_nodes

    return LaunchDescription(all_nodes)

