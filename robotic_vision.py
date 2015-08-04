import cv2
import get
img=cv2.imread('/home/amarjeet/a.png')
c=get.getcolor(img,raw_input('Red ,Voilet,Yellow,Voilet,Green'))
d,e=get.getshape(c,img,raw_input('circle ,triangle,square'))
cv2.imwrite('reee.png',d)

