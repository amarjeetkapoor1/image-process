import cv2
import numpy as np
import getshape
cap = cv2.VideoCapture(0)
while(1):
	q,frame = cap.read()
	a=getshape.getcolor(frame,'Red')
	frame=getshape.getshape(a,frame,'circle')
	cv2.imshow('frame',frame)
	k = cv2.waitKey(0)
	if k == 27:
		break
cv2.destroyAllWindows()
