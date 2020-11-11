import cv2
import numpy as np


# Basic Initialization 

def empty(a):
    pass

kernel = np.ones((5,5),np.uint8)

frame_height = 640
frame_width = 480
cap =cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)
cap.set(10,150)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]
colorIndex = 0


#Making Trackbar window and trackbars

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 560,320)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)


#Creating Paint Window

paintWin = np.zeros([480,640,3]) + 255
paintWin = cv2.rectangle(paintWin, (30,1), (120,65), (0,0,0) , 0 )
paintWin = cv2.rectangle(paintWin, (160,1) , (255,65) , colors[0], -1)
paintWin = cv2.rectangle(paintWin, (280,1) , (370,65) , colors[1], -1)
paintWin = cv2.rectangle(paintWin, (400,1) , (485,65) , colors[2], -1)
paintWin = cv2.rectangle(paintWin, (520,1) , (600,65) , colors[3], -1)

cv2.putText(paintWin, "CLEAR",(58,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(paintWin, "BLUE",(187,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(paintWin, "GREEN",(295,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(paintWin, "RED",(415,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(paintWin, "BLACK",(530,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)


# Main Video Capturing 

while True:
    success,img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # Getting Trackbar Positions for creating a mask

    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
    v_min = cv2.getTrackbarPos("Val Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
    v_max = cv2.getTrackbarPos("Val Max","Trackbars")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])


    # Shows color Options in Video Outputed by Webcam 

    img = cv2.rectangle(img, (30,1), (120,65), (0,0,0) , 0 )
    img = cv2.rectangle(img, (160,1) , (255,65) , colors[0], -1)
    img = cv2.rectangle(img, (280,1) , (370,65) , colors[1], -1)
    img = cv2.rectangle(img, (400,1) , (485,65) , colors[2], -1)
    img = cv2.rectangle(img, (520,1) , (600,65) , colors[3], -1)

    cv2.putText(img, "CLEAR",(58,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, "BLUE",(187,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, "GREEN",(295,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, "RED",(415,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, "BLACK",(530,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)


    # Making A mask and dilating and eroding to remove impurities.  

    mask = cv2.inRange(imgHSV,lower,upper)
    mask = cv2.erode(mask,kernel,iterations=1)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask = cv2.dilate(mask,kernel,iterations=1)


    


    cv2.imshow("Air Canvas",img)
    #cv2.imshow("Mask",mask)
    cv2.imshow("Paint", paintWin)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

