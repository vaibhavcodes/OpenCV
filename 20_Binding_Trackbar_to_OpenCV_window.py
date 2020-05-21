# Binding Trackbar to OpenCV window

from cv2 import cv2
import numpy as np

def onchange_fxn(x):  # x is the value of trackbar
    print(x)



cv2.namedWindow('Trackbar_Window')  # Creating a window with name as "Trackbar_Window"

# Syntax of creating trackbar
# cv2.createTrackbar( trackbar_name, window_name, value, count, function_to_be_called)
cv2.createTrackbar('Blue_Channel' , 'Trackbar_Window' , 0, 255, onchange_fxn) # Trackbar to change the values for Blue channel
cv2.createTrackbar('Green_Channel' , 'Trackbar_Window' , 0, 255, onchange_fxn) # Trackbar to change the values for Green channel
cv2.createTrackbar('Red_Channel' , 'Trackbar_Window' , 0, 255, onchange_fxn) # Trackbar to change the values for Red channel



while (1):
    img = np.zeros((400,600,3) , np.uint8) # Whenever using while loop always place image inside the loop
    
    # Getting the positions of the Trackbars
    b = cv2.getTrackbarPos('Blue_Channel' , 'Trackbar_Window')
    g = cv2.getTrackbarPos('Green_Channel' , 'Trackbar_Window')
    r = cv2.getTrackbarPos('Red_Channel' , 'Trackbar_Window')

    img[:] = [b, g, r] # Changing the Blue, Greem and Red channels of the image

    cv2.imshow('Trackbar_Window' , img)    
    
    if cv2.waitKey(1) == 27:   # NOTE: Always keep '1' in waitKey in a while loop otherwise our program inside the while loop won't work if '0' is put
        break


cv2.destroyAllWindows()