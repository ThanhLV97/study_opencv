import cv2 as cv
import datetime
record = cv.VideoCapture(0)
print(record.get(cv.CAP_PROP_FRAME_WIDTH))
print(record.get(cv.CAP_PROP_FRAME_HEIGHT))
record.set(3, 3000)
record.set(4, 3000)
print(record.get(3))
print(record.get(4))
while record.isOpened():
    ret, frame = record.read()
    if ret:
        front = cv.FONT_HERSHEY_COMPLEX
        text = "height " + str(record.get(3)) + " width:" + str(record.get(3))
        date = str(datetime.datetime.now())
        frame = cv.putText(frame, date, (55, 55), front, 1, (255,255,255), cv.LINE_4)
        cv.imshow('video', frame)
        if cv.waitKey(1000) & 0xFF == ord('q'):
            break
    else:
        break
record.release
cv.destroyAllWindows()
