import cv2
import numpy as np 
img = cv2.imread('Car.jpg')
print 'The Dimensions in the Image : '
print img.ndim
print 'The Shape of the Image : '
print img.shape
print 'The array of the Image : '
print img
print 'The data type of the Image array : '
print img.dtype
print 'The length of the first dimension of the Image : '
print len(img)
