import cv2
import numpy as np 

# create VideoCapture Object with argument 0 to
# capture from camera one
cap = cv2.VideoCapture(0)

while(True):

	# capture frame by frame
	# ret holds True or False depending on wether frame is captured
	ret, frame = cap.read()
	# convert to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# display the resulting frame
	cv2.imshow('frame captured', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()		