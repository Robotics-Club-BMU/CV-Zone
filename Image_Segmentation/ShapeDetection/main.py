import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def main():
    image = cv.imread('input.jpg')
    # converting image into grayscale image
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


    # setting threshold of gray image
    _, threshold = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    # using a findContours() function
    contours, _ = cv.findContours(
        threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    i = 0
    # list for storing names of shapes
    for contour in contours:
        # here we are ignoring first counter because
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue

        # cv.approxPloyDP() function to approximate the shape
        approx = cv.approxPolyDP(
            contour, 0.01 * cv.arcLength(contour, True), True)

        # using drawContours() function
        cv.drawContours(image, [contour], 0, (0, 0, 255), 5)

        # finding center point of shape
        M = cv.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])

        # putting shape name at center of each shape
        if len(approx) == 3:
            cv.putText(image, 'Triangle', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        elif len(approx) == 4:
            cv.putText(image, 'Quadrilateral', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        elif len(approx) == 5:
            cv.putText(image, 'Pentagon', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        elif len(approx) == 6:
            cv.putText(image, 'Hexagon', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        else:
            cv.putText(image, 'circle', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # displaying the image after drawing contours
    cv.imshow('shapes', image)
    cv.imwrite('detected.png', image)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
