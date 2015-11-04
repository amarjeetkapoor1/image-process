'''libraries to be imported '''
import cv2
import numpy as np
import scipy.ndimage as sy
import matplotlib.pylab as py
from skimage.measure import regionprops
import os
import math

name=65
input=None
point_contour=[]

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
	global point_contour
	point_contour =[]
	contours, hierarchy = cv2.findContours(
	binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cmax={'circle':16,'square':8,'triangle':6}
	for a in contours :
		epsilon = 0.02*cv2.arcLength(a,True)
		approx = cv2.approxPolyDP(a,epsilon,True)
		point_contour.append(approx)
		x,y=binary.shape
		if (approx.size == cmax[shape] and 
			cv2.contourArea(a) > x*y/600 and  
			cv2.isContourConvex(approx)):
			mark_points(approx,orignal)
			cv2.drawContours(orignal,[a],0, (int(0),int(255),int(25)), 3)
	return orignal,contours

def mark_points(approx,image):
	global name
	for a in range(approx.size/2):
		color=image[approx[a][0][1],approx[a][0][0],:]
		cv2.putText(
					image,(chr(name)+str(a)),(approx[a][0][0]+3,approx[a][0][1]-3)
					,cv2.FONT_HERSHEY_SIMPLEX,0.70,
					(int(color[2]),int(color[1]),int(color[0])),3)
		cv2.circle(image,
				(approx[a][0][0],approx[a][0][1]),
				1,(int(color[2]),int(color[1]),int(color[0])),3)
	get_distance(approx)
	name=name+1
	if(name>122):
		name=65

#finding distance b/w points
def get_distance(approx):
	global name
	for a in range(approx.size/2):
			point1=chr(name)+str(a)
			if(a == (approx.size/2)-1):
				point2=chr(name)+str(0)
				print(
						'distance between points %s and %s is %f'%(point1,point2,
						math.sqrt((approx[a][0][0]-approx[0][0][0])**2+
						(approx[a][0][1]-approx[0][0][1])**2)))
			else:
				point2=chr(name)+str(a+1)
				print(
						'distance between points %s and %s is %f'%(point1,point2,
						math.sqrt((approx[a][0][0]-approx[a+1][0][0])**2+
						(approx[a][0][1]-approx[a+1][0][1])**2)))
'''
def get_angle(approx):
	for a in range(approx.size/2):
			print('no', a)
			if(a == (approx.size/2)-1):
				
			else:
'''			
					
'''function to find basic RGB color in image using threshold'''
def getcolor_basic (img,color,n=0.44):
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

def auto_canny(image, sigma=0.33):
	a = cv2.GaussianBlur(image, (7,7), 0)
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged
	
'''function to find chromatacity of image'''
def chroma(img):
	#change img datatype
	img=img.astype('float32')
	#grama correction applied
	img=img**(22/10)
	#split color channels
	b,g,r=cv2.split(img)
	#calculate chromaticity
	Y=r+b+g
	R=r/Y
	G=g/Y
	B=b/Y
	#returning merged image
	return cv2.merge([B,G,R])

'''function to find colors in image using HSV'''
def getcolor(img,color):
	a=chroma(img)
	a=a*255
	a=a.astype('uint8')	
	hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
	global input
	"""if(input == None):"""
	b=os.popen('locate -b \'\getcolor.txt\'')
	data=b.read()
	data=data.split('\n')
	input=readtxt(color,data[0])
	a = cv2.GaussianBlur(img, (7,7), 0)
	lower_color = np.array([input[0],input[1],input[2]])
	upper_color = np.array([input[3],input[4],input[5]])
	mask = cv2.inRange(hsv, lower_color, upper_color)
	kernal=np.ones((3,3),np.uint8)
	c=cv2.morphologyEx( mask, cv2.MORPH_OPEN,kernal)
	kernal=np.ones((17,17),np.uint8)
	c=cv2.morphologyEx(c, cv2.MORPH_CLOSE,kernal)
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
def readtxt (name,filename):
	file = open(filename)
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
			
'''function to threshold image'''

def threscolor(img,n):
	
	img_copy=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	img_copy=img_copy>n
	img_copy=img_copy*255
	return img_copy
'''
def order_points(pts):	
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")

	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	# return the ordered coordinates
	return rect

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))

	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))

	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	# return the warped image
	return warped
		
def prospect(image):
	global point_contour
	maxx=[]
	max_area=0
	for a in point_contour:
		if(cv2.counterArea(a)>max_area and len(a) == 8):
			max_area=cv2.counterArea(a)
			maxx=a
	point=[]
	for a in range(len(point)):
		pts.append((point[a][0][0],point[a][0][1]))
	pts=np.array(point)
	four_point_transform(image,pts)
'''	
