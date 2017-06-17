import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt
import sys

def getshape(binary,orignal):
	global point_contour
	point_contour =[]
	i, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	x,y=binary.shape
	bl= np.zeros((x,y,3), np.uint8)
	for a in contours :
		epsilon = 0.02*cv2.arcLength(a,True)
		approx = cv2.approxPolyDP(a,epsilon,True)
		point_contour.append(approx)
		x,y=binary.shape
		i=255*np.random.random_sample()
		cv2.drawContours(bl,[a],0, (int(i),int(i),int(i)), -1)
		cv2.drawContours(bl,[a],0, (int(0),int(0),int(0)), 3)
	return bl,contours
	
	
if __name__=='__main__':
    if len(sys.argv)==2:
        im = cv2.imread(sys.argv[1])
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        #canny edge detection is not as useful as threshold_binary
        edges = cv2.Canny(imgray,100,200)
        ret, thresh = cv2.threshold(imgray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        kernel = np.ones((5,5), np.uint8)

        """
        img_d = cv2.dilate(edges, kernel, iterations=1)
        kernel = np.ones((4,4), np.uint8)
        img_d = cv2.erode(img_d, kernel, iterations=1)
        """

        a, b = getshape(thresh,im)

        a = cv2.erode(a, kernel, iterations=3)
        a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        #print count_colors.count_color(a)
        x,y=a.shape
        color=[]
        tr = -1
        count=0
        for r in range(x) :
	        for b in range(y):
		        color.append(a[r][b])
	
        color.sort()

        b=0

        for r in color:
	        if(tr!=r):
		        count=count+1
		        tr=r
		
        print "No of polygon",count-1


        cv2.imwrite('na.png',a)
        cv2.imwrite('na1.png',thresh)
        #cv2.imwrite('ne.png',edges)
        #cv2.imwrite('nd.png',img_d)
