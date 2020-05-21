# Image features and making an image using B,G,R channles values

from cv2 import cv2
import numpy as np

img = cv2.imread("ronaldo.jpg")

print(img.shape)  # (503, 750, 3)  --> returns a tuple of rows, columns and channels 
print(img.size)   # 1131750   ---> returns total number of pixels
print(img.dtype)  # uint8  ---> returns the datatype of the image

# a = cv2.split(img)  # It will return an array of 3 arrays each representing one-one channel of B, G and R 
# print(len(a))  # It will return 3 

b, g, r = cv2.split(img)  # B, G, R channels will get store in their respective variable

# If we are given B.G,R channels values Merge will create an image by combining b,g,r channels.
img1 = cv2.merge((b,g,r))  # New image img1 is created by merging B,G,R channels

cv2.imshow('Window1', img1)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()


