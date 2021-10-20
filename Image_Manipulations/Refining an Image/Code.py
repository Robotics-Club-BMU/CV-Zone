# Refining an Image using Open CV

import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    image = cv2.imread('refine.jpg')
    # sharpened_image = unsharp_mask(image)
    # cv.imwrite('my-sharpened-image.jpg', sharpened_image)
    # cv2.imshow("refined", unsharp_mask(image))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # Plotting of source and destination image

    kernel = np.array([[-1, -1, -1],
                       [-1, 10, -1],
                       [-1, -1, -1]])
    image_sharp = cv2.filter2D(image, -1, kernel)

    plt.subplot(121), plt.title('Input Image'), plt.imshow(image)
    plt.subplot(122), plt.title('Refined Image'), plt.imshow(image_sharp)

    plt.show()

main()
