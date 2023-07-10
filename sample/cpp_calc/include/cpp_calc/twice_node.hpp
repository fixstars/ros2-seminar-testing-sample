// Copyright (c) 2023 Fixstars inc.
//
// Use of this source code is governed by an MIT-style
// license that can be found in the LICENSE file or at
// https://opensource.org/licenses/MIT.
#pragma once

#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/int32.hpp>

namespace cpp_calc
{
using Int32 = std_msgs::msg::Int32;

class TwiceNode : public rclcpp::Node
{
public:
  TwiceNode();

private:
  rclcpp::Subscription<Int32>::SharedPtr sub_;
  rclcpp::Publisher<Int32>::SharedPtr pub_;
};
}  // namespace cpp_calc
