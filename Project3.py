import cv2
import numpy as np

framewidth= 640
frameheight= 480
nplatecascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
count = 0

cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)

while True:
    success, img = cap.read()


    imgG = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    numberplate = nplatecascade.detectMultiScale(imgG,1.1)

    for (x, y, w, h) in numberplate:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,"numberPlate",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        n = img[y:y+h,x:x+w]
        cv2.imshow("numberplate",n)

    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("Resources/scanned/nplate/numberplate_"+str(count)+".jpg",n)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"saved",(150,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("result", img)
        cv2.waitKey(500)
        count+=1