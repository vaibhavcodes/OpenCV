# Make different shapes on image
from cv2 import cv2

img = cv2.imread('lena.jpg', 1)

img = cv2.line(img, (0,0), (160,160), (0,255,0), 10)  # Make a line

img = cv2.arrowedLine(img, (0,0), (100,100), (0,0,255), 10) # Make an arrowed line

img = cv2.rectangle(img, (180,180), (400,400), (255,0,0), 7) # Produce a rectangle

img = cv2.circle(img, (290,290), 100, (255,255,0), -1) # Produce a circle

# Note: If in above thickness=-1 is put then it will cover the whole figure as in case of circle

# Writing a text on the image
img = cv2.putText(img, "HOTT Sensation!!", (10,450), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

cv2.imshow('window1' , img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()