# Copyright (c) 2023 Fixstars inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

from .accumulator import Accumulator


class AccumulatorNode(Node):
    def __init__(self):
        super().__init__("accum")
        self._acc = Accumulator()
        self._pub = self.create_publisher(Int32, "dst", 10)
        self._sub = self.create_subscription(Int32, "src", self.callback, 10)

    def callback(self, msg):
        self._acc.add(msg.data)
        self._pub.publish(Int32(data=self._acc.get()))


def main(args=None):
    rclpy.init(args=args)
    node = AccumulatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
