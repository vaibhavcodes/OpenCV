# Display multiple images using Matplotlib

from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('black_and_white.png')

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

title = ['Original Image' , 'Binary' , 'Binary Inverse' , 'Truncated' , 'ToZero' , 'ToZero Inverse']
images = [img, th1, th2, th3, th4, th5]

for i in range(len(images)):
    # plt.subplot( no_of_rows, no_of_columns, index ) 
    # NOTE: Here index starts with 1
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(title[i])


plt.show()


