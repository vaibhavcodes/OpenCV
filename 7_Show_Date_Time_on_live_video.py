# Show the current Date & Time on live video
from cv2 import cv2
import datetime

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    date_time = str(datetime.datetime.now())

    # Putting Date and Time on the frame
    frame = cv2.putText( frame, date_time, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2 )

    cv2.imshow('Video Window' , frame)


    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()