#!/usr/bin/env python3
import rospy
from ultralytics import YOLO
import supervision as sv
import cv2
from PIL import Image
from yolov8_pkg.msg import BoundingBox


if __name__ == '__main__':

	model = YOLO("Projects/rosnano/src/yolov8_pkg/models/yolov8n.pt")
	
	rospy.init_node('webcam')
	
	bounding_box_pub = rospy.Publisher("bounding_boxes", BoundingBox, queue_size=10)
	
	cap = cv2.VideoCapture(0)
	
	ret, img = cap.read()

	while ret:
		ret, img = cap.read()
		if ret:

			img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

			result = model(source = img)

			detections = sv.Detections.from_yolov8(result[0])

			for bbox, _, conf, class_id, tracker_id in detections:

				det_class = model.model.names[class_id]
				x1,y1,x2,y2 = bbox
				
				msg = BoundingBox()
				
				msg.class_label = det_class
				msg.box_coordinates = (int(x1),int(y1),int(x2),int(y2))
				
				bounding_box_pub.publish(msg)

