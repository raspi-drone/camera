import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy
from std_msgs.msg import String


class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')

        qos = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.BEST_EFFORT
        )
        self.publisher_ = self.create_publisher(String, '/topic', qos)
        
        self.declare_parameter('timer_period', 0.5)
        timer_period = self.get_parameter('timer_period').value
        
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World: {self.i}'

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1
        


def main(args=None):
    rclpy.init(args=args)

    my_node = MyNode()

    try:
        rclpy.spin(my_node)
    except KeyboardInterrupt:
        pass
    finally:
        my_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()