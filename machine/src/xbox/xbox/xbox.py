#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import pygame
import json
from std_msgs.msg import String

class WriterNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("this is %s" % name)
        self.joy()
        # self.command_publisher_ = self.create_publisher(String,"command", 10) 
        # self.timer = self.create_timer(0.5, self.timer_callback)

    # def timer_callback(self):
    #     """
    #     定时器回调函数
    #     """
    #     msg = String()
    #     msg.data = json.dumps({"message":'message',"value":1,'type':2})
    #     self.command_publisher_.publish(msg) 
    #     self.get_logger().info(f'发布了指令：{msg.data}')    #打印一下发布的数据
    
    def joy(self):
        # command_publisher = self.create_publisher(String,"xbox_button_input", 10) 
        # 模块初始化
        pygame.init()
        pygame.joystick.init()
        # 若只连接了一个手柄，此处带入的参数一般都是0
        joystick = pygame.joystick.Joystick(0)
        # 手柄对象初始化
        joystick.init()
        while True: 
            data = {}
            for event_ in pygame.event.get():
                # 按键按下或弹起事件
                if event_.type == pygame.JOYBUTTONDOWN or event_.type == pygame.JOYBUTTONUP:
                    buttons = joystick.get_numbuttons()
                    # 获取所有按键状态信息
                    data['type'] = 'JOYBUTTONDOWN'
                    data['button'] = -1
                    for i in range(buttons):
                        button = joystick.get_button(i)
                        # print("button " + str(i) +": " + str(button))
                        if(button==1):
                            data['button'] = i
                        '''
                            index   A--0
                                    B--1
                                    X--2
                                    Y--3
                                    L1--4
                                    R1--5
                                    select--6
                                    start--7
                                    mode--8
                        '''
                        # data['type'] = 'JOYBUTTONDOWN'
                        # data['button'] = button
                        # data['value'] = i
                # 轴转动事件
                elif event_.type == pygame.JOYAXISMOTION:
                    axes = joystick.get_numaxes()
                    # 获取所有轴状态信息
                    axis_list = []
                    for i in range(axes):
                        axis = joystick.get_axis(i)
                        axis_list.append(axis)
                    print(axis_list)
                    data['type'] = 'JOYAXISMOTION'
                    data['value'] = axis_list
                    # 左摇杆 0,1 右摇杆3，4  
                    print("---------------------------------------------------------")
                # 方向键改变事件
                elif event_.type == pygame.JOYHATMOTION:
                    hats = joystick.get_numhats()
                    # 获取所有方向键状态信息
                    for i in range(hats):
                        hat = joystick.get_hat(i)
                        print ("---------:",hat)
                        # if ( (not hat[0]==0) and (not hat[1]==0)):
                        # print("hat -if " + str(i) +": " + str(hat))
                        data['type'] = 'JOYHATMOTION'
                        data['value'] = hat
                        # else:
                            # print("hat -else" + str(i) +": " + str(hat))
                print(data)
                # message = json.dumps(data)
                # command_publisher(message)

def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = WriterNode("xbox")  # 新建一个节点
    # node.joy()
    # rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    # rclpy.shutdown() # 关闭rclpy

   
