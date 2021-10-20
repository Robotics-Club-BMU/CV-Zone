
# Display Multiple Images in One Window

## **Libraries Used**

```
import cv2
import numpy as np
import matplotlib.pyplot as plt
```
![importing libraies](https://user-images.githubusercontent.com/90252937/137975147-f0a0c366-2bfe-4724-91f7-5703a54c788f.jpeg)

## **Importing images**

```
img1 = cv2.imread('image.jpg')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
```

![1st image](https://user-images.githubusercontent.com/90252937/137975466-96660f01-2fbe-4dac-8f88-25fce617c966.jpeg)

### 2nd Same image

```
img2 = cv2.imread('image.jpg')
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.show()
```
![2nd image](https://user-images.githubusercontent.com/90252937/137975602-305dc0fb-681c-42b9-a79b-b28d3eea2372.jpeg)

## Setting images in Horizontal

```
Hori = np.concatenate((img1, img2), axis=1)
```
## **Showing Multiple Image in one Window**

```
cv2.imshow('HORIZONTAL', Hori)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

![image hori](https://user-images.githubusercontent.com/90252937/137976208-73f9002c-d077-4b20-b612-185b0ac308fa.jpeg)
