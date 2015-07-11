import cv2
import numpy as np
import scipy.ndimage as sy
import matplotlib.pylab as py
from skimage.measure import regionprops


def getshape(binary,orignal,shape):
	r,w=sy.measurements.label(binary)
	pro=regionprops(r)
	cmax={'circle':1,'square':0.829999,'triangle':0.793}
	cmin={'circle':0.80,'square':0.720,'triangle':0.30}
	xmax={'circle':0.91,'square':1,'triangle':0.79}
	xmin={'circle':0.79,'square':0.89,'triangle':0.30}
	for a in range(len(pro)):
		q=n(4*pi*pro[a].area/pro[a].perimeter^2)
		print(q , pro[a].extent, pro[a].eccentricity)
		if(q<=cmax[shape] and q>=cmin[shape] and pro[a].extent>=xmin[shape] and pro[a].extent <=xmax[shape] ):
			print(q)	
			minr, minc, maxr, maxc=pro[a].bbox
			cv2.rectangle(orignal,(int(minc),int(minr)),(int(maxc),int(maxr)),(int(1),int(1),int(1)))
			cv2.circle(orignal,(int(pro[a].centroid[1]),int(pro[a].centroid[0])),int(5),(int(1),int(1),int(1)))
	return orignal

def getcolor (img,color,n=0.44):
	n=float(n)
	img=img.astype('float32')
	img=img**(22/10)
	b,g,r=cv2.split(img)
	Y=r+b+g
	R=r/Y
	G=g/Y
	B=b/Y
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
	kernal=np.ones((50,50),np.uint8)
	c=cv2.morphologyEx( c, cv2.MORPH_OPEN,kernal)
	c=cv2.morphologyEx( c, cv2.MORPH_CLOSE,kernal)
	return c





