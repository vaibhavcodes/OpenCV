# Adaptive thresholding is the method where the threshold value is calculated for smaller regions and 
# therefore, there will be different threshold values for different regions. In OpenCV, you can perform 
# Adaptive threshold operation on an image using the method adaptiveThreshold() of the Imgproc class.

# if an image has different lighting conditions in different areas. In that case, adaptive thresholding can help. 
# Here, the algorithm determines the threshold for a pixel based on a small region around it. So we get 
# different thresholds for different regions of the same image which gives better results for images 
# with varying illumination.
from cv2 import cv2
import numpy as np

img = cv2.imread('sudoku.jpg')


# NOTE: If not converted to grayscale the following error is coming:
# error: (-215:Assertion failed) src.type() == CV_8UC1 in function 'cv::adaptiveThreshold'
 
# The problem is that you are trying to use adaptive thresholding to an image that is not in greyscale. 
# And the function only works with a greyscale images.
# So you have to convert your image to a greyscale format as it is described in documentation.
# They read the image in a greyscale format with: img = cv2.imread('dave.jpg',0). You can also convert it 
# to greyscale

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SYNTAX: adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# NOTE: More the value of 'C' the more white the image becomes
adap_img = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1) # MEAN

adap_img1 = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) # GAUSSIAN


cv2.imshow('Original Image' , img)
cv2.imshow('Adaptive_Mean Image' , adap_img)
cv2.imshow('Adaptive_Gaussian Image' , adap_img1)



if cv2.waitKey(0) ==27:
    cv2.destroyAllWindows()