import cv2
import numpy
from matplotlib import image
img=cv2.imread('shapes.png',0)
img=img.astype('uint8')
x,y=img.shape
print(x,y)
a=img
a=a.astype('int')
color=[]
tr = -1
count=0
for r in range(x) :
	for b in range(y):
		color.append(a[r][b])
	
color.sort()
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
print(count)

max=[]
while(count!=0):
	first=0
	second=0
	max=[]
	b=-1
	min=[]
	max_no=[]
	min_no=[]
	for third in no_colors:
		if(second>=first and second >third):
			max.append(value_colors[b])
			max_no.append(no_colors[b])
		if(second<=first and second<third):
			min.append(value_colors[b])
			min_no.append(no_colors[b])		
		first=second
		second=third
		b=b+1
	if(second>first):
		max.append(value_colors[b])
		max_no.append(no_colors[b])

	else:
		min.append(value_colors[b])
		max_no.append(no_colors[b])
	value_colors=max
	no_colors =max_no
	if(len(value_colors)<=20):
		break
print(value_colors,min)
min.sort()
min.pop()
min.append(255)
x,y=img.shape
for r in range(x) :
	for b in range(y):
		for c in range(len(min)):
			if(img[r][b]<min[c]):
				img[r][b]=value_colors[c-1]
				break
cv2.imwrite('new.png',img)












