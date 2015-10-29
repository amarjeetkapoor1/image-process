// Header Files
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include<iostream>

//using namespaces
using namespace cv;
using namespace std;

int main()
{
	//open and read the image
	Mat img = imread("test.jpg", CV_LOAD_IMAGE_COLOR);

	if(img.empty())
	{
		cout<<"image cannot be loaded..!!"<<endl;
	}

	//change the color image to grayscale image
	cvtColor(img, img, CV_BGR2GRAY);

	Mat img_hist_equalized;
	//equalize the histogram
	equalizeHist(img, img_hist_equalized);

	//create windows
	namedWindow("Original Image", CV_WINDOW_AUTOSIZE);
	namedWindow("Histogram Equalized", CV_WINDOW_AUTOSIZE);

	//show the image
	imshow("Original Image", img);
	imshow("Histogram Equalized", img_hist_equalized);

	//wait fot the key press
	waitKey(0);

	//destroy all open windows
	destroyAllWindows();

	return 0;
}
