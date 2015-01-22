import numpy as np 
import cv2
from matplotlib import pyplot as plt 
# load image
img = cv2.imread('Car.jpg', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()