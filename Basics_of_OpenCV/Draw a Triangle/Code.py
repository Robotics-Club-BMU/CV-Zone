# Python code to draw a triangle and find centroid

# importing libraries
import numpy as np
import cv2

# Width and height of the black window
width = 400
height = 300

# Create a black window of 400 x 300
img = np.zeros((height, width, 3), np.uint8)

# Three vertices(tuples) of the triangle
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

# Drawing the triangle with the help of lines
#  on the black window With given points
# cv2.line is the inbuilt function in opencv library
cv2.line(img, p1, p2, (255, 0, 0), 3)
cv2.line(img, p2, p3, (255, 0, 0), 3)
cv2.line(img, p1, p3, (255, 0, 0), 3)

# finding centroid using the following formula
# (X, Y) = (x1 + x2 + x3//3, y1 + y2 + y3//3)
centroid = ((p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3)

# Drawing the centroid on the window
cv2.circle(img, centroid, 4, (0, 255, 0))

# image is the title of the window
cv2.imshow("image", img)
cv2.waitKey(0)
