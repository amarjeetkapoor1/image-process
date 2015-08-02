'''importing basic libraries'''
import cv2
import numpy as np
'''importing our own module''' 
import get
def CallBackFunc(event, x, y,flags,userdata):
	print(x,y)

'''main program'''
'''initializing video object '''
cap = cv2.VideoCapture(0)
''' while which is always true'''
while(1):
	#reading image of video in frame
	q,frame = cap.read()
	#getting binary image
	binary=get.getcolor(frame,'Red')
	#identifying shape from binary image and plotting it on original image 
	f,r=get.getshape(binary,frame,'circle')
	#displaying image for ms
	cv2.namedWindow("frame", 1);
	
	cv2.setMouseCallback("frame", CallBackFunc)
	cv2.imshow('frame',f)
	k = cv2.waitKey(2)
	#checking condition if esc is press exit 
	if k == 27:
		break
#destroy window
cv2.destroyAllWindows()
