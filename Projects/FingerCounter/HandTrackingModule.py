import cv2 as cv
import mediapipe as mp
import time


class HandDetector:
    def __init__(self,
                 static_image_mode=False,
                 max_num_hands=2,
                 model_complexity=1,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=static_image_mode,
            max_num_hands=max_num_hands,
            model_complexity=model_complexity,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils


    def find_hands(self, image, draw=True):
        image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return image

    def find_pos(self, image, hand_num=0, draw=True):
        landmark_list = []
        if self.results.multi_hand_landmarks:
            if hand_num < len(self.results.multi_hand_landmarks):
                current_hand = self.results.multi_hand_landmarks[hand_num]
                for ID, landmark in enumerate(current_hand.landmark):
                    h, w, c = image.shape 
                    cx, cy = int(landmark.x*w), int(landmark.y*h)
                    landmark_list.append([ID, cx, cy])
        return landmark_list

        

def main():
    cap = cv.VideoCapture(0)
    p_time = 0
    c_time = 0
    detector = HandDetector()
    while True:
        success, image = cap.read()
        image = detector.find_hands(image)
        landmark_list = detector.find_pos(image)
        if len(landmark_list):
            print(landmark_list[4])

        c_time = time.time()
        fps = 1/(c_time-p_time)
        p_time = c_time

        cv.putText(image, str(int(fps)), (10, 70),
                cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)

        cv.imshow("Hand Tracking", image)
        cv.waitKey(1)

if __name__ == "__main__":
    main()