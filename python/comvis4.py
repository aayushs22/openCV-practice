import numpy as np
import cv2
#cv2.namedWindow('timtim', cv2.WINDOW_NORMAL)
img=cv2.imread('c:/Users/Lenovo/Desktop/cpp/python/ph.jpg',cv2.IMREAD_COLOR)
px=img[55,55]
print(px) 
img[55,55]=[255,255,255]
print(px)  

roi =img[100:150,100:150]

print(roi)

#img[100:1500,100:150]=(45,66,35)
img[100:150,100:150]=img[700:750,700:750]
#cv2.imshow('timtim',img)
cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
cv2.imshow('custom window', img)

cv2.waitKey(0)
cv2.destroyAllWindows()