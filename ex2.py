import cv2
import numpy as np
# load image as grayscale
img = cv2.imread('Car.jpg', 0)
cv2.imshow('car', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print 'Saving the image as png'
# sve image as a PNG image
cv2.imwrite('Car.png',img)

    
