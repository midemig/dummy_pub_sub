from nav_msgs.msg import Odometry

from rcl_interfaces.msg import SetParametersResult

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from std_msgs.msg import Empty

class DummyPublisher(Node):
    def __init__(self):
        super().__init__('dummy_publisher')

        self.declare_parameter('message_type', 'Empty')
        self.declare_parameter('topic_name', 'dummy_topic')
        self.declare_parameter('frequency', 1.0)

        message_type = self.get_parameter('message_type').get_parameter_value().string_value
        topic_name = self.get_parameter('topic_name').get_parameter_value().string_value
        frequency = self.get_parameter('frequency').get_parameter_value().double_value

        if message_type == 'Image':
            self.publisher_ = self.create_publisher(Image, topic_name, 10)
            self.msg = Image()
        elif message_type == 'Odometry':
            self.publisher_ = self.create_publisher(Odometry, topic_name, 10)
            self.msg = Odometry()
        else:
            self.publisher_ = self.create_publisher(Empty, topic_name, 10)
            self.msg = Empty()

        self.timer = self.create_timer(1.0 / frequency, self.timer_callback)
        self.add_on_set_parameters_callback(self.parameter_callback)

    def parameter_callback(self, params):
        for param in params:
            if param.name == 'frequency' and param.type_ == param.Type.DOUBLE:
                self.timer.cancel()
                self.timer = self.create_timer(1.0 / param.value, self.timer_callback)
        return SetParametersResult(successful=True)

    def timer_callback(self):
        self.publisher_.publish(self.msg)
        # self.get_logger().info(f'Publishing {self.msg.__class__.__name__} message on {self.publisher_.topic_name}')

def main(args=None):
    rclpy.init(args=args)
    node = DummyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
