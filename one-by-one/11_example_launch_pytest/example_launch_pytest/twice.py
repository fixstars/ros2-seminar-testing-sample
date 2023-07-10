import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

class TwiceNode(Node):
    def __init__(self):
        super().__init__("twice")
        self._pub = self.create_publisher(Int32, "dst", 10)
        self._sub = self.create_subscription(
            Int32,
            "src",
            lambda msg: self._pub.publish(Int32(data=msg.data * 2)),
            10
        )

def main(args=None):
    rclpy.init(args=args)
    node = TwiceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

