#warp perspective

import cv2
import numpy as np
img = cv2.imread("Resources/dsc.png")
width,height= 330,265
pts1= np.float32([[176,43],[299,78],[127,220],[253,248]])
pts2= np.float32 ([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgW= cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("original",img)

cv2.imshow("wrapped",imgW)
cv2.waitKey(0)