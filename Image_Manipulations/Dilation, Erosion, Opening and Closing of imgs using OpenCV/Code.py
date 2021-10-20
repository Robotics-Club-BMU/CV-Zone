# Python program to demonstrate erosion ,dilation ,open & closing of image using Open CV

import cv2
import numpy as np
 
# Reading the input image
img = cv2.imread(r'C:\Users\Dell\Pictures\Screenshots\monkey.png', 0)
 
# Taking a matrix of size 5 as the kernel
kernel = np.ones((5,5), np.uint8)
 
# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('Input', img)
cv2.imshow('Dilation', img_dilation)
cv2.imshow('Erosion', img_erosion)

cv2.waitKey(0)

#Program for opening image

import cv2
import numpy as np

image = cv2.imread(r'C:\Users\Dell\Pictures\Screenshots\boyimg.png', 0)
kernel = np.ones((5,5), np.uint8)

image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', image)

#Program for closing image

import cv2
import numpy as np
image = cv2.imread(r'C:\Users\Dell\Pictures\Screenshots\boyimg.png', 0)
kernel = np.ones((5,5), np.uint8)
image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', image)
