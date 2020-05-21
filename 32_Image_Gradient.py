# Image gradient is the directional change in the intensity or colour of an image

# Laplacian :--> Laplacian Operator is a second order derivative mask which is used to find edges in an image. 
# Laplacian gives better edge localization as compared to first-order.It produces a uniform edge magnitude for
# all directions.

# Laplacian(frame, depth)

# When depth=-1 or CV_64F, the destination image will have the same depth as the source.

# ============================================================================================================
# ============================================================================================================
# ============================================================================================================

# Sobel :--> It is a first order derivative mask which is used to find the edges in a particular direction
# either in X or Y. Using the sobel operation, you can detect the edges of an image in both horizontal and 
# vertical directions.



# Sobel(src, dst, ddepth, dx, dy)

# src − An object of the class Mat representing the source (input) image.
# dst − An object of the class Mat representing the destination (output) image.
# ddepth − An integer variable representing the depth of the image. 
# NOTE: When depth=  (-1) or (CV_64F) , the destination image will have the same depth as the source. 
# dx − An integer variable representing the x-derivative. (0 or 1). 1 when we want gradient in x-direction
# dy − An integer variable representing the y-derivative. (0 or 1). 1 when we want gradient in y-direction



from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('ronaldo.jpg', 0)

lap_img = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
# NOTE: As when converting to grayscale the slope becomes negative and of floating type so first we take the 
# absolute value to remove the signs and then convert the type from floating to uint8 which is required.
lap_img = np.uint8(np.absolute(lap_img))


sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0) # from left to right 
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1) # from top to bottom 

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))


title = ['Original Image', 'Laplacian Image', 'Sobelx Image', 'Sobely Image']
images = [img, lap_img, sobelx, sobely]

for i in range(len(images)):
    plt.subplot(2,2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
