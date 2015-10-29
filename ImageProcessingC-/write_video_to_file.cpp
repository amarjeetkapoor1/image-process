//library files
#include "opencv2/highgui/highgui.hpp"
#include <iostream>

//namespaces
using namespace cv;
using namespace std;

int main()
{
	//open the video camera no. 0
	VideoCapture cap(0);

	//if not success, exit program
	if(!cap.isOpened())
	{
		cout<<"Error: Cannot open the video file"<<endl;
		return -1;
	}

	//create a window called "MyVideo"
	namedWindow("MyVideo",CV_WINDOW_AUTOSIZE);

	//get the width of frames of the video
	double dWidth = cap.get(CV_CAP_PROP_FRAME_WIDTH);

	//get the height of frames of the video
	double dHeight = cap.get(CV_CAP_PROP_FRAME_HEIGHT);

	cout<<"Frame Size="<<dWidth << "x" << dHeight << endl;

	//casting double to int, because by default value is in double but frame Size accepts int values only
	Size frameSize(static_cast<int>(dWidth), static_cast<int>(dHeight));

	//initialize the VideoWriter object
	VideoWriter oVideoWriter("MyVideo.avi", CV_FOURCC('P','I','M','1'), 20, frameSize, true);

	//if not initialized the VideoWriter successfully, exit the program
	if(!oVideoWriter.isOpened())
	{
		cout<<"Error: Failed to write the video"<<endl;
		return -1;
	}

	while(1)
	{
		Mat frame;

		//read a new frame from video 
		bool bSuccess = cap.read(frame);

		//if not success, break loop
		if(!bSuccess)
		{
			cout<<"Error: Cannot read a frame from video file"<<endl;	
			break;
		}

		//write the frame into the file
		oVideoWriter.write(frame);

		//show the frame in "MyVideo" window
		imshow("MyVideo", frame);

		//wait for 'esc' key press for 30ms. If 'esc' key is pressed, break loop
		
		if(waitKey(10) == 27)
		{
			cout<<"esc key is pressed by user"<<endl;
			break;
		}
	}
	return 0;
}
