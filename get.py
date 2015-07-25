'''libraries to be imported '''
import cv2
import numpy as np
import scipy.ndimage as sy
import matplotlib.pylab as py
from skimage.measure import regionprops
import os

#function to find blob of particular shape in binary image
''' getshape take three paramter binary image, orignal image and 
shape which is to be found'''
def getshape1(binary,orignal,shape):
	r,w=sy.measurements.label(binary)
	print(w)
	pro=regionprops(r)
	cmax={'circle':1,'square':0.84999,'triangle':0.71}
	cmin={'circle':0.85,'square':0.720,'triangle':0.30}
	emax={'circle':0.90,'square':1,'triangle':0.70}
	emin={'circle':0.70,'square':0.90,'triangle':0.30}
	print('circlularity' ,'extent', 'orientation','aspect ratio',
	'eccentricity')
	for a in range(len(pro)): 
			q=(4*22*pro[a].area)/(7*(pro[a].perimeter**2))
			print(q,pro[a].extent, pro[a].orientation,pro[a].eccentricity)
			if(q>=cmin[shape] and q<=cmax[shape] ):
				minr, minc, maxr, maxc=pro[a].bbox
				cv2.rectangle(orignal,(minc,minr),(maxc,maxr),(1,1,1),5)
				cv2.circle(orignal,
				(int(pro[a].centroid[1]),int(pro[a].centroid[0])),
				1,(1,1,1),5)
	return orignal

#function to find blob of particular shape in binary image using contours
def getshape(binary,orignal,shape):
	contours, hierarchy = cv2.findContours(
	binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cmax={'circle':16,'square':8,'triangle':6}
	for a in contours :
		epsilon = 0.02*cv2.arcLength(a,True)
		approx = cv2.approxPolyDP(a,epsilon,True)
		print(approx.size)
		if (approx.size == cmax[shape]):
			cv2.drawContours(orignal,[a],0, (int(40),int(255),int(25)), 3)	
	return orignal,contours

'''function to find basic RGB color in image using threshold'''
def getcolor1 (img,color,n=0.44):
	n=float(n)
	img=chroma(img)
	B,G,R=cv2.split(img)
	if(color=='red'):
		c=R>n
		c=c*255
	if(color=='green'):
		c=G>n
		c=c*255
	if(color=='blue'):
		c=B>n
		c=c*255
	c=c.astype('uint8')
	kernal=np.ones((7,7),np.uint8)
	c=cv2.morphologyEx( c, cv2.MORPH_OPEN,kernal)
	c=cv2.morphologyEx( c, cv2.MORPH_CLOSE,kernal)
	return c
'''function to find chromatacity of image'''

def chroma(img):
	img=img.astype('float32')
	img=img**(22/10)
	b,g,r=cv2.split(img)
	Y=r+b+g
	R=r/Y
	G=g/Y
	B=b/Y
	return cv2.merge([B,G,R])

''' function to find colors in image using HSV'''	
def getcolor(img,color):
	a=chroma(img)
	a=a*255
	a=a.astype('uint8')	
	hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
	input=readtxt(color)
	lower_color = np.array([input[0],input[1],input[2]])
	upper_color = np.array([input[3],input[4],input[5]])
	mask = cv2.inRange(hsv, lower_color, upper_color)
	kernal=np.ones((33,33),np.uint8)
	c=cv2.morphologyEx( mask, cv2.MORPH_OPEN,kernal)
	kernal=np.ones((5,5),np.uint8)
	c=cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernal)
	if(color == 'Red'):
		d=getcolor(img,'Red1')
		c=d+c
	return c
		

'''function to find homography points for making homograpy matrix'''
def gethomograph(img1):
	c=getcolor(img1,'blue',0.45)
	r,w=sy.measurements.label(c)
	pro=regionprops(r)
	H=np.ones((9, 2), dtype=np.float32)
	b=0
	c=0
	for a in range(len(pro)):
		q=n(4*pi*pro[a].area/pro[a].perimeter^2)
		H[a][0]=pro[a].centroid[0]	
		H[a][1]=pro[a].centroid[1]
		cv2.circle(img1,(int(pro[a].centroid[1]),int(pro[a].centroid[0]))
		,5,(a,b,c))		
	return H

'''function to read data of color from image'''
def readtxt( name ):
	file = open('getcolor.txt')	
	a = file.readlines()
	d=[]
	for c in a:
		c = c.split(' ' or '/n')
		c=list(c)
		if c[0] == name :
			for e in range(len(c)):
				if(c[e].isdigit()):
					d.append(int(c[e]))
			return d





