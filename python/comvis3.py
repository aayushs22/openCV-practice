import numpy as np
import cv2

img=cv2.imread('c:/Users/Lenovo/Desktop/cpp/python/ph.jpg',cv2.IMREAD_COLOR)

cv2.rectangle(img,(0,0),(150,150),(255,255,255),15 )
cv2.circle(img,(150,63),55,(45,0,66),-1)
#cv2.line(img,(0,0),(150,150),(255,255,255),15 )
pts=np.array([[10,5],[20,30],[70,20]],np.int32)
#pts=pts.reshape((-1,0,1))
cv2.polylines(img,[pts],True,(0,255,255),1)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(0,130),font,18,(12,56,88),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()