

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

# Reading, Writing and Displaying Images through OPEN -CV

Machines see and process everything using numbers, including images and text. How do you convert images to numbers – I can hear you wondering. Two words – pixel values:

![pic 3](https://cdn.analyticsvidhya.com/wp-content/uploads/2019/02/pixelExample.png)

Every number represents the pixel intensity at that particular location. In the above image, I have shown the pixel values for a grayscale image where every pixel contains only one value i.e. the intensity of the black color at that location.

Color images have multiple values for a single pixel. These values represent the intensity of respective channels – Red, Green and Blue channels for RGB images, for instance

Reading and writing images is essential to any computer vision project. And the OpenCV library makes this function a whole lot easier.

![pic4](https://cdn.analyticsvidhya.com/wp-content/uploads/2019/02/colorPixelExample.jpeg)

## Image processing operations

When you write a Computer Vision algorithm, there are a lot of basic image processing operations that you will use over and over again. Most of these functions are present in the imgproc module. You can do things such as image filtering, morphological operations, geometric transformations, color conversions, drawing on images, histograms, shape analysis, motion analysis, feature detection, and so on. Let's consider the following figure:

![images](https://static.packt-cdn.com/products/9781785280948/graphics/B04283_01_03.jpg)

The right-hand side image is a rotated version of the left-hand side image. We can do this transformation with a single line in OpenCV. There is another module called ximgproc that contains advanced image processing algorithms such as structured forests for edge detection, domain transform filters, adaptive manifold filters, and so on.


## Building GUI

OpenCV provides a module called highgui that handles all the high-level user interface operations. Let's say that you are working on a problem and you want to check what the image looks like before you proceed to the next step. This module has functions that can be used to create windows to display images and/or video. There is also a waiting function that will wait until you hit a key on your keyboard before it goes to the next step. There is a function that can detect mouse events as well. This is very useful to develop interactive applications. Using this functionality, you can draw rectangles on these input windows and then proceed based on the selected region.

Consider the following image:

![test img](https://static.packt-cdn.com/products/9781785280948/graphics/B04283_01_04.jpg)

As you can see, we have drawn a green rectangle on the image and applied a negative film effect to that region. Once we have the coordinates of this rectangle, we can operate only on that region.

## Video analysis

Video analysis includes tasks such as analyzing the motion between successive frames in a video, tracking different objects in a video, creating models for video surveillance, and so on. OpenCV provides a module called video that can handle all of this. There is a module called videostab that deals with video stabilization. Video stabilization is an important part of video cameras. When you capture videos by holding the camera in your hands, it's hard to keep your hands perfectly steady. If you look at that video as it is, it will look bad and jittery. All modern devices use video stabilization techniques to process the videos before they are presented to the end user.

## Feature extraction

As discussed earlier, the human visual system tends to extract the salient features from a given scene so that it can be retrieved later. To mimic this, people started designing various feature extractors that can extract these salient points from a given image. Some of the popular algorithms include SIFT (Scale Invariant Feature Transform), SURF (Speeded Up Robust Features), FAST (Features from Accelerated Segment Test), and so on. There is a module called features2d that provides functions to detect and extract all these features. There is another module called xfeatures2d that provides a few more feature extractors, some of which are still in the experimental phase. You can play around with these if you get a chance. There is also a module called bioinspired that provides algorithms for biologically inspired Computer Vision models.

## Object detection

Object detection refers to detecting the location of an object in a given image. This process is not concerned with the type of object. If you design a chair detector, it will just tell you the location of the chair in a given image. It will not tell you whether it's a red chair with a high back or a blue chair with a low back. Detecting the location of objects is a very critical step in many Computer Vision systems. Consider the following image:

![chair img](https://static.packt-cdn.com/products/9781785280948/graphics/B04283_01_06.jpg)

OpenCV has modules called objdetect and xobjdetect that provide the framework to design an object detector. You can use it to develop detectors for random items such as sunglasses, boots, and so on.

Thus, We can create many projects using Open -CV. Ranging from Machine learning to AI TO Image detection & modification, Open CV has it all.

### Photo credits:

https://subscription.packtpub.com/book/application-development/9781785280948/1/ch01lvl1sec10/what-can-you-do-with-opencv

https://opencv.org/about/
