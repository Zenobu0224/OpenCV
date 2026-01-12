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

    # def draw_landmarks(imgs, draw=True):
    #     img_rgb = cv.cvtColor(imgs, cv.COLOR_BGR2RGB)
    #     self.results