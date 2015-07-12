import cv2
import numpy
from matplotlib import image

def count_color(img):
	img=img.astype('int')
	a=(img[:,:,0]+1000*img[:,:,1]+1000000*img[:,:,2])
	a=a.astype('int')
	x,y=a.shape
	color=[]
	tr = 0
	count=0
	for r in range(x) :
		for b in range(y):
			color.append(a[r][b])
	color.sort()
	no=0
	no_colors=[]
	value_colors=[]
	b=0
	c=0
	for r in color:
		if(tr!=r):
			count=count+1
			value_colors.append(tr)
			no_colors.append(b)
			tr=r
			b=0
		b=b+1
	no_colors.append(b)
	value_colors.append(tr)
	return no_colors , value_colors


