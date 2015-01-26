import cv2
import numpy as np 

print 'Lets load the image "Car.jpg"'
img = cv2.imread('Car.jpg')
cv2.imshow('Car.jpg', img)
cv2.waitKey(3500)
cv2.destroyAllWindows()

print 'No. of Dimensions in the Image : '
print img.ndim

print 'The Shape of the Image : '
print img.shape

print 'The array of the Image : '
print img

print 'The data type of the Image array : '
print img.dtype

print 'The length of the first dimension of the Image array : '
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

print '''Now, lets change the Blue value for all pixels at
positions 40 - 52 in the first dimension and at 
positions 63 - 75 in second dimension of the Image'''
for i in range(40,52):
	for j in range(63,75):
		img[i,j,0] = 255
		
print 

print 'Yes, See the image !'     
cv2.imshow('Car', img)
cv2.waitKey(3500)
cv2.destroyAllWindows()
