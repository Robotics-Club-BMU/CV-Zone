
#  Erosion , Dilation ,Opening & Closing of images using OpenCV in python

## Basics of Erosion: 

- Erodes away the boundaries of the foreground object.
- Used to diminish the features of an image.

### Working of erosion: 
 

1. A kernel(a matrix of odd size(3,5,7) is convolved with the image.
2. A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel are 1, otherwise, it is eroded (made to zero).
3. Thus all the pixels near the boundary will be discarded depending upon the size of the kernel.
4. So the thickness or size of the foreground object decreases or simply the white region decreases in the image.

## Basics of dilation: 
 

- Increases the object area
- Used to accentuate features
- Working of dilation:
 

1. A kernel(a matrix of odd size(3,5,7) is convolved with the image
2. A pixel element in the original image is ‘1’ if at least one pixel under the kernel is ‘1’.
3. It increases the white region in the image or the size of the foreground object increases 
 
## Uses of Erosion and Dilation: 
 

### Erosion: 
- It is useful for removing small white noises.
- Used to detach two connected objects etc.

### Dilation:
- In cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
- It is also useful in joining broken parts of an object.

### Opening an image

In this program, we will perform the opening operation on image. Opening removes small objects from the foreground of an image, placing them in the background. This technique can also be used to find specific shapes in an image. Opening can be called erosion followed by dilation. The function we will use for this task is cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel).

### Closing an image

In this program, we will perform the closing operation using the cv2.morphologyEx() function. Closing removes small holes in the foreground, changing small holes of background into foreground. This technique can also be used to find specific shapes in an image. The function we will use for this task is cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel).

