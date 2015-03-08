from cv2 import *
import cv2
import numpy as np

image = imread('can.jpg')
b = image[:, :, 0]
g = image[:, :, 1]
r = image[:, :, 2]
gb = compare(g,b,CMP_GT)
rg = compare(r,g,CMP_GT)
rrt = compare(r,230,CMP_GT)
rgb = bitwise_and(rg,gb)
rgbrt = bitwise_and(rgb,rrt)

cieLab = cvtColor(image,COLOR_BGR2LAB)
L,a,b = split(cieLab)
Lm = mean(L)
am = mean(a)
bm = mean(b)
R1 = compare(L,Lm,CMP_GT)
R2 = compare(a,am,CMP_GT)
R3 = compare(b,bm,CMP_GT)
R4 = compare(b,a,CMP_GT)
R12 = bitwise_and(R1,R2)
R34 = bitwise_and(R3,R4)
R1234 = bitwise_and(R12,R34)

R = bitwise_and(R1234,rgbrt)
Rf = cv2.bilateralFilter(R, 10, 17, 17)
#edged = cv2.Canny(Rf, 30, 200)
_, cnts, _ = cv2.findContours(Rf.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

'''areas = [cv2.contourArea(c) for c in cnts]
max_index = np.argmax(areas)
cnt=cnts[max_index]'''
print len(cnts)


for c in cnts:
	if (cv2.contourArea(c) > 100):
		print 'fire detected'
		cv2.drawContours(image, [c], -1, (0, 255, 0), 3)
	else: 
	    print 'No Fire detected'	
imshow("Image", image)
imshow('Rf', Rf)
waitKey(0)
#imshow('image',R)
#waitKey(0) 
