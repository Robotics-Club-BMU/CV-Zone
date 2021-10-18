
# **Open CV - computer vision, machine learning, image processing & much more**

*[OpenCV](https://www.geeksforgeeks.org/opencv-overview/) (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.*

![open cv](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6gUKfO1PB6g3Y6KQZuOd1GOBbYCHli6tUuw&usqp=CAU)

The library has more than 2500 optimized algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms. These algorithms can be used to detect and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving objects, extract 3D models of objects, produce 3D point clouds from stereo cameras, stitch images together to produce a high resolution image of an entire scene, find similar images from an image database, remove red eyes from images taken using flash, follow eye movements, recognize scenery and establish markers to overlay it with augmented reality, etc. OpenCV has more than 47 thousand people of user community and estimated number of downloads exceeding 18 million. The library is used extensively in companies, research groups and by governmental bodies.

## *Computer Vision*

Computer vision is a process by which we can understand the images and videos how they are stored and how we can manipulate and retrieve data from them. Computer Vision is the base or mostly used for Artificial Intelligence. Computer-Vision is playing a major role in self-driving cars, robotics as well as in photo correction apps. 

The first OpenCV version was 1.0. OpenCV is released under a BSD license and hence it’s free for both academic and commercial use. It has C++, C, Python and Java interfaces and supports Windows, Linux, Mac OS, iOS and Android. When OpenCV was designed the main focus was real-time applications for computational efficiency. All things are written in optimized C/C++ to take advantage of multi-core processing. 

Look at the following images :

![pic1](https://media.geeksforgeeks.org/wp-content/uploads/20190629122733/main1.jpg)

![pic2](https://media.geeksforgeeks.org/wp-content/uploads/20190629123027/information.jpg)

from the above original image, lots of pieces of information that are present in the original image can be obtained. Like in the above image there are two faces available and the person(I) in the images wearing a bracelet, watch, etc so by the help of OpenCV we can get all these types of information from the original image. 
It’s the basic introduction to OpenCV we can continue the Applications and all the things in our upcoming articles. 

**Applications of OpenCV :** There are lots of applications which are solved using OpenCV, some of them are listed below 
 
- face recognition
- Automated inspection and surveillance
- number of people – count (foot traffic in a mall, etc)
- Vehicle counting on highways along with their speeds
- Interactive art installations
- Anamoly (defect) detection in the manufacturing process (the odd defective products)
- Street view image stitching
- Video/image search and retrieval
- Robot and driver-less car navigation and control
- object recognition
- Medical image analysis
- Movies – 3D structure from motion
- TV Channels advertisement recognition

**OpenCV Functionality**
- Image/video I/O, processing, display (core, imgproc, highgui)
- Object/feature detection (objdetect, features2d, nonfree)
- Geometry-based monocular or stereo computer vision (calib3d, stitching, videostab)
- Computational photography (photo, video, superres)
- Machine learning & clustering (ml, flann)
- CUDA acceleration (gpu)

## **Image-Processing** 

Image processing is a method to perform some operations on an image, in order to get an enhanced image and or to extract some useful information from it. 
If we talk about the basic definition of image processing then **“Image processing is the analysis and manipulation of a digitized image, especially in order to improve its quality”.**

**Digital-Image :**

An image may be defined as a two-dimensional function f(x, y), where x and y are spatial(plane) coordinates, and the amplitude of fat any pair of coordinates (x, y) is called the intensity or grey level of the image at that point. 
In another word An image is nothing more than a two-dimensional matrix (3-D in case of coloured images) which is defined by the mathematical function f(x, y) at any point is giving the pixel value at that point of an image, the pixel value describes how bright that pixel is, and what colour it should be. 
Image processing is basically signal processing in which input is an image and output is image or characteristics according to requirement associated with that image.

**Image processing basically includes the following three steps:**

1. Importing the image
2. Analysing and manipulating the image
3. Output in which result can be altered image or   report that is based on image analysis

### **How Does A Computer Read An Image?** 
![pic 3](data:image/jpeg;base64,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)

We are humans we can easily make it out that is the image of a person who is me. But if we ask computer “is it my photo?”. The computer can’t say anything because the computer is not figuring out it all on its own. 
The computer reads any image as a range of values between 0 and 255. For any color image, there are 3 primary channels -red, green and blue.

# OPEN -CV & PYTHON 
### *Open -CV & python ,can be used for creating many interactive projects for an expert as well as for beginners,because of its user-friendliness:*

# Here are some projects using OPEN CV & Python:

## Resizing image using open CV

Usually when working on images,we often need to resize the images according to certain requirements.Mostly you will do such operation in Machine learning and deep learning as it reduces the time of training of a neural network. As the number of pixels in an image increases, the more is the number of input nodes that in turn increases the complexity of the model. We use an inbuilt resize() method to resize an image.

Syntax: cv2.resize(s, size,fx,fy,interpolation)

## Parameters:

s - input image (required).

size - desired size for the output image after resizing (required)

fx - Scale factor along the horizontal axis.(optional)

fy - Scale factor along the vertical axis.

Interpolation(optional) - This flag uses following methods:
 
 **INTER_NEAREST** – a nearest-neighbor interpolation
 
 **INTER_LINEAR** – a bilinear interpolation (used by default) 
 
 **INTER_AREA** – resampling using pixel area relation. It may be a preferred method for    image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
 
 **INTER_CUBIC** – a bicubic interpolation over 4×4 pixel neighborhood 
 
 **INTER_LANCZOS4** – a Lanczos interpolation over 8×8 pixel neighborhood

Here is an example of how we can use this method:

import cv2

import numpy as np
 
#### #importing the opencv module  
import cv2  
#### #using imread('path') and 1 denotes read as  color image  
img = cv2.imread('dog.jpg',1)  
print(img.shape)
img_resized=cv2.resize(img, (780, 540),  
               interpolation = cv2.INTER_NEAREST) 
cv2.imshow("Resized",img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
![img 1](https://d1m75rqqgidzqn.cloudfront.net/wp-data/2020/11/20184424/dog.jpg)

original

![img 2](https://d1m75rqqgidzqn.cloudfront.net/wp-data/2020/11/20184435/q1.png)
Resized

# OpenCV Drawing Functions

*We may require to draw certain shapes on an image such as circle, rectangle, ellipse, polylines, convex, etc. and we can easily do this using OpenCV.It is often used when we want to highlight any object in the input image for example in case of face detection,we might want to highlight the face with a rectangle.Here we will learn about the drawing functions such as circle,rectangle,lines,polylines and also see how to write text on an image.*

## Drawing circle:

We use the method to circle to draw a circle in an image.Here is the syntax and parameters:

**Syntax:** 

cv2.circle(image, center_coordinates, radius, color, thickness)
### Parameters: 
image: It is the input image on which a circle is to be drawn. 

center_coordinates: It is the center coordinates of the circle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value). 

radius: It is the radius of the circle. 

color: It is the color of the border line of the circle to be drawn. We can pass a tuple For in BGR,  eg: (255, 0, 0) for blue color. 

thickness: It is the thickness of the circle border line in px. Thickness of -1 px will fill the circle shape by the specified color.

Return Value: It returns an image.

*import numpy as np  
import cv2  
img = cv2.imread(r'C:\Users\Mirza\dog.jpeg', 1)  
cv2.circle(img,(80,80), 55, (255,0,0), -1)  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()*

## Drawing rectangle:

In a similar we can draw a rectangle.Here is the the syntax for this function:

 **Syntax:** 
 
 cv2.rectangle(image, start_point, end_point, color, thickness)

### Parameters:

- image: It is the input image on which rectangle is to be drawn.
- start_point: It is the starting coordinates(top left vertex) of the rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
- end_point: It is the ending coordinates(bottom right) of the rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
- color: It is the color of the border line of the rectangle to be drawn. We can pass a tuple For in BGR,  eg: (255, 0, 0) for blue color. 
- thickness: It is the thickness of the rectangle border line in px. Thickness of -1 px will fill the rectangle shape by the specified color.
- Return Value: It returns an image.

Here is an example of this function:

import numpy as np  
import cv2  
img = cv2.imread(r'C:\Users\Mirza\dog.jpeg', 1)  
cv2.rectangle(img,(15,25),(200,150),(0,255,255),15)  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()

## Write text on an image

We can write text on the image by using the putText() method. The syntax is given below.

 **Syntax**

 cv2.putText(img, text, org, font,fontScale color)  
### Parameters:
img: It represents the input image on which we have to write text

text: The text which we want to write on the image.

org: It denotes the Bottom-left corner of the text string on the image.So it is used to set the location of text on the image

font: the font of text.Here is the list of supported fonts.

fontScale: The scale of the font by which you can increase or decrease size

color: Represents the color. We can pass a tuple For in BGR,  eg: (255, 0, 0) for blue color. 

 
Here is an example:

import numpy as np  
import cv2  
font = cv2.FONT_HERSHEY_SIMPLEX  
mg = cv2.imread(r'C:\Users\Mirza\dog.jpeg', 1)  
cv2.putText(img,'Dog',(10,500), font, 1,(255,255,255),2)  
#### #Display the image  
cv2.imshow("image",img)  
cv2.waitKey(0) 


#  ***Canny Edge Detection*** 

Edge detection is an image processing technique used for finding the boundaries of objects within images.Here we will use a popular edge detection algorithm Canny Edge Detection, developed by John F. Canny.In OpenCV, we have Canny() method to implement this algorithm.Here is the syntax:

edges = cv2.Canny(img, minVal, maxVal, apertureSize, L2gradient)  

Parameters-

img: input image whose edges we want to detect.

minVal: Minimum intensity gradient (required)

maxVal: Maximum intensity gradient (required)

L2gradient: is a flag with default value =False, indicating the default L1 norm is enough to calculate the image gradient magnitude,If its is set as True a more accurate L2 norm is used to calculate the image gradient magnitude but it is computationally more expensive.

aperture: aperture size for the Sobel operator.

As we can see we have two threshold values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges.also those edges with intensity gradient less than minVal are sure to be non-edges and are discarded. The edges which lie between these two thresholds are classified edges or non-edges based on their connectivity with the ‘sure edges’. If they are connected to “sure-edge” pixels, they are considered to be part of edges. Otherwise, they are also discarded as non-edges.

### Here is an example:

import cv2

img = cv2.imread('dog.jpg')

edges = cv2.Canny(img,200,300,True)

cv2.imshow("Edge Detected Image", edges)  

cv2.imshow("Original Image", img)  

cv2.waitKey(0)  # waits until a key is pressed  

cv2.destroyAllWindows()  # destroys the window showing image

![image 1](https://d1m75rqqgidzqn.cloudfront.net/wp-data/2020/11/30232844/edge.png)
Original img ................................ Edge Detected Image

Thus , these are some of the projects that we can do using OPEN -CV. Apart from these, OPEN-CV can be used in many other fields, like Machine - Learning, AI , etc.
Apart from python, OPEN -CV  can  also be combined with other languages like C, C++, Java, etc, to produce many more interactive apps & innovations.


### Photo and Content Credits :
https://www.mygreatlearning.com/blog/opencv-tutorial-in-python/

https://opencv.org/about/

