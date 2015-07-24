'''importing basic libraries'''
import cv2
import numpy as np
'''importing our own module''' 
import get

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
	frame=get.getshape(binary,frame,'circle')
	#displaying image for ms
	cv2.imshow('frame',frame)
	k = cv2.waitKey(2)
	#checking condition if esc is press exit 
	if k == 27:
		break
#destroy window
cv2.destroyAllWindows()
