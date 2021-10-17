import cv2 as cv 
import numpy as np


def main():
    blank_image = np.zeros((500, 500), dtype="uint8")

    cv.rectangle(blank_image, (0, 0), (150, 200), (255, 255, 255), thickness=5)
    cv.circle(blank_image, (0, 500), 200, (255, 255, 255), thickness=-1)
    cv.line(blank_image, (0, 500), (500, 0), (255, 255, 255), thickness=5)

    triangle = np.array([[[350, 130], [380, 230], [190, 280]]], np.int32)
    cv.polylines(blank_image, [triangle], True, (255,255,255), thickness=8)
    cv.imshow("Cirlce", blank_image)

    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("output.jpg", blank_image)


if __name__ == "__main__":
    main()