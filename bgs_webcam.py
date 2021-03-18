import cv2

import numpy as np

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fg = fgbg.apply(frame)
    cv2.imshow('Original', frame)
    cv2.imshow('mask', fg)
    
    k = cv2.waitKey(30)
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
