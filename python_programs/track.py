# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2


final=list()
camera = cv2.VideoCapture(0)

# initialize the first frame in the video stream
firstFrame = None
# loop over the frames of the video
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
	(grabbed, frame) = camera.read()
	text = "Unoccupied"
 
	# if the frame could not be grabbed, then we have reached the end
	# of the video
	if not grabbed:
		break
 
	# resize the frame, convert it to grayscale, and blur it
	#frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue
	# compute the absolute difference between the current frame and
	# first frame
	frameDelta = abs(firstFrame-gray)
	thresh=frameDelta
	#thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
 
	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	print("new")
 	d=0
	# loop over the contours
	[a,b]=gray.shape
	for c in cnts:
		d=d+1
		print(cv2.contourArea(c))
		if(d==1):
			continue
	
		# if the contour is too small, ignore it
		#if cv2.contourArea(c) < area :
		#	continue
 		
 		
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"
			# draw the text and timestamp on the frame
	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
	# show the frame and record if the user presses a key
	cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key is pressed, break from the lop
	if key == ord("q"):
		break
 
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()

'''def prospect(image):
	global point_contour
	maxx=[]
	max_area=0
	for a in point_contour:
		if(cv2.counterArea(a)>max_area and len(a) == 8):
			max_area=cv2.counterArea(a)
			maxx=a
	point=[]
	for a in range(len(point)):
		pts.append((point[a][0][0],point[a][0][1]))
	pts=np.array(point)
'''
