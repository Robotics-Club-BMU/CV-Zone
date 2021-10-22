# Python program to transform an image using
# threshold.
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Image operation using thresholding
img = cv2.imread('coins.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255,
                            cv2.THRESH_BINARY_INV +
                            cv2.THRESH_OTSU)
cv2.imshow('image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
