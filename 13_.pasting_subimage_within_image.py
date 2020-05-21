# Pasting a small part from an image to another part or position within an image

from cv2 import cv2
import numpy as np

img = cv2.imread('ronaldo.jpg')


co = img[280:340, 330:390]   # Taking the pixels from the required area

img[273:333, 100:160] = co   # Pasting the pixels of the subimage over required area

cv2.imshow('Window1', img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()