# Copyright (c) 2023 Fixstars inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
import rosbag2_py
from rclpy.serialization import serialize_message

from std_msgs.msg import Int32


def main():
    path = "testdata.bag"
    storage_options = rosbag2_py.StorageOptions(uri=path, storage_id="sqlite3")
    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format="cdr",
        output_serialization_format="cdr",
    )

    writer = rosbag2_py.SequentialWriter()
    writer.open(storage_options, converter_options)

    topic_name = "/src"
    topic = rosbag2_py.TopicMetadata(
        name=topic_name,
        type="std_msgs/msg/Int32",
        serialization_format="cdr",
    )
    writer.create_topic(topic)

    for i in range(10):
        msg = Int32(data=i)
        timestamp = i * 100000000  # delta time = 100ms
        writer.write(topic_name, serialize_message(msg), timestamp)

    # Close bag
    del writer


if __name__ == "__main__":
    main()
