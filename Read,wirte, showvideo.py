import cv2 as cv
record = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
"""cài đặt hàm cho out.write"""
out = cv.VideoWriter('save.avi',fourcc,20.0,(640,480))
while  (record.isOpened()):
    ret, frame = record.read()
    if True:
        ret, frame = record.read()
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        print(record.get(cv.CAP_PROP_FRAME_HEIGHT))
        print(record.get(cv.CAP_PROP_FRAME_WIDTH))
        out.write(frame)
        cv.imshow('frame',  frame)

        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break
record.release()
out.release()
cv.destroyAllWindows()