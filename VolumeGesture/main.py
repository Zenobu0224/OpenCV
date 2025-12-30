import cv2 as cv
import HandTrack as ht
import numpy as np
from pycaw.pycaw import AudioUtilities
import time 

# Initialize Webcam
capture = cv.VideoCapture(0)

# Initialize Hand Tracker class
hand_tracker = ht.HandTracker(num_hands=1, detection_confidence=0.8)

# Initialize System Audio Control (Pycaw)
device = AudioUtilities.GetSpeakers()
speaker_vol = device.EndpointVolume

# FPS calculation (var)
p_time = 0
c_time = 0

# Volume UI (var)
vol_bar = 400
vol_percent = 0

while True:
    successful, imgs = capture.read()
    if not successful:
        print('Error')
        break

    # Process hand landmarks
    imgs = hand_tracker.hand_landmarker(imgs)
    landmark_position = hand_tracker.landmark_position(imgs)

    if landmark_position:
        # Get coordinates for Tip of Thumb (Index 4) and Tip of Index Finger (Index 8)
        x1, y1 = landmark_position[8][1], landmark_position[8][2]
        x2, y2 = landmark_position[4][1], landmark_position[4][2]
        cx, cy = int(x1 + x2) // 2, int(y1 + y2) // 2
        
        # Draw trackers on fingers
        cv.circle(imgs, (x1, y1), 8, (250, 0, 0), -1)
        cv.circle(imgs, (x2, y2), 8, (250, 0, 0), -1)
        cv.line(imgs, (x1, y1), (x2, y2), (250, 0, 0), 3)
        cv.circle(imgs, (cx, cy), 8, (250, 0, 0), -1)

        # Calculate distance between thumb and index finger
        length = np.hypot(x2-x1, y2-y1)

        # Change color to Green when volume is Max
        if length >= 210:      
            cv.circle(imgs, (x1, y1), 8, (0, 250, 0), -1)
            cv.circle(imgs, (x2, y2), 8, (0, 250, 0), -1)
            cv.line(imgs, (x1, y1), (x2, y2), (0, 250, 0), 3)
            cv.circle(imgs, (cx, cy), 8, (0, 250, 0), -1)

        # Change color to Red when volume is Min
        elif length <= 35:
            cv.circle(imgs, (x1, y1), 8, (0, 0, 250), -1)
            cv.circle(imgs, (x2, y2), 8, (0, 0, 250), -1)
            cv.line(imgs, (x1, y1), (x2, y2), (0, 0, 250), 3)
            cv.circle(imgs, (cx, cy), 8, (0, 0, 250), -1)

        # Map the finger distance to Volume Range, Bar Height, and Percentage
        volume = np.interp(length, [35, 210], [-66, 0])
        vol_bar = np.interp(length, [35, 210], [400, 100])
        vol_percent = np.interp(length, [35, 210], [0, 100])

        # Apply the volume to the system
        speaker_vol.SetMasterVolumeLevel(volume, None)

    # Calculate Frames Per Second (FPS)
    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time

    # Draw Volume Bar UI
    cv.rectangle(imgs, (30, 400), (70, 100), (0, 250, 0), 3)
    cv.rectangle(imgs, (30, 400), (70, int(vol_bar)), (0, 250, 0), -1)
    cv.putText(imgs, f'{int(vol_percent)} %', (30, 450), cv.FONT_HERSHEY_PLAIN, 2, (250, 0, 0), 2)

    # Display FPS and Window
    cv.putText(imgs, f'FPS : {int(fps)}', (30, 50), cv.FONT_HERSHEY_PLAIN, 2, (250, 0, 0), 3)
    cv.imshow('Live Video', imgs)

    # Press 'Esc' to exit
    if cv.waitKey(1) & 0xFF==27:
        break

capture.release()
cv.destroyAllWindows()