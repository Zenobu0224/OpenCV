import cv2 as cv
import mediapipe as mp

class HandTracker():
    def __init__(self, mode=False, num_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        # Initialize MediaPipe Hand parameters
        self.mode = mode
        self.num_hands = num_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        # Setup MediaPipe Hands and Drawing utilities
        self.mp_hands = mp.solutions.hands
        
        # Model
        self.hands = self.mp_hands.Hands(static_image_mode=mode,
                                         max_num_hands=num_hands,
                                         min_detection_confidence=detection_confidence,
                                         min_tracking_confidence = tracking_confidence)
        
        self.mp_draw = mp.solutions.drawing_utils       # For drawing landmarks & lines

    def hand_landmarker(self, imgs, draw=True):
        # Convert frame to RGB (MediaPipe requires RGB)
        img_bgr = cv.cvtColor(imgs, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(img_bgr)

        # Draw hand connections on the frame if landmarks are detected
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(imgs, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        
        return imgs
    
    def landmark_position(self, imgs):
        landmark_list = []

        # Extract specific coordinates (x, y) for each landmark
        if self.results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(self.results.multi_hand_landmarks, self.results.multi_handedness):
                label = handedness.classification[0].label

                # Focus only on the Left hand landmarks
                if label == "Left":
                    for id, landmark in enumerate(hand_landmarks.landmark):
                        (h, w, _) = imgs.shape
                        # Convert normalized coordinates to pixel coordinates
                        cx, cy = int(landmark.x*w), int(landmark.y*h)
                        landmark_list.append([id, cx, cy])

        return landmark_list