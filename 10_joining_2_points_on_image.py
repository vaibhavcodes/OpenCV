# Joining two points on an image
from cv2 import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,255), -1)  # Produce the circle at the clicked points 

        point_coords.append((x,y))

        if len(point_coords)>=2:
            # Producing the line from Point1 to Point2
            cv2.arrowedLine(img, (point_coords[-2]), (point_coords[-1]), (0,255,0), 2)

        cv2.imshow('Window1', img)



point_coords = []  # To store the coordinates of the points at which mouse has clicked on the screen

img = np.zeros((520,520,3))  # Black image
cv2.imshow('Window1', img)

cv2.setMouseCallback('Window1', click_event)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
