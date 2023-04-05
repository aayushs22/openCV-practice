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

    #cv2.imshow('Tophat',tophat)#diff b/w input and opening of image
    #cv2.imshow('Blackhat',blackhat)#diff b/w input and closing of image
    

    cv2.imshow('frame',mask)
    cv2.imshow('grey',res)

    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=1)

    #erosion and dilation help at the boundary.

    #opening help us remove false positives
    #closing help us remove false negatives
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()  
#out.release()  
cv2.destroyAllWindows() 