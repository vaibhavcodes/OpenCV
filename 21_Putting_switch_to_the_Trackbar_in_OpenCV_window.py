# Putting switch to the Trackbar in OpenCV window
# Switch is nothing but a Trackbar with two values as 0 and 1- o means OFF and 1 means ON

from cv2 import cv2
import numpy as np

def onchange_fxn(x):  # x is the value of trackbar
    print(x)

#img = np.zeros((400,600,3) , np.uint8)

cv2.namedWindow('Trackbar_Window')  # Creating a window with name as "Trackbar_Window"

# Syntax of creating trackbar
# cv2.createTrackbar( trackbar_name, window_name, min_value, max_value, function_to_be_called)
cv2.createTrackbar('Blue_Channel' , 'Trackbar_Window' , 0, 255, onchange_fxn) # Trackbar to change the values for Blue channel
cv2.createTrackbar('Green_Channel' , 'Trackbar_Window' , 0, 255, onchange_fxn) # Trackbar to change the values for Green channel
cv2.createTrackbar('Red_Channel' , 'Trackbar_Window' , 0, 255, onchange_fxn) # Trackbar to change the values for Red channel

# Creating a switch
switch_name = "Switch-\n 0: ON \n 1: OFF "
cv2.createTrackbar(switch_name , 'Trackbar_Window' , 0, 1, onchange_fxn)


while (1): # Whenever using while loop always place image inside the loop
    img = np.zeros((400,600,3) , np.uint8)
    # Getting the positions of the Trackbars
    b = cv2.getTrackbarPos('Blue_Channel' , 'Trackbar_Window')
    g = cv2.getTrackbarPos('Green_Channel' , 'Trackbar_Window')
    r = cv2.getTrackbarPos('Red_Channel' , 'Trackbar_Window')

    # # Getting the positions of the switch Trackbar
    s = cv2.getTrackbarPos(switch_name , 'Trackbar_Window')

    if s==1: # Checking if the switch is ON
        img[:] = [b, g, r] # Changing the Blue, Greem and Red channels of the image
    else:
        img[:] = 0   # 0 means no change in the BGR channels of the image 

    cv2.imshow('Trackbar_Window' , img)    
    
    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows()