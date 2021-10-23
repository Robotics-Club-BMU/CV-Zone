import time
import HandTrackingModule as HTM
import cv2 as cv
import math
import numpy as np


def set_brightness(percent: int):
    print(f"Setting the brightness to {percent}")


########################
w_cam, h_cam = 640, 480
########################

cap = cv.VideoCapture(0)
cap.set(3, w_cam)
cap.set(4, h_cam)

p_time = 0
detetctor = HTM.HandDetector()
percent = 0
vol_bar = 400
while True:
    success, image = cap.read()
    image = detetctor.find_hands(image)
    landmark_list = detetctor.find_pos(image)
    if len(landmark_list) != 0:
        x1, y1 = landmark_list[4][1:3]
        x2, y2 = landmark_list[8][1:3]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv.circle(image, (x1, y1), 15, (255, 0, 255), cv.FILLED)
        cv.circle(image, (x2, y2), 15, (255, 0, 255), cv.FILLED)
        cv.circle(image, (cx, cy), 15, (255, 0, 255), cv.FILLED)
        cv.line(image, (x1, y1), (x2, y2), (255, 0, 255), thickness=3)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)
        # Hand range goes from 30 to 250, so we are going make it 35 to 245
        # We need to map 30 to 250 to 0 to 100 for the percentage of the brightness of the LED
        percent = np.interp(length, [25, 245], [0, 100])
        vol_bar = np.interp(length, [25, 245], [400, 150])
        set_brightness(percent)

        if length < 60:
            cv.circle(image, (cx, cy), 15, (0, 255, 0), cv.FILLED)

    cv.rectangle(image, (50, 150), (85, 400), (255, 0, 0), 3)
    cv.rectangle(image, (50, int(vol_bar)), (85, 400), (255, 0, 0), cv.FILLED)
    cv.putText(image, f'{int(percent)} %', (40, 450),
               cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time
    cv.putText(image, f'FPS: {int(fps)}', (40, 50),
               cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv.imshow("LED Brightness", image)
    if cv.waitKey(5) & 0xFF == 27:
        break
cap.release()
