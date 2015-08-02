import cv2
import numpy
from matplotlib import image
img=cv2.imread('try.png')
img=img.astype('uint8')
x,y,r=img.shape
img=img.astype('float32')
Y=img[:,:,0]+img[:,:,1]+img[:,:,2]
r=img[:,:,0]/Y
g=img[:,:,1]/Y
r=r*255
g=g*255
k=numpy.ones((5,5),numpy.float32)
img=cv2.filter2D(img ,-1 , k)

r=r.astype('uint8')
g=g.astype('uint8')
print(g,'\n')
g=g.astype('int')
a=(r+1000*g)
a=a.astype('int')

print(a,'\n')
x,y=a.shape
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
	b=0
	min=[]
	max_no=[]
	min_no=[]
	for third in no_colors:
		if(second>=first and second >third):
			max.append(value_colors[b-1])
			max_no.append(no_colors[b-1])
		if(second<=first and second<third):
			min.append(value_colors[b-1])
			min_no.append(no_colors[b-1])		
		first=second
		second=third
		b=b+1
		
	if(second>first):
		max.append(value_colors[b-2])
		max_no.append(no_colors[b-2])

	else:
		min.append(value_colors[b-2])
		max_no.append(no_colors[b-2])
	value_colors=max
	no_colors =max_no
	if(len(value_colors)<=20):
		break
min.sort()
min.pop()
min.append(255255)
print("\n")
print(min,value_colors)
