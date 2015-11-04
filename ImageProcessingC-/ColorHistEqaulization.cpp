//header files 
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>

//using namespaces
using namespace cv;
using namespace std;

int main()
{
	//open and read the image
	Mat img = imread("test.jpg", CV_LOAD_IMAGE_COLOR);
	
	//if unsuccessful, exit the program
	if(img.empty())
	{
		cout<<"Image cannot be loaded"<<endl;
	}

	vector<Mat> channels;
	Mat img_hist_equalized;

	//change the color of image from BGR to YCrCb	
	cvtColor(img, img_hist_equalized, CV_BGR2YCrCb);

	//split the image into channels
	split(img_hist_equalized, channels);

	//equalize histogram on the 1st channel (Y)
	equalizeHist(channels[0], channels[0]);
	
	//merge 3 channels including the modified 1st channel into one image
	merge(channels, img_hist_equalized);

	//change the color of the image from YCrCb to BGR format (to dispaly image properly)
	cvtColor(img_hist_equalized, img_hist_equalized, CV_YCrCb2BGR);

	//create Windows
	namedWindow("Original Image", CV_WINDOW_AUTOSIZE);
	namedWindow("Histogram Equalized", CV_WINDOW_AUTOSIZE);

	//show th image
	imshow("Original Image", img);
	imshow("Histogram Equalized", img_hist_equalized);

	//wait for key press
	waitKey(0);

	//destroy all open Windows
	destroyAllWindows();

	return 0;
}
	
