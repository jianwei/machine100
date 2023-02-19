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
        self.command_publisher_ = self.create_publisher(String,"command", 10) 
        self.joy()
        

    
    def joy(self):
        pygame.init()
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
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
                # 方向键改变事件
                elif event_.type == pygame.JOYHATMOTION:
                    hats = joystick.get_numhats()
                    # 获取所有方向键状态信息
                    for i in range(hats):
                        hat = joystick.get_hat(i)
                        data['type'] = 'JOYHATMOTION'
                        data['value'] = hat

                print(data)
                msg = String()
                msg.data = json.dumps(data)
                self.command_publisher_.publish(msg) 
                # self.get_logger().info(f'发布了指令：{msg.data}')    #打印一下发布的数据

def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    WriterNode("xbox")  # 新建一个节点


   
