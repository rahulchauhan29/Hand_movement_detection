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
Lower_red1=np.array([0,100,100])
Upper_red1=np.array([10,255,255])

while True:
    ret, img=frame.read()
    #remaining code goes here
    
    cv2.imshow("Frame",img)

    k=cv2.waitKey(30) & 0xFF
    if k==27: #Press"Esc" key to exit
        break
        
#release videocapture object
frame.release()
#destroy all windows
cv2.destroyAllWindows()        
