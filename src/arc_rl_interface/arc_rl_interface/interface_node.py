import rclpy
from rclpy.node import Node

class InterfaceNode(Node):
    def __init__(self):
        super().__init__('interface_node')
        self.get_logger().info('InterfaceNode has started.')

def main(args=None):
    rclpy.init(args=args)
    node = InterfaceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
