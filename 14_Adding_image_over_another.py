# Adding one image over another image

from cv2 import cv2
import numpy as np

img1 = cv2.imread("ronaldo.jpg")
img2 = cv2.imread("opencv_logo.png")

img1 = cv2.resize(img1 , (512,512) )
img2 = cv2.resize(img2 , (512,512) )

# result_image = cv2.add(img1, img2)   # Add will simply add two images

# addWeighted method allows us to add weights to an image1 and image2.
# Weights actually means of which image we want the intensity(darkness) more or less
result_image = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)  

cv2.imshow('Window', result_image)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()