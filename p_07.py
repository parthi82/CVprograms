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
print 'pixel at (89,139) has BGR value : '
px = img[89,139] 
print px
print 'Pixel at (53,76) has BGR value : '
px = img[53,76]
print px
print 'The Blue value at (53,76) is '
print img [53,76,0]
print '''After changing the value of blue to 255,
         The pixel at (53,76) becomes : '''
img[53,76,0] = 255
print img[53,76]

for i in range(40,52):
	for j in range(63):
		img[i,j,0] = 255

print 'Yes, see the image !'     
cv2.imshow('Car', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
