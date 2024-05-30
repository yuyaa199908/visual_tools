import rclpy
from rclpy.node import Node
# msgs
from sensor_msgs.msg import Image

# add
import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
import sys

from cv_bridge import CvBridge

class Depth2Color(Node):
    def __init__(self):
        super().__init__('depth2color')
        self.sub_image = self.create_subscription(
                            Image(), 
                            '/camera/depth/image_rect_raw', 
                            self.CB_masking,
                            10)
        self.pub_image =  self.create_publisher(Image, '/depth_with_color', 10)

    def CB_masking(self, msg):
        img_np = CvBridge().imgmsg_to_cv2(msg)

        depth_array = np.array(img_np, dtype=np.uint16)
        depth_normalized = cv2.normalize(depth_array, None, 0, 255, cv2.NORM_MINMAX) 
        depth_normalized = np.uint8(depth_normalized)
        depth_colormap = cv2.applyColorMap(depth_normalized, cv2.COLORMAP_VIRIDIS)#cv2.COLORMAP_JET
        msg_out = CvBridge().cv2_to_imgmsg(depth_colormap, encoding="bgr8")
        self.pub_image.publish(msg_out)

def main():
    rclpy.init()
    node = Depth2Color()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()