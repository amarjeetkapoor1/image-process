import cv2
import get
img=cv2.imread('/home/amarjeet/a.png')
c=get.getcolor(img,raw_input('Red ,Voilet,Yellow,Voilet,Green'))

#c=get.chroma(img)
#c=c*255
#c=c.astype('uint8')
#c=get.auto_canny(img)
d,e=get.getshape(c,img,raw_input('circle ,triangle,square'))
cv2.imwrite('reee.png',d)

