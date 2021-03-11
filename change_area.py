import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--path", type = str, required = True, help = "Path of input image")
ap.add_argument("-p", "--percent", type = int, default=20, help = "percent to which incr/decr mask")
ap.add_argument("-o", "--operation", type = str, required = True, help = "operation type")

args = vars(ap.parse_args())

op = args["operation"]

img = cv2.imread(args["path"])
#print(img.shape)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(img.shape)

cnts = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
if len(cnts) == 1:
	A = cv2.contourArea(cnts[0])
	#print("Original A: ", A)
	#for increasing the mask
	if op == 'increase':
		increase_area = A + A*(args["percent"]/100)
		while A < increase_area:
			img = cv2.dilate(img, (3, 3), iterations=1)
			cnts = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours(cnts)
			A = cv2.contourArea(cnts[0])
		cv2.imwrite("increased-mask.png", img)
	#for decreasing the mask
	elif op == 'decrease':
		decrease_area = A - A*(args["percent"]/100)
		while A > decrease_area:
			img = cv2.erode(img, (3, 3), iterations = 1)
			cnts = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours(cnts)
			A = cv2.contourArea(cnts[0])
		cv2.imwrite("decreased_mask.png", img)
	#if given operation is other than incr/decr
	else:
		print("Please enter valid operation")
#no considering more than one mask in a single image
else:
	print("More than one mask in a single image")


