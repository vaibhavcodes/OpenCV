# Applying BITWISE_NOT operation on a downloaded image

from cv2 import cv2
import numpy as np

img1 = cv2.imread("black_and_white.png")

bit_not = cv2.bitwise_not(img1)

cv2.imshow('IMG1 Window', img1)


cv2.imshow('IMG1 NOT Window', bit_not)  # Resultant window

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()