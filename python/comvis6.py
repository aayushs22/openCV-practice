import cv2
import numpy as np

img=cv2.imread('c:/Users/Lenovo/Desktop/cpp/python/bookpage.jpg')

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)


cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
cv2.imshow('custom window',gaus)
cv2.waitKey(0)
#cv2.release()
cv2.destroyAllWindows()