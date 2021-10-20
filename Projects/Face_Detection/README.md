
# **Face  Detection**

Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. Today we will be using the face classifier. You can experiment with other classifiers as well.

### Libraries Used

```
import cv2
```

#### Importing cascade

```
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
```
#### Setting webcam

```
webcam = cv2.VideoCapture(0)
```
You can use a video instead of webcam just by replacing (0) with video file

####  Read the frame
```
while True:
    _, img = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
```

#### Rectangle for Face and Output

```
 for (a,b,c,d) in faces:
        cv2.rectangle(img, (a, b), (a+c, b+d), (0, 0, 255), 2)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
webcam.release()
cv2.destroyAllWindows()
```
### Output

![webcam detection](https://user-images.githubusercontent.com/90252937/138077050-5e3ddd30-f1e6-48b3-8d04-9c34ed9e2e71.jpeg)
