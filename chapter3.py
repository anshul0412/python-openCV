import cv2
import numpy as np

#resize and cropping

img= cv2.imread("Resources/aa.jpg")
print(img.shape)  #first height then width
imgR= cv2.resize(img,(200,150))  #first width then height
print(imgR.shape)

imgCrop= img[0:200,200:400]   #first height then width
cv2.imshow("original",img)

cv2.imshow("resized",imgR)

cv2.imshow("cropped",imgCrop)
cv2.waitKey(0)
