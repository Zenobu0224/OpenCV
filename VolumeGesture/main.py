import cv2 as cv
import HandTrack as ht
import numpy as np
from pycaw.pycaw import AudioUtilities
import time 


capture = cv.VideoCapture(0)
hand_tracker = ht.HandTracker(num_hands=1, detection_confidence=0.8)

device = AudioUtilities.GetSpeakers()
speaker_vol = device.EndpointVolume

p_time = 0
c_time = 0

while True:
    successful, imgs = capture.read()

    imgs = hand_tracker.hand_landmarker(imgs)
    landmark_position = hand_tracker.landmark_position(imgs)

    if not successful:
        print('Error')
        break

    if landmark_position:
        x1, y1, = landmark_position[8][1], landmark_position[8][2]
        x2, y2 = landmark_position[4][1], landmark_position[4][2]
        cx, cy = int(x1 + x2) // 2, int(y1 + y2) // 2
        
        cv.circle(imgs, (x1, y1), 8, (250, 0, 0), -1)
        cv.circle(imgs, (x2, y2), 8, (250, 0, 0), -1)
        cv.line(imgs, (x1, y1), (x2, y2), (250, 0, 0), 3)
        cv.circle(imgs, (cx, cy), 8, (250, 0, 0), -1)

        length = np.hypot(x2-x1, y2-y1)

        if length >= 210:
            cv.circle(imgs, (x1, y1), 8, (0, 250, 0), -1)
            cv.circle(imgs, (x2, y2), 8, (0, 250, 0), -1)
            cv.line(imgs, (x1, y1), (x2, y2), (0, 250, 0), 3)
            cv.circle(imgs, (cx, cy), 8, (0, 250, 0), -1)

        elif length <= 35:
            cv.circle(imgs, (x1, y1), 8, (0, 0, 250), -1)
            cv.circle(imgs, (x2, y2), 8, (0, 0, 250), -1)
            cv.line(imgs, (x1, y1), (x2, y2), (0, 0, 250), 3)
            cv.circle(imgs, (cx, cy), 8, (0, 0, 250), -1)

        
        volume = np.interp(length, [35, 210], [-66, 0])

        speaker_vol.SetMasterVolumeLevel(volume, None)
    

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time

    cv.putText(imgs, f'FPS : {int(fps)}', (30, 50), cv.FONT_HERSHEY_PLAIN, 2, (250, 0, 0), 3)
    cv.imshow('Live Video', imgs)

    if cv.waitKey(1) & 0xFF==27:
        break

capture.release()
cv.destroyAllWindows()