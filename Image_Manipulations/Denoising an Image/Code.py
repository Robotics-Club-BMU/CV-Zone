# Denoising an Image

import cv2
from matplotlib import pyplot as plt

image = cv2.imread('input.png')

median = cv2.medianBlur(image,5)

# plt.subplot(121), plt.title('Input Image'),  plt.imshow(image)
# plt.subplot(122), plt.title('Output Image'), plt.imshow(median)
#
# plt.show()

cv2.imshow('Median',median)
cv2.waitKey(0)
cv2.destroyAllWindows()

