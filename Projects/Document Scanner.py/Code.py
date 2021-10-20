# Document Scanner

import cv2
import numpy as np

"""A function used to sharpen the image and make it more clear"""
def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=2.0, threshold=1):
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


img = cv2.imread('document.jpg')  # Read Image
height, width, channels = img.shape  # Find Height And Width Of Image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # RGB To Gray Scale

kernel = np.ones((5, 5), np.uint8)  # Reduce Noise Of Image
erosion = cv2.erode(gray, kernel, iterations=1)
opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

edges = cv2.Canny(closing, 20, 240)  # Find Edges

# Get Threshold Of Canny
thresh = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Find Contours In Image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Find Biggest Contour
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
print(max_index)

# Find approxPoly Of Biggest Contour
epsilon = 0.1 * cv2.arcLength(contours[max_index], True)
approx = cv2.approxPolyDP(contours[max_index], epsilon, True)

# Crop The Image To approxPoly
pts1 = np.float32(approx)
pts = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts)
result = cv2.warpPerspective(img, matrix, (width, height))

flip = cv2.flip(result, 1)  # Flip Image
rotate = cv2.rotate(flip, cv2.ROTATE_90_COUNTERCLOCKWISE)  # Rotate Image

width = int(img.shape[1])
height = int(img.shape[0])
dim = (width, height)

# resize image
resized = cv2.resize(rotate, dim, interpolation=cv2.INTER_AREA)


kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
# kernel = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, 0]], np.float32)
# kernel = 1/3 * kernel
sharpened_image = cv2.filter2D(resized, -1, kernel)
# sharpened_image = unsharp_mask(resized)

alpha = 1.2 # Contrast control (1.0-3.0)
beta = 1.8 # Brightness control (0-100)

adjusted = cv2.convertScaleAbs(sharpened_image, alpha=alpha, beta=beta)


cv2.imshow('Result', adjusted)

cv2.waitKey(0)
cv2.destroyAllWindows()
