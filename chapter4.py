import cv2
import numpy as np

#draw shaped and to put text on images
#first we will create a matrix filled with 0{black}

img= np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 0,0,0

cv2.line(img,(0,0),(300,300),(0,0,255),5)
cv2.circle(img,(300,300),50,(255,0,255),10)

#text on images

cv2.putText(img,"openCV",(300,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,200,20),1)

cv2.imshow("img",img)


cv2.waitKey(0)