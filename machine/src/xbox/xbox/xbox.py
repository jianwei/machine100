#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import pygame

class WriterNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("this is %s" % name)
        self.joy()

    
    def joy(self):
        # 模块初始化
        pygame.init()
        pygame.joystick.init()
        # 若只连接了一个手柄，此处带入的参数一般都是0
        joystick = pygame.joystick.Joystick(0)
        # 手柄对象初始化
        joystick.init()

        while True: 
            for event_ in pygame.event.get():
                # 按键按下或弹起事件
                if event_.type == pygame.JOYBUTTONDOWN or event_.type == pygame.JOYBUTTONUP:
                    buttons = joystick.get_numbuttons()
                    # 获取所有按键状态信息
                    for i in range(buttons):
                        button = joystick.get_button(i)
                        if(button==1):
                            print("button " + str(i) +": " + str(button))
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
                        # print("axis " + str(i) +": " + str(axis))
                    print(axis_list)
                    # 左摇杆 0,1 右摇杆3，4  
                    print("---------------------------------------------------------")
                # 方向键改变事件
                elif event_.type == pygame.JOYHATMOTION:
                    hats = joystick.get_numhats()
                    # 获取所有方向键状态信息
                    for i in range(hats):
                        hat = joystick.get_hat(i)
                        if (hat!=(0,0)):
                            print("hat " + str(i) +": " + str(hat))
                            print(type(hat))


def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = WriterNode("xbox")  # 新建一个节点
    # node.joy()
    # rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    # rclpy.shutdown() # 关闭rclpy

   
