import cv2

#bright image
def grayscacle(img,n):
	cc,rr,dd =img.shape
	n=input(" enter no. in range 0-255 ")
	imgB=img+n
	for a in range(cc):
		for b in range(rr):
				if (imgB[a][b][0]<n or imgB[a][b][1]<n or imgB[a][b][2]<n ):
					imgB[a][b]=255
	return imgB

#negative image
def negative(img):
	imgB=1-img
	cv2.imwrite('negative.png',imgB)

#contrasting image.
def contrast(img,n):
	img=img.astype('float32')
	imgB=img*n
	for a in range(cc):
		for b in range(rr):
			if(imgB[a][b][0]>255 or imgB[a][b][1]>255 or 
			imgB[a][b][2]>255):			
				imgB[a][b]=255
	return imgB
		

#posterisation image
def posterisation(img):
	n=int(input('posterisation level'))
	imgB=n*floor(img/n)
	imgB=imgB.astype('uint8')
	return imgB


