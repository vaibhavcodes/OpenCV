# BITWISE_AND operation on images

from cv2 import cv2
import numpy as np

img1 = cv2.imread("b_w.png")

img2 = np.zeros((184, 307, 3), dtype=np.uint8)  # Creating a black image of the same shape as of img1

# Making a small white rectangle inside the black box such that half white rectangle remains in white 
# side and other half in black side 
img2 = cv2.rectangle(img2, (100,10), (200,100), (255,255,255), -1) 

bit_and = cv2.bitwise_and(img1, img2)

cv2.imshow('IMG1 Window', img1)
cv2.imshow('IMG2 Window', img2)

# Black represent 0 and white represents 1 so white will come only on the places where we have white in
# both the images as only 1 and 1 gives 1 in AND gate
cv2.imshow('And Window', bit_and)  # Resultant window

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()