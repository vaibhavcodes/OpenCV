# Thresholding --> Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation 
# to the threshold value provided. 
# In thresholding, each pixel value is compared with the threshold value. 
# If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value 
# (generally 255).

from cv2 import cv2
import numpy as np

# In gradient.jpg we can see that there is a shade from black starting at the left decreasing to white at 
# the right most i.e. pixels from '0' i.e. pixel value of 'black' to the '255' which is a pixel value 'white'
img = cv2.imread("gradient.jpg")

threshold_value = 127

# NOTE: threshold function returns two values- return and image
# SYNTAX:-->  threshold(src , threshold_value , maxval , type_of_threshold)

# cv2.THRESH_BINARY--> As it's binary, pixels < threshold_value will be converted to 0 and pixels > threshold_value
# will be converted to 1

# cv2.THRESH_BINARY_INV --> It works vice-versa of the above one

_ , thr_img1 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
_ , thr_img2 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY_INV)


# cv2.THRESH_TRUNC --> Up to threshold value the same pixels as that of original image will be retained but
# for the pixels > threshold_value the pixels value will be equal to the threshold_value
_ , thr_img3 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_TRUNC)


# cv2.THRESH_TOZERO --> for pixels < threshold_value the pixel value will be converted to 0 and for the
# pixels > threshold_value the same pixels as that of original image will be retained

# cv2.THRESH_TOZERO_INV --> It works just the vice-versa of the above one
_ , thr_img4 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_TOZERO)
_ , thr_img5 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_TOZERO_INV)


cv2.imshow('Original Image', img)
cv2.imshow('1_THRESH_BINARY Image', thr_img1)
cv2.imshow('2_THRESH_BINARY_Inverse Image', thr_img2) 
cv2.imshow('3_THRESH_TRUNC Image', thr_img3)
cv2.imshow('4_THRESH_TOZERO Image', thr_img4)
cv2.imshow('5_THRESH_TOZERO_INV Image', thr_img5)

if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()