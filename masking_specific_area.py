#import required modules
import numpy as np
import cv2
import matplotlib.pyplot as plt

# create a polygons using all outer corners of the ROI
external_poly = np.array( [[[0, 278], [89, 256], [188, 489], [215, 485], [325, 640], [0, 640]]], dtype=np.int32 )
#external_poly = np.array( [[[1, 262], [105, 275], [240, 639], [1, 639]]], dtype=np.int32 )
im = cv2.imread("./abc.jpg", 1)
print(im.shape)
#cv2.fillPoly( your_image , polygon_coordinate, mask_color(127,127,127) )
cv2.fillPoly( im , external_poly, (127,127,127) )
#save/write the masked image on disk
cv2.imwrite("output_.jpg", im)
