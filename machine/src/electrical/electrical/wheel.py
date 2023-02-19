#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from  std_msgs.msg import String
import json
from Rosmaster_Lib import Rosmaster

class WriterNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("this is %s" % name)
        # 创建订阅者
        self.command_subscribe_ = self.create_subscription(String,"command",self.command_callback,10)
        self.bot = Rosmaster()
        self.bot.create_receive_threading()

    def command_callback(self,msg):
        self.get_logger().info(f'收到命令:[{msg.data}]')
        message = msg.data
        object_message = json.loads(message)
        # self.get_logger().info(f'收到命令:[{object_message,type(object_message)}]')
        # 摇杆
        if ("type" in object_message):
            print(object_message["type"])
            if (object_message["type"]=="JOYAXISMOTION"): 
                # left_left_right = object_message["value"][0]
                # left_up_down = object_message["value"][1]
                right_left_right = object_message["value"][3]
                right_up_down = object_message["value"][4]
                print(right_left_right,right_up_down)
                # 上 左  负数
                speed = int(100*right_up_down)
                print("speed:",speed)
                self.bot.set_motor(0, speed, 0, speed)
                # if(right_up_down>=0):
                #     speed = int(100*right_up_down)
                #     print("speed:",speed)
                #     self.bot.set_motor(0, speed, 0, speed)
                #     pass
                # else:
                #     pass




        else :
            pass
            
            # if (right_up_down>0): #后退
            #     pass 
            # elif (right_up_down<0): #前进



def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = WriterNode("wheel")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy

   
