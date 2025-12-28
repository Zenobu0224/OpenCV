import cv2 as cv
import time 


capture = cv.VideoCapture(0)

while True:
    successful, imgs = capture.read()

    if not successful:
        print('Error')
        break


    cv.imshow('Live Video', imgs)

    if cv.waitKey(1) & 0xFF==27:
        break

capture.release()
cv.destroyAllWindows()