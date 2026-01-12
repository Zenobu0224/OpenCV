import cv2 as cv
import mediapipe as mp


class HandTrack():
    def __init__(self, mode=False, num_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.num_hands = num_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=mode,
                                         max_num_hands=num_hands,
                                         min_detection_confidence=detection_confidence,
                                         min_tracking_confidence=tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils


    def draw_landmarks(self, imgs, draw=True):
        img_rgb = cv.cvtColor(imgs, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(imgs, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return imgs
    
    
    def get_landmarks(self, imgs):
        landmark_list = []

        if self.results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(self.results.multi_hand_landmarks, self.results.multi_handedness):
                label = handedness.classification[0].label

                if label == 'Left':
                    for id, lm in enumerate(hand_landmarks.landmark):
                        (h, w, _) = imgs.shape

                        cx, cy = int(lm.x*w), int(lm.y*h)

                        landmark_list.append([id, cx, cy])

        return landmark_list