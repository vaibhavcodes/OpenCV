# Smoothening is often used to reduce noise in an image.
# Smootheing the Images by Blurring -  It is achieved by various types of filters like:
# Homogeneous filter, Gaussian filter, Median filter, Bilateral filter

# Images are filtered using various low-pass filter & high-pass filter
# LPF is used for image blurring
# HPF is used for edges finding

from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv_logo.png')
#img = cv2.imread('salt_pepper_noise.jpg') # Use this image for MedianBlur()

img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Converted for matplotlib


# We can see that the original image has noise that we can see at the outer edges of the text

# Homogeneous filter: 
# It is done by filter2d
# Here each output pixel is the mean of its kernel neighbours
kernel = np.ones((5,5) , np.float32)/25 # As we are taking kernel size of 5x5 so we have divided by 1*25 = 25
# Here we have divided by 25 to make each element of the kernal a mean of its neighbours

hom = cv2.filter2D(img, -1, kernel)
# After this filter we can see that the noise from the edges of the text has gone and now the edges have 
# become smooth

# When we want image blurring we need to convolve the image over LPF. There are various algorithms for that:

# Algo-1: Averaging algorithm- blur()
blur = cv2.blur(img , (5,5))

# Gaussianblur()- In this the pixels of kernel at the centre have more weight and decreases as it move towards 
# left or right. It shows better result then blur().
# Gaussian blur is designed mainly for removing high frequency noise
gblur = cv2.GaussianBlur(img, (5,5), 0)

# MedianBlur() filter - This filter is used when dealing with 'Salt and Pepper' noise. The images which have dot dot 
# all over the image are salt and pepper noise
# This filter replaces each pixel with the median of its neighbouring pixels
median = cv2.medianBlur(img, 5) #Kernel size=5
# NOTE: for medianBlur() the kernel size is always odd and greater than 1

# bilateralFilter --> It is used when we want to make the image blurred by keeping the edges intact and sharp
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

images = [img, hom, blur, gblur, median, bilateral]
title = ['Original Image', 'Homogeneous' , 'Blur Image', 'GaussianBlur Image' , 'Median Image', 'Bilateral Image']


for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])
    plt.title(title[i])
    
plt.show()
