#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from  std_msgs.msg import String

class WriterNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("this is %s" % name)
        # self.command_subscribe = self.create_subscription(String,"xbox_button_input",self.command_callback,10)

    def command_callback(self,msg):
        self.get_logger().info(f'收到命令:[{msg.data}]')



def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = WriterNode("wheel")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy

   
