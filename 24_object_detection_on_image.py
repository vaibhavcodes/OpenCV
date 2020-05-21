# Object detection on an image- Masking is used for the object detection

# In OpenCV, a mask image is of type uint8. Pixels of value 0xFF are true and pixels of value 0 are false.

# By applying a mask M on an image I, the pixels of I whose corresponding pixel in M are true are copied into 
# a new image. The rest of the pixels in the new image are set to 0  i.e.  When mask is applied on to an image 
# then a new image is formed with only the required object in white colour and rest of the image will be black 
# as only the required object will have its pixels value as 1 and rest of the image pixels as 0

# R, G, B in RGB are all co-related to the color luminance( or intensity), i.e., We cannot 
# separate color information from luminance. 
# HSV or Hue Saturation Value is used to separate image luminance from color information. 
# This makes it easier when we are working on or need luminance of the image/frame. 
# HSV is also used in situations where color description plays an integral role.

# HSV color space consists of 3 matrices, 'hue', 'saturation' and 'value'. In OpenCV, value range for
# 'hue', 'saturation' and 'value' are respectively 0-179, 0-255 and 0-255. 'Hue' represents the color, 
# 'saturation' represents the amount to which that respective color is mixed with white i.e depth of the colour 
# and 'value' represents the amount to which that respective color is mixed with black i.e. brightness of the colour.

from cv2 import cv2
import numpy as np

def on_change(x):
    pass

cv2.namedWindow("Trackbars")

cv2.createTrackbar("upper_hue", "Trackbars", 0, 179, on_change)
cv2.createTrackbar("upper_saturation", "Trackbars", 0, 255, on_change)
cv2.createTrackbar("upper_value", "Trackbars", 0, 255, on_change)

cv2.createTrackbar("lower_hue", "Trackbars", 0, 179, on_change)
cv2.createTrackbar("lower_saturation", "Trackbars", 0, 255, on_change)
cv2.createTrackbar("lower_value", "Trackbars", 0, 255, on_change)

while True:
    img_bgr = cv2.imread('smarties.png')  # img is of BGR format

    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    cv2.imshow("BGR IMAGE", img_bgr) # Original Image in BGR format

    cv2.imshow("HSV IMAGE", img_hsv)  # Original image converted into HSV format

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

cv2.destroyAllWindows()

# NOTE: To check the blue balls go with the following values: low = [110, 50, 50], high = [130, 255, 255]