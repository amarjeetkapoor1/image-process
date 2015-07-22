import cv2
import numpy as np
import scipy.ndimage as sy
import matplotlib.pylab as py
from skimage.measure import regionprops


def getshape(binary,orignal,shape):
	r,w=sy.measurements.label(binary)
	print(w)
	pro=regionprops(r,img)
	cmax={'circle':1,'square':0.829999,'triangle':0.793}
	cmin={'circle':0.80,'square':0.720,'triangle':0.30}
	xmax={'circle':0.90,'square':1,'triangle':0.70}
	xmin={'circle':0.70,'square':0.90,'triangle':0.30}
	print('circlularity' ,'extent', 'orientation','aspect ratio','eccentricity')
	for a in range(len(pro)):
		q=n(4*pi*pro[a].area/pro[a].perimeter^2)
		print(q , pro[a].extent, pro[a].orientation,pro[a].minor_axis_length/pro[a].major_axis_length,pro[a].eccentricity)
		if(q>=cmin[shape] and q <=cmax[shape] ):
			print(q)	
			minr, minc, maxr, maxc=pro[a].bbox
			cv2.rectangle(orignal,(int(minc),int(minr)),(int(maxc),int(maxr)),(int(1),int(1),int(1)),int(5))
			cv2.circle(orignal,(int(pro[a].centroid[1]),int(pro[a].centroid[0])),int(1),(int(1),int(1),int(1)),int(5))
	return orignal

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

def chroma(img):
	img=img.astype('float32')
	img=img**(22/10)
	b,g,r=cv2.split(img)
	Y=r+b+g
	R=r/Y
	G=g/Y
	B=b/Y
	return cv2.merge([B,G,R])
	
def getcolor(img,color):
	img=chroma(img)
	img=img*255
	img=img.astype('uint8')	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	input=readtxt(color)
	lower_color = np.array([input[0],input[1],input[2]])
	upper_color = np.array([input[3],input[4],input[5]])
	mask = cv2.inRange(hsv, lower_color, upper_color)
	kernal=np.ones((11,11),np.uint8)
	c=cv2.morphologyEx( mask, cv2.MORPH_OPEN,kernal)
	kernal=np.ones((11,11),np.uint8)
	c=cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernal)
	if(color == 'Red'):
		d=getcolor(img,'Red1')
		c=d+c
	return c
		


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
		cv2.circle(img1,(int(pro[a].centroid[1]),int(pro[a].centroid[0])),int(5),(int(a),int(b),int(c)))		
	return H

def readtxt( name ):
	file = open('/home/amarjeet/projects/imageprocess/getcolor.txt')	
	a = file.readlines()
	d=[]
	print(a)
	for c in a:
		print(c)
		c = c.split(' ' or '/n')
		c=list(c)
		if c[0] == name :
			for e in range(len(c)):
				print(c)
				if(c[e].isdigit()):
					d.append(int(c[e]))
			print(d)
			return d





