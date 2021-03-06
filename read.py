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
    mask1=cv2.inRange(hsv,Lower_red,Upper_red)
    mask2=cv2.inRange(hsv,Lower_red1,Upper_red1)
    mask=mask1+mask2
    mask=cv2.erode(mask,kernel,iterations=2)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask=cv2.dilate(mask,kernel,iterations=1)
    res=cv2.bitwise_and(img,img,mask=mask)
    cnts,heir=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    center=None
    
    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))

        if radius>5:
            cv2.circle(img,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(img,center,5,(0,0,255),-1)

    pts.appendleft(center)
    for i in xrange (1,len(pts)):
        if pts[i-1]is None or pts[i]is None:
            continue
        thick=int(np.sqrt(len(pts)/float(i+1))*2.5)
        cv2.line(img,pts[i-1],pts[i],(0,0,255),thick)
    
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
