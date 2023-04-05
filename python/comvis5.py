import cv2
import numpy as np

img1= cv2.imread('c:/Users/Lenovo/Desktop/cpp/python/im1.png',cv2.IMREAD_COLOR)
img2= cv2.imread('c:/Users/Lenovo/Desktop/cpp/python/apple.png',cv2.IMREAD_COLOR)

#add=img1 + img2
"""img1=img1/2
img2=img2/2"""

"""add =cv2.add(img1,img2)

weighted =cv2.addWeighted(img1,0.9,img2,0.1,0)"""





img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
rows,cols,channels=img2.shape

roi=img1[0:rows,0:cols]
#cv2.imshow('add',add)
mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)

dat=img1_bg+img2_fg

cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
cv2.imshow('custom window', dat)

"""print(img1[1500,1500])
print(img2[1500,1500])
print(weighted[1500,1500])"""

cv2.waitKey(0)
#cv2.release()
cv2.destroyAllWindows()
