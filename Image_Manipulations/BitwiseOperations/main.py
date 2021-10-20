import numpy as np
import cv2 as cv

image_1 = np.zeros((500, 500), dtype="uint8")
cv.rectangle(image_1, (100, 100), (300, 300), 255, -1)
cv.imshow("Image_1", image_1)


image_2 = np.zeros((500, 500), dtype="uint8")
cv.circle(image_2, (150, 150), 90, 255, -1)
cv.imshow("Image_2", image_2)


bit_and = cv.bitwise_and(image_1, image_2)
cv.imshow("Bitwise And", bit_and)
cv.imwrite("bit_and.jpg", bit_and)

bit_or = cv.bitwise_or(image_1, image_2)
cv.imshow("Bitwise Or", bit_or)
cv.imwrite("bit_or.jpg", bit_or)

bit_not = cv.bitwise_not(image_1)
cv.imshow("Bitwsie Not of Image_1", bit_not)
cv.imwrite("bit_not.jpg", bit_not)

bit_xor = cv.bitwise_xor(image_1, image_2)
cv.imshow("Bitwise XOR", bit_xor)
cv.imwrite("bit_xor.jpg", bit_and)


cv.waitKey(0)
cv.destroyAllWindows()
