import cv2
import numpy
img=cv2.imread('try.png')
img=10*floor(img/10)
x,y,r=img.shape
a=numpy.ndarray(shape=(255,255,255))
color=[]
tr = 0
count=0
for r in range(x) :
	for b in range(y):
		R=img[r][b][0]
		G=img[r][b][1]
		B=img[r][b][2]
		a[R][G][B]=1
		count=count+1


for r in range(255):
	for b in range(255):
		for c in range(255):
			if(a[r][b][c]==1): 
				tr=tr+1
			count=count+1
			print(count)
print('no.of colours',tr)
