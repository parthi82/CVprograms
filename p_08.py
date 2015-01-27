import numpy as np 
import cv2
img = cv2.imread('Car.jpg', -1)
print img.shape
crop = img[0:30, 0:44]
print crop.shape
cv2.imshow('croped', crop)
cv2.waitKey(3000)
cv2.destroyAllWindows()
img[44:74, 44:88] = crop
cv2.imshow('Croped and merge', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

