import cv2 as cv
import numpy as np
def click_envent(event,x,y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,' ,', y)
        font = cv.FONT_HERSHEY_COMPLEX
        strXY = str(x) + ' ,' + str(y)
        cv.putText(img, strXY,(x,y),font,1,(255,0,0),4, cv.LINE_4)
        cv.imshow('img',img)

img = cv.imread('leona.png')
img2 = cv.imread('hong.jpg')
# print(img.shape, img.size, img.dtype)
# b,g,r = cv.split(img)
# img =cv.merge((b,g,r))
# ball = img[251:281,252 :282] # same size for two region
# img[206:236,235:265] = ball
# cv.imshow('img',img)
# cv.setMouseCallback('img',click_envent)
img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))
# dst = cv.add(img,img2)
dst = cv.addWeighted(img,.5,img2,.9,0)
cv.imshow('dsr',dst)
cv.waitKey(0)
cv.destroyAllWindows()
print("in some thing ")
