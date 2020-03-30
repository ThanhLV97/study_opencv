import  cv2 as cv
import  numpy as np
img = cv.imread('gradient.jpg',0)
_,th1 = cv.threshold(img,117,255,cv.THRESH_BINARY)
_,th2 =cv.threshold(img,117,255,cv.THRESH_BINARY_INV) # 0-1 and 1-0
_,th3 =cv.threshold(img,50,255,cv.THRESH_TRUNC) # 50-255 to trunc
_,th4 =cv.threshold(img,50,255,cv.THRESH_TOZERO) # 50-250 TO BLACK




cv.imshow('th1',th1)
cv.imshow('img',img)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.imshow('th4',th4)
cv.waitKey(0)
cv.destroyAllWindows()