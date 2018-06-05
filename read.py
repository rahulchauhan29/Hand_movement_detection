#importing required modules
import cv2
from collections import deque
import numpy as np

#capturing frames from camera
frame=cv2.VideoCapture(0)

#defining range for required colour(these valus can be edited for the required colour)
pts=deque(maxlen=50)

Lower_green=np.array([50,100,100])
Upper_green=np.array([70,255,255])
