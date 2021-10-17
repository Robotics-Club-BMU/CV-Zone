import cv2 as cv


def display_large_images(image, width=1200):
    #display larger images!
    scale = width/image.shape[1]
    dimensions = (int(image.shape[1]*scale), int(image.shape[0]*scale))
    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)


def main():             
    file = "./cat_large.jpg"
    image = cv.imread(file)
    if image.shape[1] >= 1800:
        image = display_large_images(image)
    cv.imshow("Cat", image)
    cv.waitKey(0)


if __name__ == "__main__":
    main()
