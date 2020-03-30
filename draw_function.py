import numpy as np
import cv2 as cv
# img = cv.imread('leona.png', 1)
img = np.zeros([555,555,3],np.uint8)
img = cv.line(img, (0,0), (255,255), (0, 0, 255),5 ) #248, 252, 5

img = cv.arrowedLine(img,(0,0),(555,480),(10, 240, 113),6) #113, 240, 10

img = cv.rectangle(img, (55,55), (268,289), (10,233,99),8)

img = cv.circle(img, (100 ,55), 100,(113, 240, 10), 25)
font = cv.FONT_HERSHEY_COMPLEX
img =cv.putText(img, 'true love is break love',(100,100),font,1,(255, 240, 10),cv.LINE_4)

cv.imshow('image', img)
cv.waitKey(0)

cv.destroyAllWindows(0)

