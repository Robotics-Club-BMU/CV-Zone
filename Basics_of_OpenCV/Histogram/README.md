

# Image-Histogram

Histogram of an image, like other histograms also shows frequency. But an image histogram, shows frequency of pixels intensity values. In an image histogram, the x axis shows the gray level intensities and the y axis shows the frequency of these intensities.

## Libraries

```
 import cv2
```

```
 from matplotlib import pyplot as plt
```
```
 from pylab import imshow
```

## Importing file from local PC

I imported image from my PC you can also use any link with image for this purpose.

```
img = cv2.imread('C:/Users/ayush/Desktop/image.jpg',0)
```
## Image Preview

```
imshow (img)
```



![git](https://user-images.githubusercontent.com/90252937/137700571-61010797-5e2e-4cde-8b3d-da273399f00c.jpeg)

## Ploting Histogram

```
histg = cv2.calcHist([img],[0],None,[256],[0,256]) 
```

```
plt.plot(histg)
plt.show()
```

![histo](https://user-images.githubusercontent.com/90252937/137701219-357225fc-3c14-4024-adc7-a3373543984b.jpeg)




  