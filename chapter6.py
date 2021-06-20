#joining images

import cv2
import numpy as np
img = cv2.imread("Resources/aa.jpg")

#to join this image with itself
#to join images both or all images should be of same channel
#img2= cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)  #joining this image will not work

hor = np.hstack((img,img))
ver= np.vstack((img,img))

cv2.imshow("Horizontal",hor)

cv2.imshow("Vertical",ver)


cv2.waitKey(0)