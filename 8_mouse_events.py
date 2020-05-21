from cv2 import cv2
import numpy as np

# dir(cv2)  ---> This will give all the classes available in the cv2 library

# As we need events list
# events variable will contain all the events present in the cv2 library
# events = [i for i in dir(cv2) if 'EVENT' in i]  


# click_event function is called when some action is performed by the mouse
# x and y are the coordinates of the point at which the mouse will click on the 'Window1'
# The parameters mentioned has been made generalised in cv2 definition
def click_event(event, x, y, flags, param): 
    if event == cv2.EVENT_LBUTTONDOWN:
        text_x_y = str(x)+' , '+str(y)
        cv2.putText(img, text_x_y, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
        cv2.imshow('Window1', img)   # Throughout the same window name will go


img = np.zeros((512, 512, 3))  # This will make a Black image
cv2.imshow('Window1', img)   # Throughout the same window name will go

cv2.setMouseCallback('Window1' , click_event)   # Throughout the same window name will go

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

