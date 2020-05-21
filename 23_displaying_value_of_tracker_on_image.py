# Displaying the value of the Trackbar on the image

from cv2 import cv2
import numpy as np

def onchange_func(x):
    pass

cv2.namedWindow('Tracker_Window')

cv2.createTrackbar('Tracker', 'Tracker_Window', 10, 250, onchange_func)

while(1):
    # NOTE: If the below image line is put outside the while loop then everytime the slider is moved 
    # the value will come over the previous value means to say that the previous value won't get remove 
    # and the new value will get written over the previous one. This is because as image is outside so 
    # image won't get refresh after every change in slider value
    img = cv2.imread('lena.jpg') # Whenever using while loop always place image inside the loop

    trackbar_value = cv2.getTrackbarPos('Tracker', 'Tracker_Window')

    # Displaying the Tracker value onto the image
    img = cv2.putText(img, str(trackbar_value), (50,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 4)

    cv2.imshow('Tracker_Window', img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
