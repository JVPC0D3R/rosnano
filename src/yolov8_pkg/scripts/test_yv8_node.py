#!/usr/bin/env python3
import rospy
from ultralytics import YOLO
#from webcam_package.msg import BoundingBox


if __name__ == '__main__':

	model = YOLO("Projects/rosnano/src/yolov8_pkg/models/yolov8n.pt")

	model(source = 0, show = True)


