#importing required modules
import cv2
from collections import deque
import numpy as np

#capturing frames from camera
frame=cv2.VideoCapture(0)

#defining range for required colour(these valus can be edited for the required colour)
pts=deque(maxlen=50)

#HSV for RED color have two ranges
Lower_red=np.array([0,100,100])
Upper_red=np.array([10,255,255])
Lower_red1=np.array([160,100,100])
Upper_red1=np.array([179,255,255])

while True:
    ret, img=frame.read()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    kernel=np.ones((5,5),np.uint8)
    mask1=cv2.inRange(hsv,Lower_green,Upper_green)
    mask2=cv2.inRange(hsv,Lower_green1,Upper_green1)
    mask=mask1+mask2
    mask=cv2.erode(mask,kernel,iterations=2)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask=cv2.dilate(mask,kernel,iterations=1)
    res=cv2.bitwise_and(img,img,mask=mask)
    cnts,heir=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    center=None
    
    #---remaining code goes here---
    
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    cv2.imshow("Frame",img)

    k=cv2.waitKey(30) & 0xFF
    if k==27: #Press"Esc" key to exit
        break
        
#release videocapture object
frame.release()
#destroy all windows
cv2.destroyAllWindows()        
