# To show the BGR channel names on the image window
# i.e. To show the colour code of the point at which the mouse pointer will be clicked 
from cv2 import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]   # 0 because in BGR 'B' is at the 0 index
        green = img[y, x, 1]
        red = img[y, x, 2]

        text_BGR = str(blue) + ' , ' + str(green) + ' , ' + str(red)

        cv2.putText(img, text_BGR, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)
        cv2.imshow('Window1', img)     # Throughout the same window name will go


img = cv2.imread('lena.jpg')
cv2.imshow('Window1' , img)     # Throughout the same window name will go

cv2.setMouseCallback('Window1' , click_event)     # Throughout the same window name will go


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()