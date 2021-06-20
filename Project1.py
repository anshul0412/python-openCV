import cv2
import numpy as np

#read web cam

framewidth= 640
frameheight= 480

cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)

mycolors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255],
            [90,48,0,118,255,255]]

mycolorvalues = [[51,153,255],   #BGR
                 [255,0,255],
                 [0,255,0],
                 [255,0,0]]

mypoints = []     #[x,y,colorid]

def findcolor(img, mycolors,mycolorvalues):
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new=[]
    for color in mycolors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imghsv,lower,upper)
        x,y= getContours(mask)
        cv2.circle(imgResult,(x,y),10,mycolorvalues[count],cv2.FILLED)
        if x!=0 and y!=0:
            new.append([x,y,count])
        count += 1
        #cv2.imshow(str(color[0]),mask)
    return new


def getContours(img):
    _,contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #(this function provide three things: image , contour and hierarchy, so need to put _ in  beginning)
    x,y,w,h= 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            perimeter = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawoncanvas(mypoints, mycolorvalues):
    for point in mypoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, mycolorvalues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    new = findcolor(img,mycolors,mycolorvalues)
    if len(new)!=0:
        for n in new:
            mypoints.append(n)

    if len(mypoints)!=0:
        drawoncanvas(mypoints,mycolorvalues)


    cv2.imshow("result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

