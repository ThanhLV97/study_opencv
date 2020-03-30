import cv2 as cv
img = cv.imread('leona.png', 0)
cv.imshow('image',img)
k= cv.waitKey(0) & 0xFF
if k ==27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('copy_leona.jpg', img)
    cv.destroyAllWindows()
# print(img)

