import cv2 as cv
import GestureCore as gc
import pyautogui
import time 


wCam = 850
hCam = 699

capture = cv.VideoCapture(0)
capture.set(3, wCam)
capture.set(4, hCam)
hand_track = gc.HandTracker(num_hands=1, detection_confidence=0.75, tracking_confidence=0.75)

p_time = 0
c_time = 0
tip_point = [4, 8, 12, 16, 20]

current_gesture = None

while True:
    successful, imgs = capture.read()

    if not successful:
        print('CV Error')
        break

    imgs = hand_track.tracking(imgs)
    landmark_list = hand_track.find_position(imgs)

    if landmark_list:
        fingers = []

        # THUMB
        if landmark_list[tip_point[0]][1] > landmark_list[tip_point[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        # FINGERS
        for i in range(1, 5):
            if landmark_list[tip_point[i]][2] < landmark_list[tip_point[i]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        new_gesture = None
        if all(f==1 for f in fingers):
            cv.putText(imgs, str('JUMP'), (30, 110), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
            new_gesture = 'JUMP'
        elif all(f==0 for f in fingers):
            cv.putText(imgs, str('ROLLDOWN'), (30, 110), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
            new_gesture = 'ROLLDOWN'
        elif fingers[1] == 1 and fingers[2] == 1:
            cv.putText(imgs, str('LEFT'), (30, 110), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
            new_gesture = 'LEFT'
        elif fingers[1] == 1:
            cv.putText(imgs, str('RIGHT'), (30, 110), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
            new_gesture = 'RIGHT'

        if new_gesture != current_gesture:
            if new_gesture == 'JUMP':
                cv.putText(imgs, str(new_gesture), (30, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
                pyautogui.press('up')
            elif new_gesture == 'ROLLDOWN':
                cv.putText(imgs, str(new_gesture), (30, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
                pyautogui.press('down')
            elif new_gesture == 'LEFT':
                cv.putText(imgs, str(new_gesture), (30, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
                pyautogui.press('left')
            elif new_gesture == 'RIGHT':
                cv.putText(imgs, str(new_gesture), (30, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
                pyautogui.press('right')
            
            current_gesture = new_gesture

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time

    cv.putText(imgs, f'FPS : {int(fps)}', (30, 50), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv.imshow('Live Video', imgs)

    if cv.waitKey(1) & 0xFF==27:
        break

capture.release()
cv.destroyAllWindows()