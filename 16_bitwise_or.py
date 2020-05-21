# BITWISE_OR operation on images

from cv2 import cv2
import numpy as np

img1 = cv2.imread("b_w.png")

img2 = np.zeros((184, 307, 3), dtype=np.uint8)  # Creating a black image
img2 = cv2.rectangle(img2, (100,10), (200,100), (255,255,255), -1) # Making a white rectangle inside the black box

bit_or = cv2.bitwise_or(img1, img2)

cv2.imshow('IMG1 Window', img1)
cv2.imshow('IMG2 Window', img2)

# Black represent 0 and white represents 1 so BLACK will come only on the places where we have BLACK in
# both the images as only 0 and 0 gives 0 in OR gate
cv2.imshow('OR Window', bit_or)  # Resultant window

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()