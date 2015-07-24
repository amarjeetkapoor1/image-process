import cv2

def moment(img,q,p):
	x,y=img.shape
	d=0
	w=0
	v=0
	for xx in range(x):
		for yy in range(y):
			d=(xx**p)*(yy**q)*img[xx][yy]+d
			w=(xx)*img[xx][yy]+w
			v=(yy)*img[xx][yy]+v
	return w,v
