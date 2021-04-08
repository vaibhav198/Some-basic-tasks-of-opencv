"""
this is a simple python program to rotate an image by 90 
degree clockwise, and comparing the time taken by cv2.rotate() and 
cv2.transpose() + cv2.flip()
"""
#Importing important packages
import cv2
import time
#Reading original image
img = cv2.imread('1.jpg')

#rotate clockwise(Using transpose)
start_time1 = time.time()
r_img = cv2.transpose(img)
r_img = cv2.flip(r_img, flipCode=1) #flipCode = 0 for vertical rotation
print("transpose time is ", (time.time() - start_time1))
#Write rotated image on disk
cv2.imwrite("trans_img.jpg", r_img)
#Rotate image clockwise (using rotate)
start_time2 = time.time()
cr_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
print("Rotation time is ", (time.time() - start_time2))
#write image on disk
cv2.imwrite("rotate_img.jpg", cr_img)
