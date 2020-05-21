# Use of Matplotlib library to show a single image

# NOTE: Opencv reads the images in BGR format and matplotlib reads an image in RGB format

from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lena.jpg')  # As this image is read by OpenCV so It's in BGR format
cv2.imshow('Original Image' , img)

# As now we have to show the image using Matplotlib so we need to convert the above image in RGB format
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)

# xticks and yticks are used either to remove x and y tick marks on the plot or to show the tick marks by the 
# label we want. 
# eg: ([]) tell that we don't need any ticks
# eg: (ticks , labels)

plt.xticks([])  # This will not show any ticks on the X- axis
plt.yticks([0, 100, 200, 300, 400, 500] , ['0_label' , '100_label' , '300_label', '400_label', '500_label'])

plt.title("--Lena Image--")  # To show the title above the image
plt.show()



