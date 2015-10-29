//header files
#include "opencv2/highgui/highgui.hpp"
#include <iostream>

//namespaces
using namespace cv;
using namespace std;

int main()
{
	Mat img = imread("test.jpg", CV_LOAD_IMAGE_COLOR);

	if(img.empty())
	{
		cout<<"Image cannot be loaded."<<endl;
		return -1;
	}

	//increase the brightness by 75 units
	Mat imgH;// = img + Scalar(75,75,75);
	img.convertTo(imgH,-1,2,0);

	//decrease brightness by 75 units
	Mat imgL;// = img + Scalar(-50,-50,-50);
	img.convertTo(imgL, -1,0.5,-5);

	namedWindow("Original Image", CV_WINDOW_AUTOSIZE);
	namedWindow("High Brightness", CV_WINDOW_AUTOSIZE);
	namedWindow("Low Brightness", CV_WINDOW_AUTOSIZE);

	imshow("Original Image", img);
	imshow("High Brightness", imgH);
	imshow("Low Brightness", imgL);

	waitKey(0);

	//destroy open windows
	destroyAllWindows();

	return 0;
}
