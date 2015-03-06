from cv2 import *
import numpy as numpy

def rgbfilter(image):
	'''
	This is a color filter based on a method proposed in "Fire Detection Using Statistical
	Color Model in Video Sequences" by Turgay Celik, Hasan Demeril, Huseyin Ozkaramanli, Mustafa Uyguroglu

	This method uses the RGB color space and does three comparisons.
	The method returns true at any pixel that satisfies:
	red > green > blue
	red > red threshold (depends on amount of light in image)
	'''

	b,g,r = split(image)
	rt = 230
	gb = compare(g,b,CMP_GT)
	rg = compare(r,g,CMP_GT)
	rrt = compare(r,rt,CMP_GT)
	rgb = bitwise_and(rg,gb)
	
	return bitwise_and(rgb,rrt)

def rgbfilter2(image):
	""" 
	This is a simple threshold filter with experimental thresholds:
	r > rt (red threshold)
	g > gt (green threshold)
	b < bt (blue threshold)

	Night: rt = 0, gt = 100, bt = 140

	"""

	b,g,r = split(image)
	rt = 0
	gt = 100
	bt = 140
	ggt = compare(g,gt,CMP_GT)
	bbt = compare(b,bt,CMP_LT)
	rrt = compare(r,rt,CMP_GT)
	rgb = bitwise_and(ggt,bbt)
	
	return bitwise_and(rgb,rrt)

def labfilter(image):
	'''
	This is a filter based on a method proposed in "Fast and Efficient Method for Fire Detection
	Using Image Processing" by Turgay Celik

	This method uses the CIE L*a*b* color space and performs 4 bitwise filters
	The method returns true at any pixel that satisfies:
	L* > Lm* (mean of L* values)
	a* > am* (mean of a* values)
	b* > bm* (mean of b* values)
	b* > a*
	'''
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
	
	return bitwise_and(R12,R34)

def filter(filt):
	''' 
	Choice of filters:
	filt = 0 : only RGB Filter
	filt = 1 : only cieLAB Filter
	filt = 2 : both filters
	filt = 3 : RGB Filter 2
	filt = 4 : all
	'''

	if filt == 0:
		return rgbfilter(img)
	elif filt == 1:
		return labfilter(img)
	elif filt == 2:
		R1 = rgbfilter(img)
		R2 = labfilter(img)
		R = bitwise_and(R1,R2)
		return R
	elif filt == 3:
		return rgbfilter2(img)
	elif filt == 4:
		R1 = rgbfilter(img)
		R2 = labfilter(img)
        R3 = bitwise_and(R1,R2)
        R4 = rgbfilter2(img)
        return bitwise_and(R3,R4)	

img = imread('fire5.jpeg')
print filter.__doc__
c = int(raw_input('choose Filter:'))
o = filter(c)	
imshow('output', o)	
imshow('input', img)	
waitKey(0)
