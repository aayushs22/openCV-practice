import cv2
import numpy as np

img=cv2.imread('c:/Users/Lenovo/Desktop/cpp/python/ph.jpg')


cap= cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()

    frame=cv2.GaussianBlur(frame,(15,15),0)

    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    cedges=cv2.Canny(frame,150,50)   
    sobelxy=cv2.Sobel(frame,cv2.CV_64F,1,1,ksize=5)


    cv2.imshow('original',frame)
    #cv2.imshow('laplacian',laplacian)
    #cv2.imshow('sobelx',sobelx)
    #cv2.imshow('sobely',sobely)
    cv2.imshow('canny edges',cedges)
    cv2.imshow('sobelxy',sobelxy)


    

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()  
#out.release()  
cv2.destroyAllWindows() 