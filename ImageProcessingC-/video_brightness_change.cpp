//header files
#include "opencv2/highgui/highgui.hpp"
#include <iostream>

//namespaces
using namespace cv;
using namespace std;

int main()
{
	//open the video file for reading
	VideoCapture cap("videotest.mp4");

	//if not success, exit program
	if(!cap.isOpened())
	{
		cout<<"Cannot open th evideo file"<<endl;
//		return -1;
	}

	//create window
	namedWindow("Original Video", CV_WINDOW_AUTOSIZE);
	namedWindow("Brightness Increased", CV_WINDOW_AUTOSIZE);
	namedWindow("Brightness Decreased", CV_WINDOW_AUTOSIZE);

	while(1)
	{
		Mat frame;

		//read a new frame from video
		bool bSuccess = cap.read(frame);

		//if not success, break loop
		if(!bSuccess)
		{
			cout<<"Cannot read the frame from video file"<<endl;
			break;
		}

		//increase brightness by 50 units
		Mat frameH = frame + Scalar(50,50,50);

		//decrease the brightness by 50 units
		Mat frameL = frame + Scalar(-50,-50,-50);

		//show the frame in "Original Video" window
		imshow("Original Video", frame);
		//show the frame in "Brightness Increased" window
		imshow("Brightness Increased", frameH);
		//show the frame in "Brightness decreased" window
		imshow("Brightness Decreased", frameL);

		//wait for 'esc' key press for 30 ms. If 'esc' key is pressed, break loop
		if(waitKey(30)==27)
		{
			cout<<"esc key is pressed by user"<<endl;
			break;
		}
	}
//	return 0;
}
