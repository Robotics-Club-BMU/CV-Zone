import cv2 as cv 


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w/2, h/2)
    
    M = cv.getRotationMatrix2D(center, angle, scale)
    rotated = cv.warpAffine(image, M, (w, h))
    return rotated


def main():
    image = cv.imread("park.jpg")

    cv.imshow("Orignal Image", image)
    
    rotated_1 = rotate(image, 90)
    cv.imshow("Rotated Image by 90 degrees", rotated_1)

    rotated_2 = rotate(image, 47)
    cv.imshow("Rotated Image by 47 degrees", rotated_2)

    rotated_3 = rotate(image, 120)
    cv.imshow("Rotated Image by 120 degrees", rotated_3)

    rotated_4 = rotate(image, 60)
    cv.imshow("Rotated Image by 60 degrees", rotated_4)

    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("rotated_1.jpg", rotated_1)
    cv.imwrite("rotated_2.jpg", rotated_2)
    cv.imwrite("rotated_3.jpg", rotated_3)
    cv.imwrite("rotated_4.jpg", rotated_4)

main()