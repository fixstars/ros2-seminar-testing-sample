# Copyright (c) 2023 Fixstars inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
import pytest
import launch_pytest
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import AnyLaunchDescriptionSource
from ament_index_python import get_package_share_directory

from pathlib import Path

import rclpy
import rclpy.node
from std_msgs.msg import Int32
from threading import Thread

import domain_coordinator
import contextlib
import os

stack = contextlib.ExitStack()
if "ROS_DOMAIN_ID" not in os.environ and "DISABLE_ROS_ISOLATION" not in os.environ:
    domain_id = stack.enter_context(domain_coordinator.domain_id())
    print("ROS_DOMAIN_ID is", domain_id)
    os.environ["ROS_DOMAIN_ID"] = str(domain_id)


@pytest.fixture
def integration_launch():
    return IncludeLaunchDescription(
        AnyLaunchDescriptionSource(
            str(
                Path(get_package_share_directory("integration"))
                / "launch"
                / "integration.launch.yaml"
            )
        )
    )


@pytest.fixture
def testdata():
    path_to_test = Path(__file__).parent.parent

    return ExecuteProcess(
        cmd=[
            "ros2",
            "bag",
            "play",
            str(path_to_test / "data" / "testdata.bag"),
            "--delay",
            "1",
            "--wait-for-all-acked",
            "1000",
        ],
        shell=True,
    )


@pytest.fixture
def receiver():
    rclpy.init()
    node = ReceiverNode()
    node.start()
    yield node
    node.destroy_node()
    rclpy.shutdown()


@launch_pytest.fixture
def generate_test_description(testdata, integration_launch):
    return LaunchDescription(
        [
            testdata,
            integration_launch,
        ]
    )


@pytest.mark.launch(fixture=generate_test_description)
async def test_should_be_90(testdata, receiver):
    await testdata.get_asyncio_future()
    yield
    assert receiver.msgs[-1] == Int32(data=90)


class ReceiverNode(rclpy.node.Node):
    def __init__(self):
        super().__init__("test_receiver")

    def start(self):
        self.msgs = []
        self._sub = self.create_subscription(
            Int32, "dst", lambda msg: self.msgs.append(msg), 10
        )
        self._ros_spin_thread = Thread(
            target=lambda node: rclpy.spin(node), args=(self,)
        )
        self._ros_spin_thread.start()
