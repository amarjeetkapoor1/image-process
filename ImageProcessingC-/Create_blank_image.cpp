//header files

#include "opencv2/highgui/highgui.hpp"
#include<iostream>

using namespace cv;
using namespace std;

int main()
{
	Mat img(500, 1000, CV_8UC3, Scalar(100,0,0));  //create an image (3 channels, 8 bit image depth, 500 high, 1000 wide, (0,0,100) assigned for Blue, Green and Red plane respectively.)

	namedWindow("MyWindow", CV_WINDOW_AUTOSIZE);   //create a window with the name "MyWindow"

	imshow("MyWindow", img);   //display the image which is stored in the 'img' in the "MyWindow" window

	waitKey(0);   //wait infinite time for a keypress

	destroyWindow("MyWindow");   //destroy the window with the name, "MyWindow"

	return 0;
}
