#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):  # inherits from Node from rclpy.node

    def __init__(self):
        self.counter_ = 0
        super().__init__('my_test_node')  # node name, different from file name
        self.get_logger().info("Hello from ROS2")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)  # initialize ROS communications
    node = MyNode()
    rclpy.spin(node)  # enables all callbacks too
    rclpy.shutdown()  # destroys node and everything in it

if __name__ == '__main__':  # directly execute file from terminal
    main()
