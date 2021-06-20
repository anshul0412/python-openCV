import cv2
print("package imported")

"""img= cv2.imread("Resources/jar.PNG")
cv2.imshow("output",img)
cv2.waitKey(0)
"""
#video capture

"""
cap=cv2.VideoCapture("Resources/bruno.mp4")
while True:
    success, img1= cap.read()
    cv2.imshow("video",img1)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
"""

#web cam

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img1 = cap.read()
    cv2.imshow("video", img1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break