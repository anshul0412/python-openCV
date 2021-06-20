import cv2
import numpy as np

#web cam
widthimg = 480
heightimg = 640
cap=cv2.VideoCapture(1)
cap.set(3,480)
cap.set(4,480)
cap.set(10,150)

def preprocess(img):
    imgG = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgB = cv2.GaussianBlur(img,(5,5),1)
    imgC = cv2.Canny(imgB, 200, 200)
    kernel = np.ones((5,5))
    imgD = cv2.dilate(imgC,kernel,iterations=2)
    imgE = cv2.erode(imgD,kernel,iterations=1)

    return imgE

def getContours(img):
    biggest = np.array([])
    maxarea = 0
    _,contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #(this function provide three things: image , contour and hierarchy, so need to put _ in  beginning)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            #print(area)
           #cv2.drawContours(imgCon,cnt,-1,(255,0,0),3)
            perimeter = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            if area > maxarea and len(approx) == 4:
                biggest = approx
                maxarea = area
    cv2.drawContours(imgCon, biggest, -1, (255, 0, 0), 20)
    return biggest

def reorder(mypoints):
    mypoints = np.array(mypoints).reshape(4,2)
    mypointsnew = np.zeros((4,1,2), np.int32)
    add = mypoints.sum(1)
    #print("add", add)
    mypointsnew[0] = mypoints[np.argmin(add)]
    mypointsnew[3] = mypoints[np.argmax(add)]
    diff = np.diff(mypoints,axis=1)
    mypointsnew[1] = mypoints[np.argmin(diff)]
    mypointsnew[2] = mypoints[np.argmax(diff)]
   #print("newPoints",mypointsnew)
    return mypointsnew




def getwrap(img,biggest):
    """
    biggest = [[353,96],
               [186,138],
               [193,492],  #no need to define this biggest as it depend on the quality of webcam how much time it took to detect the contour corners
               [418,441]]
    """
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0],[widthimg,0],[0,heightimg],[widthimg,heightimg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgW = cv2.warpPerspective(img, matrix, (widthimg, heightimg))

    imgcropped = imgW[20:imgW.shape[0]-20,20:imgW.shape[1]-20]
    imgcropped = cv2.resize(imgcropped,(widthimg,heightimg))
    return imgcropped

while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthimg,heightimg))
    imgCon = img.copy()
    imgRes = preprocess(img)

    biggest = getContours(imgRes)
    if biggest.size !=0:
        imgWarped = getwrap(img,biggest)
        cv2.imshow("initial", img)
        cv2.imshow("contour", imgCon)
        cv2.imshow("preprocessing", imgRes)
        cv2.imshow("final", imgWarped)
    else:
        cv2.imshow("initial", img)
        cv2.imshow("preprocessing", imgRes)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break