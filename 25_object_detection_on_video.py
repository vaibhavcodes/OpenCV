# Object detection on an video

from cv2 import cv2
import numpy as np

def on_change(x):
    pass

vid = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

cv2.createTrackbar("upper_hue", "Trackbars", 0, 179, on_change)
cv2.createTrackbar("upper_saturation", "Trackbars", 0, 255, on_change)
cv2.createTrackbar("upper_value", "Trackbars", 0, 255, on_change)

cv2.createTrackbar("lower_hue", "Trackbars", 0, 179, on_change)
cv2.createTrackbar("lower_saturation", "Trackbars", 0, 255, on_change)
cv2.createTrackbar("lower_value", "Trackbars", 0, 255, on_change)

while True:
    ret , img_bgr = vid.read()

    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    cv2.imshow("BGR IMAGE", img_bgr) # Original Image i.e video frame in BGR format

    # Getting the values of the trackbars
    lower_h = cv2.getTrackbarPos("lower_hue", "Trackbars")
    lower_s = cv2.getTrackbarPos("lower_saturation", "Trackbars")
    lower_v = cv2.getTrackbarPos("lower_value", "Trackbars")

    higher_h = cv2.getTrackbarPos("upper_hue", "Trackbars")
    higher_s = cv2.getTrackbarPos("upper_saturation", "Trackbars")
    higher_v = cv2.getTrackbarPos("upper_value", "Trackbars")

    # Now masking the HSV image
    # Between the colour shades of lower_color_hsv_code and higher_color_hsv_code the colour 
    # will be masked and rest will be turned black
    lower_color_hsv_code = np.array([lower_h , lower_s , lower_v])

    higher_color_hsv_code = np.array([higher_h , higher_s , higher_v])

    # Creation of Masked image
    img_mask = cv2.inRange(img_hsv , lower_color_hsv_code, higher_color_hsv_code) 
    # Displaying the Masked image
    cv2.imshow("Masked IMAGE", img_mask)  

    # Taking bitwise_and of the masked image with original image to get the required output
    result_img = cv2.bitwise_and(img_bgr, img_bgr, mask = img_mask)
    # Displaying the Resultant image
    cv2.imshow("Resultant IMAGE", result_img)


    if cv2.waitKey(1)==27:
        break

vid.release()
cv2.destroyAllWindows()

