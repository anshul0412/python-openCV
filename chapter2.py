import cv2
import numpy as np

img = cv2.imread("Resources/aa.jpg")
kernel= np.ones((5,5),np.uint8)

imgG= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgB= cv2.GaussianBlur(img,(7,7),0)
imgC= cv2.Canny(img,150,100)
imgD= cv2.dilate(imgC,kernel,iterations=1)
imgE= cv2.erode(imgD,kernel,iterations=1)

cv2.imshow("output_grey",imgG)

cv2.imshow("output_blur",imgB)

cv2.imshow("output_canny",imgC)  #edges in image(edged image(or say image made by lines))

cv2.imshow("output_dilate",imgD)  #increase the thickness of canny image{edges}

cv2.imshow("output_errode",imgE)  #decrease the thickness{opposite of dilation}
cv2.waitKey(0)