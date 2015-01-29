import numpy as np 
import cv2
img = cv2.imread('Car.jpg', -1)
# print total number of pixels
print img.shape
# Save the pixels within the row and colmn index
crop = img[0:30, 0:44]
print crop.shape
cv2.imshow('croped', crop)
cv2.waitKey(3000)
cv2.destroyAllWindows()
# change the value of the existing pixels with the value in the crop
img[44:74, 44:88] = crop
cv2.imshow('Croped and merge', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

