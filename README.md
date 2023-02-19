conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ <br>
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/<br>
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/<br>
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/<br>
conda config --set show_channel_urls yes<br>

## 1.ROS2 
    wget http://fishros.com/install -O fishros && . fishros <br>
## 2.colcon 
    sudo apt-get install python3-colcon-common-extensions <br>
    colcon build




## 3.run build
    cd machine <br>
    colcon build<br>
## 4.source环境
    source install/setup.bash
## run test
**run folder:**
    ros2 run xbox xbox_node
    ros2 run electrical wheel_node


## lauanch
    ros2 launch <package_name> <launch_file_name>
    ros2 launch xbox xbox.launch.py
