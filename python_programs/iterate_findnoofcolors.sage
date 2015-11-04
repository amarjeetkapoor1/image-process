import cv2
import numpy
img=cv2.imread('shapes.png')
img=10*floor(img/10)
img.astype('uint8')
x,y,r=img.shape
a=numpy.ndarray(shape=(x,y))
a=(img[:,:,0]+1000*img[:,:,1]+1000000*img[:,:,2])
a.astype('int')
x,y=a.shape
color=[]
tr = 0
count=0
for r in range(x) :
	for b in range(y):
		for f in color:
           		if(a[r][b]==f):
               			count=count+1
			else:
				tr=tr+1
		print(tr)
       		if(count==0):
           		color=[a[r][b]]+color
	 	else:
     			count=0
count=0
for f in color: 
	count=count+1
print('no.of colours',count,tr)
