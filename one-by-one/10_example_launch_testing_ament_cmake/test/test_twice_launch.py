import unittest
import time

import launch
import launch_ros.actions

import launch_testing
import launch_testing.actions

import pytest

from rclpy.node import Node

import rclpy
import rclpy.executors
from std_msgs.msg import Int32


@pytest.mark.launch_test
def generate_test_description():
    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package="example_launch_testing_ament_cmake",
                executable="twice",
            ),
            launch_testing.actions.ReadyToTest(),
        ]
    )


class TestTwice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self._node = DummyTestNode()

    def tearDown(self):
        self._node.destroy_node()

    def test_success(self):
        test_data = Int32(data=1)
        self._node.publish(test_data)

        ans = self._node.get_message()
        self.assertEqual(ans, Int32(data=2))

    def test_success2(self):
        test_data = Int32(data=-1)
        self._node.publish(test_data)

        ans = self._node.get_message()
        self.assertEqual(ans, Int32(data=-2))

    # def test_failure(self):
    #     test_data = Int32(data=1)
    #     self._node.publish(test_data)

    #     ans = self._node.get_message()
    #     self.assertEqual(ans, Int32(data=3))


class DummyTestNode(Node):
    def __init__(self):
        super().__init__("test_node")
        self._msgs = []
        self._pub = self.create_publisher(Int32, "src", 10)
        self._sub = self.create_subscription(
            Int32, "dst", lambda msg: self._msgs.append(msg), 10
        )

        assert self._wait_for_connect()

    def publish(self, data):
        self._pub.publish(data)

    def get_message(self, timeout_s=5.0):
        start_len = len(self._msgs)
        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(self)

        try:
            end_time = time.time() + timeout_s
            while time.time() < end_time:
                executor.spin_once(timeout_sec=0.1)
                if start_len != len(self._msgs):
                    break

        finally:
            executor.remove_node(self)
            executor.shutdown()

        assert start_len != len(self._msgs)
        return self._msgs[-1]

    def _wait_for_connect(self, timeout_s=5):
        end_time = time.time() + timeout_s
        while time.time() < end_time:
            cnt = self._pub.get_subscription_count()
            if cnt > 0:
                return True
            time.sleep(0.1)
        return False
