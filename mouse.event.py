import cv2 as cv
import numpy as np
events = [i for i in dir(cv) if "EVENT" in i]
print(events)
points = []
def click_event(event,x,y,flags , param ):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x," ,", y)
        font = cv.FONT_HERSHEY_COMPLEX
        strXY = str(x) + ";" + str(y)
        cv.putText(img1, strXY, (x,y), font, 1, (255,255,0), cv.LINE_4)
        cv.imshow("img",img1)
    # if event == cv.EVENT_RBUTTONDOWN:
    #     print(x, " ,", y)
    #     blue = img1[y, x, 0]
    #     green = img1[y, x, 1]
    #     red = img1[y, x, 2]
    #
    #     font = cv.FONT_HERSHEY_COMPLEX
    #     strRGB = str(blue) + ", " + str(green) + ", " + str(red)
    #     cv.putText(img1, strRGB, (x, y), font, 1, (0, 255, 0), cv.LINE_4)
    #     cv.imshow("img", img1)
    # if event == cv.EVENT_RBUTTONDOWN:
    #     cv.circle(img1,(x,y),3,(255,0,0),4,cv.LINE_4)
    #     points.append((x,y))
    #     if len(points) >= 2:
    #         cv.line(img1,points[-2], points[-1],(255,0,0),cv.LINE_4)
    #     cv.imshow('img',img1)
    if event == cv.EVENT_RBUTTONDOWN:
        blue = img1[y,x,0]
        green = img1[y, x, 1] 
        red = img1[y, x, 2]
        colorimage = np.zeros((512,512,3),np.uint8)
        colorimage[:] = [blue,green,red]
        cv.imshow('img1',colorimage)



# img1 = np.zeros((512,512,3), np.uint8)
img1 = cv.imread("leona.png", )
cv.imshow("img", img1)
cv.setMouseCallback("img",click_event)
cv.waitKey(0)
cv.destroyAllWindows()

