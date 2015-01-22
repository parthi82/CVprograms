import cv2
import numpy as np 

# Load Image as GrayScale
img = cv2.imread('Car.jpg', 0)
# display Image
cv2.imshow('Car', img)
# wait for 2000 milliseconds
cv2.waitKey(2000)
# destroy the window name car
cv2.destroyWindow('Car')