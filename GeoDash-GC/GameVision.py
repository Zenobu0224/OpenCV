import cv2 as cv
import GestureCore as gc


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
        print(landmarks[8])

    cv.imshow('Live Video', imgs)

    if cv.waitKey(1) & 0xFF==27:
        break

capture.release()
cv.destroyAllWindows()