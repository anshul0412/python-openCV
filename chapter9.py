#face detection
import cv2

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
facecascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
eyecascade = cv2.CascadeClassifier("Resources/haarcascade_eye.xml")
#smilecascade = cv2.CascadeClassifier("Resources/haarcascade_smile.xml")

while True:
    success, img = cap.read()

    imgG = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    eyes = eyecascade.detectMultiScale(imgG, 1.1)
    faces = facecascade.detectMultiScale(imgG, 1.1)
    #smile = smilecascade.detectMultiScale(imgG, 1.1,4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img,"face",(x,y-5),
                    cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255),2)

    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "eyes", (x, y - 5),
                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)

    """

    for (x, y, w, h) in smile:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img,"smile",(x,y-5),
                    cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255),2)
    
    """

    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break