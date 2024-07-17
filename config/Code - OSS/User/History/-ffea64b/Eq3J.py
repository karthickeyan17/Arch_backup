import cv2
v = cv2.VideoCapture(0)
t=True
while(t):
    ret , fram = v.read()
    print(cv2.resize(fram,(224,224,3)))
    cv2.imwrite("NewPicture.jpg",fram)
    t=False
v.release()

