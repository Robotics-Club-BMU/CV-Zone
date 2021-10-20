import cv2
import numpy as np
src = cv2.imread("D:/Kriti Banka/threshold.png", cv2.IMREAD_GRAYSCALE)
ret, thresh1 = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold', thresh1)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
ret, thresh2 = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Binary Threshold Inverted', thresh2)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
ret, thresh3 = cv2.threshold(src, 120, 255, cv2.THRESH_TRUNC)
cv2.imshow('Truncated Threshold', thresh3)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
ret, thresh4 = cv2.threshold(src, 120, 255, cv2.THRESH_TOZERO)
cv2.imshow('Set to 0', thresh4)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
ret, thresh5 = cv2.threshold(src, 120, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('Set to 0 Inverted', thresh5)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
 