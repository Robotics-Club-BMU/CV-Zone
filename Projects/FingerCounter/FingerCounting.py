import time 
import cv2 as cv
import HandTrackingModule as HTM 


def main():
    cap = cv.VideoCapture(0) 
    detector = HTM.HandDetector()
    p_time = 0

    TIPS_ID = [4, 8, 12, 16, 20]

    while True:
        success, image = cap.read() 
        image = detector.find_hands(image)
        hand_1_landmarks = detector.find_pos(image, hand_num=0)
        hand_2_landmarks = detector.find_pos(image, hand_num=1)

        fingers_count = 0
        for hand_landmarks in [hand_1_landmarks, hand_2_landmarks]:
            if len(hand_landmarks):
                fingers = []

                # For thumb
                # If hand is left
                print(type(hand_landmarks[0][-1]))
                print(hand_landmarks[0][-1])
                if hand_landmarks[0][-1] == "Left":
                    if hand_landmarks[TIPS_ID[0]][1] > hand_landmarks[TIPS_ID[0]-1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                else:
                    if hand_landmarks[TIPS_ID[0]][1] < hand_landmarks[TIPS_ID[0]-1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                #Loopoing over every finger
                for i in range(1, 5):    
                    # Hand landmarks for ith finger
                    if hand_landmarks[TIPS_ID[i]][2] < hand_landmarks[TIPS_ID[i]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                fingers_count += fingers.count(1)

        c_time = time.time()
        fps = 1/(c_time-p_time)
        p_time = c_time

        cv.putText(image, str(int(fps)), (10, 70),
                cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        if fingers_count:
            cv.rectangle(image, (20, 225), (170, 425), (0, 255, 0), cv.FILLED)
            cv.putText(image, str(fingers_count), (45, 375),
                    cv.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

        cv.imshow("Counting Fingers", image)
        if cv.waitKey(5) & 0xFF == 27:
            break
    cap.release()

if __name__ == "__main__":
    main()