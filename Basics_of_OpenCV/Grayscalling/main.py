import cv2 as cv


def main():             
    file = "./park.jpg"
    image = cv.imread(file)

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    cv.imshow("Original Image", image)
    cv.imshow("Converted Image", gray)
    
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
