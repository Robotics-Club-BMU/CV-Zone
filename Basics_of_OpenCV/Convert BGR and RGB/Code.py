import cv2

image = cv2.imread("input_bgr.jpeg")

# converting BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

## vice versa
image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

cv2.imshow('image', image_rgb)
cv2.imshow('image', image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
