import cv2
import numpy as np
img = cv2.imread('diary.jpg')

blur = cv2.medianBlur(img, 15) # Step 1 is to blur out any type of Salt-pepper noise
edge = cv2.Canny(blur, 100, 200) # Find the edges using Canny Edge Detection

screen_res = [1280, 720]
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale) # Resizing the screen according the dimensions of the image

kernel = np.ones((5,5), np.uint8) 
imgd = cv2.dilate(edge, kernel, iterations=1) # Using dilation to thicken the edges

cv2.namedWindow('Edge', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Edge', window_width, window_height)
cv2.imshow('Edge', imgd)
