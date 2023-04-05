import cv2
import numpy as np

img=cv2.imread('c:/Users/Lenovo/Desktop/cpp/python/ph.jpg')


cap= cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_red=np.array([150,50,0])
    upper_red=np.array([180,255,255])
    
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    

    cv2.imshow('frame',mask)
    cv2.imshow('grey',res)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()  
#out.release()  
cv2.destroyAllWindows()