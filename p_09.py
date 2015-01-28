import numpy as np 
import cv2
img = cv2.read('Car.jpg', -1)
# Using cv2 split function
b, g, r = cv2.split(img)
print 'The blue channel.....'
cv2.imshow('Blue Channel', b)
