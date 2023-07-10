# Copyright (c) 2023 Fixstars inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
import launch
import launch_ros.actions

import pytest
import launch_pytest

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

import time
from threading import Thread

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
                package="py_accum",
                executable="accum",
            ),
        ]
    )


@pytest.mark.launch(fixture=generate_test_description)
def test_accumulation(make_test_node):
    node = make_test_node
    for i in range(10):
        node.publish(Int32(data=i))
        time.sleep(0.01)

    end_time = time.time() + 5
    while time.time() < end_time:
        if len(node.msgs) == 10:
            break
        time.sleep(0.1)

    assert len(node.msgs) == 10
    assert node.msgs[-1] == Int32(data=45)


@pytest.fixture
def make_test_node():
    rclpy.init()
    node = MakeTestNode()
    node.start()
    yield node
    node.destroy_node()
    rclpy.shutdown()


class MakeTestNode(Node):
    def __init__(self):
        super().__init__("test_node")

    def start(self):
        self._pub = self.create_publisher(Int32, "src", 10)
        self._sub = self.create_subscription(Int32, "dst", self._msg_received, 10)
        self.msgs = []
        self._ros_spin_thread = Thread(
            target=lambda node: rclpy.spin(node), args=(self,)
        )
        self._ros_spin_thread.start()

        self._wait_for_connect()

    def publish(self, data):
        self._pub.publish(data)

    def _msg_received(self, msg):
        self.msgs.append(msg)

    def _wait_for_connect(self, timeout_s=5):
        end_time = time.time() + timeout_s
        while time.time() < end_time:
            cnt = self._pub.get_subscription_count()
            if cnt > 0:
                return True
            time.sleep(0.1)
        return False
