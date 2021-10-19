import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('input.jpeg')

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 5))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
axs[0].set_title('Original Image')

# Create our shapening kernel, we don't normalize since the 
# the values in the matrix sum to 1
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])

# applying different kernels to the input image
sharpened = cv2.filter2D(image, -1, kernel_sharpening)

axs[1].imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
axs[1].set_title('Image Sharpening')
cv2.imwrite('sharpen_image.jpg', sharpened)

plt.show()
