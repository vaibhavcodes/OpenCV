# How to install opencv in windows:
# Step-1: Install python
# Steo-2: in cmd write: pip install opencv-python
# after installing in cmd only type python and then import cv2. If no error comes means it has been 
# installed properly


# Playing with images from the local machine

from cv2 import cv2

img = cv2.imread('lena.jpg', 1)   # 1 represent the coloured image, 0 represents the gray scale image

cv2.imshow ('vaibhav', img)  # vaibhav is the window name

keyvalue = cv2.waitKey(0)  # To capture the users input of the keyboard key


if keyvalue == 27:   # 27 is the ASCII value of esc key
    cv2.destroyAllWindows()

elif keyvalue == ord('s'):     # ord('s') will give the ASCII value of small 's' key
    cv2.imwrite('Copy.png' , img)  # saving of image
    cv2.destroyAllWindows()


