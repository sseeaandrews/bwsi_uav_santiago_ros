import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/santiago/bwsi_uav_santiago_ros/ros2_ws/install/my_robot_controller'
