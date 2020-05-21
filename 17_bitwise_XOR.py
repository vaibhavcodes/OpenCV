# BITWISE_XOR operation on images

from cv2 import cv2
import numpy as np

img1 = cv2.imread("b_w.png")

img2 = np.zeros((184, 307, 3), dtype=np.uint8)  # Creating a black image
img2 = cv2.rectangle(img2, (100,10), (200,100), (255,255,255), -1) # Making a white rectangle inside the black box

bit_xor = cv2.bitwise_xor(img1,img2)

cv2.imshow('IMG1 Window', img1)
cv2.imshow('IMG2 Window', img2)

# In XOR gate 0,0 gives 0 and 1,1 gives 0
cv2.imshow('XOR Window', bit_xor)  # Resultant window

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()