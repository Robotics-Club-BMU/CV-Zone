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
    
    rotated = rotate(image, 90)
    cv.imshow("Rotated Image by 90 degrees", rotated)

    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("rotated.jpg", rotated)

main()