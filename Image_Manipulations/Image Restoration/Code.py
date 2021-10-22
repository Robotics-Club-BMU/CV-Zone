import cv2
import numpy as np

# Taking Input
image = cv2.imread('damage.png')

# Load the mask.
mask = cv2.imread('mask.png', 0)
blur = cv2.GaussianBlur(mask, (7,7), cv2.BORDER_DEFAULT)

# Inpaint.
dst = cv2.inpaint(image, blur, 15, cv2.INPAINT_TELEA)

cv2.imshow("Restored", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
