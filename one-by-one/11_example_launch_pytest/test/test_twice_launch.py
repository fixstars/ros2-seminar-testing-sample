import launch
import launch_ros.actions

import pytest
import launch_pytest

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

import time
from threading import Event, Thread

import domain_coordinator
import contextlib
import os

stack = contextlib.ExitStack()
if "ROS_DOMAIN_ID" not in os.environ and "DISABLE_ROS_ISOLATION" not in os.environ:
    domain_id = stack.enter_context(domain_coordinator.domain_id())
    print("ROS_DOMAIN_ID is", domain_id)
    os.environ["ROS_DOMAIN_ID"] = str(domain_id)


@launch_pytest.fixture
def generate_test_description():
    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package="example_launch_pytest",
                executable="twice",
            ),
        ]
    )


@pytest.mark.launch(fixture=generate_test_description)
def test_success(make_test_node):
    node = make_test_node
    node.publish(Int32(data=2))
    assert node.msg_event_object.wait(timeout=5.0), "Did not receive msgs"
    assert node.msgs[0] == Int32(data=4)


@pytest.mark.launch(fixture=generate_test_description)
def test_success2(make_test_node):
    node = make_test_node
    node.publish(Int32(data=-1))
    assert node.msg_event_object.wait(timeout=5.0), "Did not receive msgs"
    assert node.msgs[0] == Int32(data=-2)


# @pytest.mark.launch(fixture=generate_test_description)
# def test_failure(make_test_node):
#     node = make_test_node
#     node.publish(Int32(data=3))
#     assert node.msg_event_object.wait(timeout=5.0), "Did not receive msgs"
#     assert node.msgs[0] == Int32(data=5)


@pytest.fixture
def make_test_node():
    rclpy.init()
    node = DummyTestNode()
    node.start()
    yield node
    rclpy.shutdown()


class DummyTestNode(Node):
    def __init__(self):
        super().__init__("test_node")
        self.msg_event_object = Event()

    def start(self):
        self._pub = self.create_publisher(Int32, "src", 10)
        self._sub = self.create_subscription(Int32, "dst", self._msg_received, 10)
        self.msgs = []
        self._ros_spin_thread = Thread(
            target=lambda node: rclpy.spin(node), args=(self,)
        )
        self._ros_spin_thread.start()

        assert self._wait_for_connect()

    def publish(self, data):
        self._pub.publish(data)

    def _msg_received(self, msg):
        self.msgs.append(msg)
        self.msg_event_object.set()

    def _wait_for_connect(self, timeout_s=5):
        end_time = time.time() + timeout_s
        while time.time() < end_time:
            cnt = self._pub.get_subscription_count()
            if cnt > 0:
                return True
            time.sleep(0.1)
        return False
