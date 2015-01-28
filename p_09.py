import numpy as np 
import cv2
img = cv2.imread('Car.jpg', -1)
# Using cv2 split function
b, g, r = cv2.split(img)
print 'The blue channel.....'
cv2.imshow('Red Channel', r)
cv2.waitKey(2800)
# merging
img2 = cv2.merge((b,g,r))
print 'merged image'
cv2.imshow('merged image....', img2)
cv2.waitKey(2800)

# more efficient way using numpy
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

# chage all blue values to 255 and red values to 0
img[:, :, 0] = 255
img[:, :, 2] = 0
cv2.imshow('New', img)
cv2.waitKey(2800)