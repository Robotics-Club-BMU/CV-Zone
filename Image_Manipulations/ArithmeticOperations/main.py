import cv2 as cv
import numpy as np


def main():
    image_1 = np.zeros((500, 500), dtype="uint8")
    image_2 = np.zeros((500, 500), dtype="uint8")

    cv.rectangle(image_1, (100, 100), (450, 450),
                 (255, 255, 255), thickness=-1)
    cv.circle(image_2, (250, 250), 175, (255, 255, 255), thickness=-1)

    cv.imshow("Image_1", image_1)
    cv.imshow("Image_2", image_2)

    add = cv.add(image_1, image_2)
    sub = cv.subtract(image_1, image_2)

    cv.imshow("Add", add)
    cv.imshow("Subtract", sub)

    cv.imwrite("add.jpg", add)
    cv.imwrite("sub.jpg", sub)

    cv.waitKey(0)
    cv.destroyAllWindows()


main()
