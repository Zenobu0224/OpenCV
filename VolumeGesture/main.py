import cv2 as cv
import HandTrack as ht
import time 


capture = cv.VideoCapture(0)
hand_tracker = ht.HandTracker()

while True:
    successful, imgs = capture.read()

    imgs = hand_tracker.hand_landmarker(imgs)
    landmark_position = hand_tracker.landmark_position(imgs)

    if not successful:
        print('Error')
        break

    if landmark_position:
        print(landmark_position[8])

    cv.imshow('Live Video', imgs)

    if cv.waitKey(1) & 0xFF==27:
        break

capture.release()
cv.destroyAllWindows()