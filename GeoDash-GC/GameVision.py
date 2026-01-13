import cv2 as cv
import GestureCore as gc
import numpy as np
import pyautogui


capture = cv.VideoCapture(0)

hand_track = gc.HandTrack()

while True:
    successful, imgs = capture.read()

    if not successful:
        print('Capture Error')
        break

    imgs = hand_track.draw_landmarks(imgs)
    landmarks = hand_track.get_landmarks(imgs)

    if landmarks:
        index_tip_x, index_tip_y = landmarks[8][1], landmarks[8][2]
        thumb_tip_x, thumb_tip_y = landmarks[4][1], landmarks[4][2]

        cv.circle(imgs, (index_tip_x, index_tip_y), 7, (0, 255, 0), -1)
        cv.circle(imgs, (thumb_tip_x, thumb_tip_y), 7, (0, 255, 0), -1)

        range = np.hypot(index_tip_x - thumb_tip_x, index_tip_y - thumb_tip_y)

        if range >= 80:
            py


    cv.imshow('Live Video', imgs)

    if cv.waitKey(1) & 0xFF==27:
        break

capture.release()
cv.destroyAllWindows()