# Printing and Changing the width & Height of the video frame 
from cv2 import cv2

cap = cv2.VideoCapture(0)

# Printing the width of the window
print("\n Width of window:")
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(3))  # The Id for Width is 3 so we can 3 to find the width directly

# Printing the height of the window
print("\n Height of window:")
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(4))  # The Id for Height is 4 so we can 4 to find the width directly

# Setting the new Width and Height to the window
cap.set(3,1280) # New Width
cap.set(4,720) # New Height

# Printing the new width and new height of the window
print('\n +++++++++++++++++++++++++++++ \n')
print(cap.get(3))  # Width
print(cap.get(4))  # Height



while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('window', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
