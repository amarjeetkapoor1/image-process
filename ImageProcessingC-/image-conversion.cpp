#include "opencv2/highgui/highgui.hpp"
#include<iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
	IplImage* img = cvLoadImage(argv[1]);
	
	cvSaveImage( argv[2], img);
	cvReleaseImage( &img);

	return 0;
}
