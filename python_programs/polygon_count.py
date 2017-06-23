import numpy as np
import cv2
import sys

"""
Time complexity depends upon shape of image

"""

def getfilledpoly(binary):

    #Get contours
    not_used, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #Get shape of binary image to create a blank image of same size
    x, y = binary.shape
    filledPolygon = np.zeros((x,y,3), np.uint8)

    #Fill the polygons
    color = 0

    #Iterat over all contoures starting from innermost
    for cont in contours :

        #Check color to  be used is range
        if(color>=255):
            color=0

        #Increment color or change color
        color=color+1

        #Fill the contour with given color
        cv2.drawContours(filledPolygon,[cont],0, (int(color),int(color),int(color)), -1)

        #Draw border of contour and this is important if the polygon is open
        #Its previous color used to fill area will be replaced with (0,0,0)
        #as area of contour will be equal to its border
        cv2.drawContours(filledPolygon,[cont],0, (int(0),int(0),int(0)), 3)

    return filledPolygon


if __name__=='__main__':
    if len(sys.argv)==2:

        #Get Image
        im = cv2.imread(sys.argv[1])

        #Convert to gray scale
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        #Get binary image
        no_use, thresh = cv2.threshold(imgray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        #Get image where polygons are filled
        filled_polygon = getfilledpoly(thresh)
        cv2.imwrite('filledpolygon.png',filled_polygon)

        #For safty remove holes
        kernel = np.ones((5,5), np.uint8)
        filled_polygon = cv2.erode(filled_polygon, kernel, iterations=3)
        filled_polygon = cv2.cvtColor(filled_polygon, cv2.COLOR_BGR2GRAY)

        #find size of matrix of image 
        row, column=filled_polygon.shape
        color=[]

        #Count number of unique colors
        for rowPixel in range(row) :
            for columnPixel in range(column):
                if filled_polygon[rowPixel][columnPixel] not in color:
                    color.append(filled_polygon[rowPixel][columnPixel])

        print "No of polygon",len(color)-1

        cv2.imwrite('imageAfterthreshing.png',thresh)
