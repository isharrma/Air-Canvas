import cv2
import numpy as np

frame_height = 640
frame_width = 480
cap =cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)
cap.set(10,150)

while True:
    success,img = cap.read()
    imgResult = img.copy()
    cv2.imshow("Air Canvas",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
