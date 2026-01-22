import cv2 as cv
import GestureCore as gc
import numpy as np
import pyautogui
import time 


capture = cv.VideoCapture(0)
# Reduce camera resolution for better performance
capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

hand_track = gc.HandTrack(num_hands=1, detection_confidence=0.7, tracking_confidence=0.7)

p_time = 0
last_press_time = 0
press_cooldown = 0.1  # Prevent spamming space bar

# Disable pyautogui pause for faster execution
pyautogui.PAUSE = 0


while True:
    successful, imgs = capture.read()

    if not successful:
        print('Capture Error')
        break

    # Flip for mirror effect (optional, makes it more intuitive)
    imgs = cv.flip(imgs, 1)

    cv.imshow('Geometry Dash Hand Controller', imgs)

    if cv.waitKey(1) & 0xFF == 27:
        break