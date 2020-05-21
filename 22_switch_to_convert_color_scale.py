# Putting switch to the Trackbar in OpenCV window 
# Here Switch is nothing but a Trackbar with two values as 0 and 1- 0 means Coloured and 1 means GrayScale

from cv2 import cv2
import numpy as np

def onchange_func(x):
    pass

cv2.namedWindow('Convert_Window')

cv2.createTrackbar('Colour_Scale_Convert', 'Convert_Window', 0, 1, onchange_func)

while(1):
    img = cv2.imread('lena.jpg') # Whenever using while loop always place image inside the loop

    trackbar_value = cv2.getTrackbarPos('Colour_Scale_Convert', 'Convert_Window')

    if trackbar_value == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Convert_Window', img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
