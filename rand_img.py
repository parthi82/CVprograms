import cv2
import numpy as np

a = np.random.rand(256, 256)
cv2.imshow('Random Image', a)
cv2.waitKey()
cv2.destroyWindow('Random Image')