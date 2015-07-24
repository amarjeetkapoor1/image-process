import cv2
import getshape 
img=cv2.imread('pictures/shapes.png')
img1=img.astype('float')
c=getshape.getcolor(img1,'Yellow')
d=getshape.getshape(c,img,'triangle')
cv2.imwrite('pictures/reee.png',d)
img1=cv2.imread('pictures/reee.png')
print(img1.dtype)
