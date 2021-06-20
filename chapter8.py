#contours and shape detection

import cv2
import numpy as np

def getContours(img):
    _,contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #(this function provide three things: image , contour and hierarchy, so need to put _ in  beginning)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgCon,cnt,-1,(255,0,0),3)
        perimeter = cv2.arcLength(cnt,True)
        #print(perimeter)
        approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
        print(len(approx))
        objcor = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        if objcor == 3: objtype = "tri"
        elif objcor == 4:
            aspratio = w/float(h)
            if aspratio >0.9 and aspratio <1.10 : objtype= "square"
            else: objtype= "rectangle"
        else: objtype = "circle"
        cv2.rectangle(imgCon,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.putText(imgCon,objtype,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

path = "Resources/Capture.PNG"
img = cv2.imread(path)
imgCon = img.copy()

imgG = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgB = cv2.GaussianBlur(img,(7,7),1)
imgC = cv2.Canny(imgB,50,50)
getContours(imgC)

cv2.imshow("jar",img)
cv2.imshow("imgG",imgG)
#cv2.imshow("blur",imgB)
cv2.imshow("canny",imgC)
cv2.imshow("contour",imgCon)
cv2.waitKey(0)