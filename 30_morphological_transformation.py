# morphological transformation : It refers to the operations performed on the image shape. And these operations
# are mainly implemented on the binary gray scale images

# It basically removes the noise from the images. The most common ways of doing it is by  dilation and erosion:

# Dilation :--> It is used to remove the noise from inside the object i.e. It expands the shape. It is used for
#               growing features and filling gaps and holes.

# Erosion :--> It is used to remove the noise from outside the object i.e. It shrinks the the connected parts. It
#              is used for shrinking the boundaries of the features, removing bridges and branches. 

# The above two are performed by comparing the noise pixels with the kernel. If the size of the noise pixels are
# less than the size of kernel then it would get replace by the kernel or will get removed.

# Opening :--> Implementing erosion first and then the dilation

# Closing :--> Implementing dilation first and then the erosion

# Morphology Gradient --> It is difference between dilation and erosion. So we'll only the amount of expansion
# done by dilation


from cv2 import cv2
import numpy as np

# Our task here is to show only the balls(object) present in the below image by removing all the noise present
# inside as well as outside the balls
img = cv2.imread('smarties.png',0)

_ , mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
# We can see that there are lots of noise present in the masked image. Noise here are the black spots inside the
# balls and white spaces outside the balls and also few white spots between two balls 

# So lets now remove the noise from inside the image i.e. filling the gaps inside the image. 
# This is known as dilation.

kernel = np.ones( (2,2) , np.uint8)

dilated_img = cv2.dilate(mask , kernel, iterations=3)
# Iterations is used when we want to apply it one after other
# So here dilation will be applied 3 times one after the other.
# NOTE: If we will take size of the kernel large then it will start expanding the balls and will start getting 
# connected to other balls.


# So lets now remove the noise from outside the image i.e. shrinking the connected branches between two balls
# and also removing white spaces from outside the balls 
# This is known as erosion.
erosion_img = cv2.erode(mask , kernel, iterations=2)

opening_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

closing_img = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

morphological_gradient_img = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Original Image' , img)
cv2.imshow('Masked Image' , mask)
cv2.imshow('Dilated Image' , dilated_img)
cv2.imshow('Erosion Image' , erosion_img)
cv2.imshow('Opening Image' , opening_img)
cv2.imshow('Closing Image' , closing_img)
cv2.imshow('Morphological Gradient Image' , morphological_gradient_img)


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
