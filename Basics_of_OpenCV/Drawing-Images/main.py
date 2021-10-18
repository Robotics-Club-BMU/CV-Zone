import cv2 as cv 
import numpy as np


def main():
    blank_image = np.zeros((500, 500), dtype="uint8")
    cv.rectangle(blank_image, (0, 0), (150, 200), (255, 255, 255), thickness=5)
    cv.imshow("Rectangle", blank_image)
    cv.imwrite("rectangle.jpg", blank_image)

    blank_image = np.zeros((500, 500), dtype="uint8")
    cv.circle(blank_image, (0, 500), 200, (255, 255, 255), thickness=-1)
    cv.imshow("Circle", blank_image)
    cv.imwrite("circle.jpg", blank_image)

    blank_image = np.zeros((500, 500), dtype="uint8")
    cv.line(blank_image, (0, 500), (500, 0), (255, 255, 255), thickness=5)
    cv.imshow("Line", blank_image)
    cv.imwrite("line.jpg", blank_image)

    triangle = np.array([[[350, 130], [380, 230], [190, 280]]], np.int32)
    blank_image = np.zeros((500, 500), dtype="uint8")
    cv.polylines(blank_image, [triangle], True, (255,255,255), thickness=8)
    cv.imshow("Polygon", blank_image)
    cv.imwrite("polygon.jpg", blank_image)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()