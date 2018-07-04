import numpy as np
import cv2#Importing the necessary libraries

cap = cv2.VideoCapture(0) 
fgbg = cv2.createBackgroundSubtractorMOG2() # Creating an object for background subtraction

while(1):
    ret, frame = cap.read()                 # Reading in the live feed from webcam

    fgmask = fgbg.apply(frame)              # Applying the background subtracor
 
    cv2.imshow('fgmask',frame)              # Displaying the frame
    median = cv2.medianBlur(fgmask,15)      # Removing the salt pepper noise from video
    cv2.imshow('frame',fgmask)              # Displaying the background- subtracted video

    
    k = cv2.waitKey(30)
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()
