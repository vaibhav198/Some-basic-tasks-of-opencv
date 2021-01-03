import numpy as np
import cv2

def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x,', ', y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		strXY = str(x) + ', ' +str(y)
		cv2.putText(img, strXY, (x, y), font, 0.5, (0, 255, 0), 2)
		cv2.imshow('image', img)

img = cv2.imread('triv3.jpg')
img = cv2.resize(img, (360, 640))
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

