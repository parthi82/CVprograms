import cv2

cap = cv2.VideoCapture(0)
ret = cap.set(3,320)
ret = cap.set(4,240)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('frame', gray)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()