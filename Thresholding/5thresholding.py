import cv2
import numpy as np#Import the librairies

img = cv2.imread('bookpage.jpg')#Load the image
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) #Apply a threshold

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#Grayscaling
retval2, threshold2 = cv2.threshold(grayscaled, 8, 255, cv2.THRESH_BINARY)#Applying the threshold on grayscale

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) # A different type of threshold

cv2.imshow('original', img)
#cv2.imshow('threshold', threshold)
#cv2.imshow('threshold2', threshold2)
cv2.imshow('threshold', gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
