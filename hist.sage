import cv2
import numpy
from matplotlib import image
img=cv2.imread('sred.png')
img=img.astype('uint8')
x,y,r=img.shape
img=cv2.blur(img,(7,7))
img=img.astype('float32')
Y=img[:,:,0]+img[:,:,1]+img[:,:,2]
R=img[:,:,0]/Y
G=img[:,:,1]/Y
R=R*255
G=G*255
R=R.astype('uint8')
G=G.astype('uint8')
a=numpy.ndarray(shape=(x,y))
a=(R+1000*G)
a=a.astype('int')
x,y=a.shape
color=[]
tr = -1
count=0
for r in range(x) :
	for b in range(y):
		color.append(a[r][b])
	
color.sort()
print(color)
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
print(value_colors)
print(count)
first=0
second=0
max=[]
b=-1
min=[]
for third in no_colors:
	if(second>=first and second >third):
		max.append(value_colors[b])
	if(second<=first and second<third):
		min.append(value_colors[b])
	first=second
	second=third
	b=b+1
if(second>first):
	max.append(value_colors[b])
else:
	max.append(value_colors[b])
print(len(min),len(max))


