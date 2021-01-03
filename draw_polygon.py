import cv2
import numpy as np
from PIL import Image

c1 =cv2.imread('./triv3.jpg')
print(c1.shape)
c1 = cv2.resize(c1,(360, 640))

pts = np.array([[4, 178], [60, 165], [348, 623], [4, 635]], np.int32)
c1= cv2.polylines(c1, [pts], True, (0, 255,0))	
#cv2.imshow("img", c1)
cv2.imwrite("triv3.jpg", c1)

