# 导入库
from launch import LaunchDescription
from launch_ros.actions import Node

# 定义函数名称为：generate_launch_description
def generate_launch_description():
    # 创建Actions.Node对象li_node，标明李四所在位置
    topic_publisher_02 = Node(
        package="example_topic_rclpy",
        executable="topic_publisher_02"
        )
    # 创建Actions.Node对象wang2_node，标明王二所在位置
    topic_subscribe_02 = Node(
        package="example_topic_rclpy",
        executable="topic_subscribe_02"
        )
    # 创建LaunchDescription对象launch_description,用于描述launch文件
    launch_description = LaunchDescription([topic_subscribe_02,topic_publisher_02])
    # 返回让ROS2根据launch描述执行节点
    return launch_description
    
