import cv2
import numpy as np 
# read image
img = cv2.imread('Car.jpg', 0)
# show image
cv2.imshow('Car', img)
# wait indefinitely until a key is pressed
k = cv2.waitKey(0)
# if ESC key is pressed exit
if k == 27:
    cv2.destroyAllWindows()
else:
    # if 's' is pressed save image and exit
    cv2.imwrite('Car.bmp', img)
    cv2.destroyAllWindows()
    