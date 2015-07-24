import cv2
import numpy
from matplotlib import image
img=cv2.imread('sred.png')
img1=img
img=cv2.blur(img,(21,21))
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
print(value_colors,no_colors)
print(len(value_colors))
first=0
second=0
max=[]
b=-1
min=[]
c=5
for third in no_colors:
	if(second>=first and second>third and c!=1):
		max.append(value_colors[b])
		c=1
	if(second<=first and second<third and c!=0):
		min.append(value_colors[b])
		c=0
	first=second
	second=third
	b=b+1
if(second>first):
	max.append(value_colors[b])
else:
	max.append(value_colors[b])
print(len(min),len(max))
x,y=a.shape
img=img.astype('uint8')
print(len(min),len(max))
min.append(255255256)
max.append(255255255)
max=set(max)
max=list(max)
max.sort()
min=set(min)
min=list(min)
min.sort()
print(min,max)
for xx in range(x):
	for yy in range(y):
		for b in min:
			if(a[xx][yy]<b):
				img[xx][yy][1]=int(max[min.index(b)-1]/1000)%1000
				img[xx][yy][2]=max[min.index(b)-1]/1000000
				img[xx][yy][0]=max[min.index(b)-1]%1000
				break

img=img.astype('uint8')
print(img)
cv2.imshow('sreddd.png',img)
cv2.imshow('sred.png',img1)
cv2.waitKey(0)



