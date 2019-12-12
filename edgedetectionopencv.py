import cv2
import numpy as np
snap = cv2.VideoCapture(0)
while(1):
    ret,frame=snap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_red=np.array([30,150,50])
    u_red=np.array([255,255,180])
    boundry=cv2.inRange(hsv,l_red,u_red)
    og_imag=cv2.bitwise_and(frame,frame,mask = boundry)
    cv2.imshow('Original',frame)
    edges=cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)
    esc=cv2.waitKey(5) & 0xFF
    if esc ==27:
        break
snap.release()
cv2.destroyAllWindows()
