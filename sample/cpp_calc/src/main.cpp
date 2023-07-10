// Copyright (c) 2023 Fixstars inc.
//
// Use of this source code is governed by an MIT-style
// license that can be found in the LICENSE file or at
// https://opensource.org/licenses/MIT.
#include <rclcpp/rclcpp.hpp>
#include <cpp_calc/twice_node.hpp>

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<cpp_calc::TwiceNode>());
  rclcpp::shutdown();
  return 0;
}
