import cv2
import numpy as np# Importing the necessary libraries
 
cap = cv2.VideoCapture(0) 
 
panel = np.zeros([100, 700], np.uint8)
cv2.namedWindow('panel') # A named windoiw for the panel
 
def nothing(x):
    pass
 
cv2.createTrackbar('L - h', 'panel', 0, 179, nothing)
cv2.createTrackbar('U - h', 'panel', 179, 179, nothing)# Creating Trackbars for H, S, V values 
 
cv2.createTrackbar('L - s', 'panel', 0, 255, nothing)
cv2.createTrackbar('U - s', 'panel', 255, 255, nothing)# Creating Trackbars for H, S, V values 
 
cv2.createTrackbar('L - v', 'panel', 0, 255, nothing)
cv2.createTrackbar('U - v', 'panel', 255, 255, nothing)# Creating Trackbars for H, S, V values 
 
cv2.createTrackbar('S ROWS', 'panel', 0, 480, nothing)
cv2.createTrackbar('E ROWS', 'panel', 480, 480, nothing)
cv2.createTrackbar('S COL', 'panel', 0, 640, nothing)
cv2.createTrackbar('E COL', 'panel', 640, 640, nothing) # Creating Trackbars to adjust the size of the window
 
 
 
while True:
    _, frame = cap.read()
 
    s_r = cv2.getTrackbarPos('S ROWS', 'panel')# Getting the values of the current location of the trackbar
    e_r = cv2.getTrackbarPos('E ROWS', 'panel')# Getting the values of the current location of the trackbar
    s_c = cv2.getTrackbarPos('S COL', 'panel')# Getting the values of the current location of the trackbar
    e_c = cv2.getTrackbarPos('E COL', 'panel')# Getting the values of the current location of the trackbar
 
    roi = frame[s_r: e_r, s_c: e_c]
 
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
 
    l_h = cv2.getTrackbarPos('L - h', 'panel')# Getting the values of the current location of the trackbar
    u_h = cv2.getTrackbarPos('U - h', 'panel')# Getting the values of the current location of the trackbar
    l_s = cv2.getTrackbarPos('L - s', 'panel')# Getting the values of the current location of the trackbar
    u_s = cv2.getTrackbarPos('U - s', 'panel')# Getting the values of the current location of the trackbar
    l_v = cv2.getTrackbarPos('L - v', 'panel')# Getting the values of the current location of the trackbar
    u_v = cv2.getTrackbarPos('U - v', 'panel')# Getting the values of the current location of the trackbar
 
    lower_green = np.array([l_h, l_s, l_v])#Applying the trackbar values
    upper_green = np.array([u_h, u_s, u_v])
 
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)
 
    bg = cv2.bitwise_and(roi, roi, mask=mask)
    fg = cv2.bitwise_and(roi, roi, mask=mask_inv)# Masking the values
 
    cv2.imshow('bg', cv2.medianBlur(bg, 15))
    cv2.imshow('fg', fg)# Displaying the frame
 
    cv2.imshow('panel', panel)
 
    k = cv2.waitKey(30) & 0xFF
    if k == 27: # Pressing ESC closes the tab
        break
 
cap.release()
cv2.destroyAllWindows()
