import cv2
import numpy as np 

# create VideoCapture Object by passing file name as parameter
cap = cv2.VideoCapture('flame.avi')

while(cap.isOpened()):

	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR_GRAY)
	cv2.imshow('test', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
cap.release()
cv2.destroyAllWindows()	    




