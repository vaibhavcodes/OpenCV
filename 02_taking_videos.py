# taking live videos 
from cv2 import cv2

obj = cv2.VideoCapture(0)    # 0,1,2 refers to the camera number you want to use

while(True):
    ret, frame = obj.read()    # Returns two values:
# ret will contains True or False based on the availability of the frame 
# frame variable will store the frame

    cv2.imshow('vaibhav video frame', frame)

    if cv2.waitKey(1) == ord('q'):   # Here in waitKey(): for images use 0 and for video use 1
        break

cv2.release()   # After the video is done release all the resources
cv2.destroyAllWindows()
