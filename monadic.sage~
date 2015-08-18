import cv2

#bright image
def bright(img,n):
	size=img.shape
	imgB=img+n
	for a in range(size[0]):
		for b in range(size[1]):
				if(len(size)==3):
					if (imgB[a][b][0]<n or 
						imgB[a][b][1]<n or 
						imgB[a][b][2]<n ):
						
						imgB[a][b]=255
				else:
					if(imgB[a][b]<n):
						imgB[a][b]=255
	return imgB

#negative image
def negative(img):
	imgB=1-img
	return imgB

#contrasting image.
def contrast(img,n):
	img=img.astype('float32')
	imgB=img*n
	size=img.shape
	for a in range(size[0]):
		for b in range(size[1]):
			if(len(size)==3):
				if(imgB[a][b][0]>255 or imgB[a][b][1]>255 or 
				imgB[a][b][2]>255):			
					imgB[a][b]=255
			else:
				if(imgB[a][b]>255 ):
					imgB[a][b]=255
	imgB=imgB.astype('uint8')
	return imgB
		

#posterisation image
def posterisation(img):
	n=int(input('posterisation level'))
	imgB=n*floor(img/n)
	imgB=imgB.astype('uint8')
	return imgB


