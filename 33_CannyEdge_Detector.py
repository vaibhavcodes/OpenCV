# Canny Edge Detector--> It is one of the most popular algorithms for edge detection.

# Noise and Edges re high frequency content.

# Noise Reduction - An edge detector is a high pass filter that enhances the high-frequency component and 
# suppresses the low ones. Since both edges and noise are high-frequency components, the edge detectors 
# tend to amplify the noise. To prevent this, we smooth the image with a low-pass filter. 
# Canny uses a `Gaussian filter` for this.

# We can see that some edges are more bright than others. The brighter ones can be considered as strong 
# edges but the lighter ones can actually be edges or they can be because of noise. 
# NOTE: To solve the problem of “which edges are really edges and which are not” Canny uses the Hysteresis 
# thresholding. In this, we set two thresholds ‘High’ and ‘Low’.

# --> Any edges with intensity greater than ‘High’ are the sure edges.
# --> Any edges with intensity less than ‘Low’ are sure to be non-edges.
# --> The edges between ‘High’ and ‘Low’ thresholds are classified as edges only if they are connected 
# to a sure edge otherwise discarded.

from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg', 0)

# Syntax: Canny(img, threshold_low, threshold_high)
canny = cv2.Canny(img, 100, 200)

images = [img, canny]
images_names = ['Original Image', 'Canny Image'] 

for i in range(2):
    plt.subplot(1,2, i+1)
    plt.imshow(images[i])
    plt.title(images_names[i])

plt.show()












