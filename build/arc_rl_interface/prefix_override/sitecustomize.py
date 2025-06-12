import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aaron/arc_rl_interface_ros2/install/arc_rl_interface'
