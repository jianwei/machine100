#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import pygame

class WriterNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("this is %s" % name)



def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = WriterNode("wheel")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy

   
