## Installation
install anaconda [anaconda](https://www.anaconda.com/products/individual) and work in jupyter notebook



## Usage
```python
import cv2
import numpy as np
src = cv2.imread("D:/Kriti Banka/threshold.png", cv2.IMREAD_GRAYSCALE)
ret, thresh1 = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold', thresh1)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
ret, thresh2 = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Binary Threshold Inverted', thresh2)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
ret, thresh3 = cv2.threshold(src, 120, 255, cv2.THRESH_TRUNC)
cv2.imshow('Truncated Threshold', thresh3)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
ret, thresh4 = cv2.threshold(src, 120, 255, cv2.THRESH_TOZERO)
cv2.imshow('Set to 0', thresh4)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
ret, thresh5 = cv2.threshold(src, 120, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('Set to 0 Inverted', thresh5)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
 ```
 ## Output
 
 <img width="385" alt="binary threshold" src="https://user-images.githubusercontent.com/72350827/138158007-f65fadf2-60e4-4824-8ca8-c405a2487c75.PNG">
 
 <img width="383" alt="binary threshold inverse" src="https://user-images.githubusercontent.com/72350827/138158035-c1e72847-1e8c-48ed-9704-cd2a7a0123db.PNG">
 
 <img width="384" alt="set to 0" src="https://user-images.githubusercontent.com/72350827/138158088-ee9a2365-b618-4415-96a7-34dd5024d933.PNG">
 
 <img width="383" alt="set to 0 inverted" src="https://user-images.githubusercontent.com/72350827/138158110-76c65ed5-0a98-47a2-bbca-3a724a84428c.PNG">
 
 <img width="388" alt="truncated threshold" src="https://user-images.githubusercontent.com/72350827/138158138-cc140ad9-e48e-4d64-98b5-003c7a0edb7d.PNG">





