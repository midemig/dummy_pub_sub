from nav_msgs.msg import Odometry

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

class DummySubNode(Node):
    def __init__(self):
        super().__init__('dummy_sub_node')

        self.declare_parameter('topic_name', 'dummy_topic')
        self.declare_parameter('message_type', 'sensor_msgs/Image')

        topic_name = self.get_parameter('topic_name').get_parameter_value().string_value
        message_type = self.get_parameter('message_type').get_parameter_value().string_value

        if message_type == 'Image':
            self.subscription = self.create_subscription(
                Image,
                topic_name,
                self.listener_callback,
                10)
        elif message_type == 'Odometry':
            self.subscription = self.create_subscription(
                Odometry,
                topic_name,
                self.listener_callback,
                10)
        else:
            self.get_logger().error('Unsupported message type')
            rclpy.shutdown()

    def listener_callback(self, msg):
        # Empty callback, discards the received data
        pass

def main(args=None):
    rclpy.init(args=args)
    node = DummySubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
