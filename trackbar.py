import cv2 as cv
import numpy as np
def nothing(x):
    pass
# img = np.zeros((300,512,3), np.uint8)

cv.namedWindow('image')
cv.createTrackbar('PC','image', 0, 400, nothing)
switch  = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)
while(1):
    img = cv.imread('leona.png')
    strput = cv.getTrackbarPos('PC','image')

    cv.putText(img, str(strput), (50,50), cv.FONT_HERSHEY_COMPLEX, 4,(255, 0, 0) )


    k = cv.waitKey(1)& 0xFF
    if k == 27 :
        break
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('image',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

# import cv2
# import numpy as np
#
# def nothing(x):
#     pass
#
# # Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)
# cv2.namedWindow('image')
#
# # create trackbars for color change
# cv2.createTrackbar('R','image',0,255,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)
# cv2.createTrackbar('B','image',0,255,nothing)
#
# # create switch for ON/OFF functionality
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'image',0,1,nothing)
#
# while(1):
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
#     # get current positions of four trackbars
#     r = cv2.getTrackbarPos('R','image')
#     g = cv2.getTrackbarPos('G','image')
#     b = cv2.getTrackbarPos('B','image')
#     s = cv2.getTrackbarPos(switch,'image')
#
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b,g,r]
#
# cv2.destroyAllWindows()