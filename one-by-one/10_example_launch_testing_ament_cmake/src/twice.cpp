#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/int32.hpp>

using Int32 = std_msgs::msg::Int32;

class TwiceNode : public rclcpp::Node {
public:
  TwiceNode() : Node("twice", "") {
    pub_ = this->create_publisher<Int32>("dst", 10);
    sub_ = this->create_subscription<Int32>(
        "src", 10, [this](const Int32::ConstSharedPtr src) -> void {
          auto output = Int32();
          output.data = src->data * 2;
          this->pub_->publish(output);
        });
  }

private:
  rclcpp::Subscription<Int32>::SharedPtr sub_;
  rclcpp::Publisher<Int32>::SharedPtr pub_;
};

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<TwiceNode>());
  rclcpp::shutdown();
  return 0;
}
