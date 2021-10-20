import cv2 as cv
import numpy as np


def main():
    image = cv.imread("park.jpg")
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # Grayscale!
    edged = cv.Canny(gray, 30, 200)  # find canny edges

    contours, hierarchy = cv.findContours(
        edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.imshow('Canny Edges After Contouring', edged)
    cv.imwrite("contours_canny.jpg", edged)

    print(f"Number of Contours found = {str(len(contours))}")

    cv.drawContours(image, contours, -1, (0, 255, 0), 3)
    cv.imshow('Contours', image)
    cv.imwrite("contours.jpg", image)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
