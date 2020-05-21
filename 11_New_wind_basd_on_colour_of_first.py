# New window is created of the colour the one which has been clicked in the original image in the first window
from cv2 import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2] 

        img_new = np.zeros((512,512,3), np.int8)  # Initially the new window has black image

        img_new[:] = [blue, green, red]  # Changing the colour channel of the image on the window 

        cv2.imshow('new_window', img_new)  # Showing the new image in new window


img = cv2.imread('lena.jpg')

cv2.imshow('Window1', img)

cv2.setMouseCallback('Window1', click_event)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
