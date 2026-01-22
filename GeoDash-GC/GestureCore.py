import cv2 as cv
import mediapipe as mp


class HandTrack():
    def __init__(self, mode=False, num_hands=1, detection_confidence=0.4, tracking_confidence=0.4):
        self.mode = mode
        self.num_hands = num_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=mode,
            max_num_hands=num_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
            model_complexity=0  # Use simpler model for speed
        )
        
        self.draw_lm = mp.solutions.drawing_utils
        self.results = None


    def track_hand(self, imgs, draw=True):
        img_rgb = cv.cvtColor(imgs, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if draw and self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                self.draw_lm.draw_landmarks(imgs, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return imgs
    
    def landmark_position(self, imgs):
        landmark_list = []

        if self.results and self.results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(self.results.multi_hand_landmarks, self.results.multi_handedness):
                label = handedness.classification[0].label

                if label == 'Right':
                    h, w = imgs.shape[:2]
                    
                    for id, landmark in enumerate(hand_landmarks.landmark):
                        cx, cy = int(landmark.x * w), int(landmark.y * h)
                        landmark_list.append([id, cx, cy])
                    
                    break  # Only process first right hand

        return landmark_list