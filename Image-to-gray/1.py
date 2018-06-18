import cv2 #Importing OpenCV
import numpy as np
import matplotlib.pyplot as plt # Importing the necessary libraries

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE) #To read an image from the directory of python as grayscale

cv2.imshow('image', img) #Displaying the image using cv2

plt.imshow(img, cmap = 'gray', interpolation ='bicubic') # Displaying the image using matplotlib.pyplot
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows() #Destroys all Windows opened by OpenCV 
