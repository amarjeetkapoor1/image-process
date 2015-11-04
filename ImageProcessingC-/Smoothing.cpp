//header files
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
//#include <iostream>
#include <stdio.h>

//using namespaces
using namespace cv;
//using namespace std;

int main()
{
	//create two empty windows
	namedWindow("Original Image", CV_WINDOW_AUTOSIZE);
	namedWindow("Smoothed Image", CV_WINDOW_AUTOSIZE);
	namedWindow("Gaussian Smooth", CV_WINDOW_AUTOSIZE);
	namedWindow("Median Smooth", CV_WINDOW_AUTOSIZE);
	namedWindow("Bilateral Smooth", CV_WINDOW_AUTOSIZE);

	//Load an image from file
	Mat src = imread("test.jpg");

	//show the loaded image
	imshow("Original Image", src);

	Mat dst, gdst, mdst, bdst;
	char zBuffer[35];

	for(int i=1;i<31;i=i+2)
	{
		//copy the text to the "zBuffer"
		snprintf(zBuffer, 35, "Kernel Size: %d x %d",i,i);

		//smooth the image in the "src" and save it to "dst"
		blur(src, dst, Size(i,i));

		//smooth the image using Gaussian kernel in the "src" and save it to "dst"
		GaussianBlur(src, gdst, Size(i,i),0,0);

		//Median Blur
		medianBlur(src, mdst, i);

		//Bilateral Blur
		bilateralFilter(src, bdst, i,i,i);

		//put the text in the "zBuffer" to the "dst" image
		putText(dst, zBuffer, Point(src.cols/4, src.rows/8), CV_FONT_HERSHEY_COMPLEX,1,Scalar(255,255,255));

		//show the blurred image with the text
		imshow("Smoothed Image", dst);

		//put the text in the "zBuffer" to the "gdst" image
		putText(gdst, zBuffer, Point(src.cols/4, src.rows/8), CV_FONT_HERSHEY_COMPLEX,1,Scalar(255,255,255));


		//show the Gaussian Smooth image
		imshow("Gaussian Smooth", gdst);

		//put the text in the "zBuffer" to the "mdst" image
		putText(mdst, zBuffer, Point(src.cols/4, src.rows/8), CV_FONT_HERSHEY_COMPLEX,1,Scalar(255,255,255),2);

		//show the Median Smooth
		imshow("Median Smooth", mdst);

		 //put the text in the "zBuffer" to the "bdst" image
                putText(bdst, zBuffer, Point(src.cols/4, src.rows/8), CV_FONT_HERSHEY_COMPLEX,1,Scalar(255,255,255));

		//show the Bilateral Smooth
		imshow("Bilateral Smooth", bdst);

		//wait for 2 seconds
		int c = waitKey(3000);

		//if the "esc" key is pressed during the wait, return
		if(c==27)
		{
			return 0;
		}
	}

	//make the "dst" image, black
	dst = Mat::zeros(src.size(), src.type());

	//make the "gdst" image, black
        gdst = Mat::zeros(src.size(), src.type());

	//make the "mdst" image, black
        mdst = Mat::zeros(src.size(), src.type());

	//make the "bdst" image, black
	bdst = Mat::zeros(src.size(), src.type());

	//copy the text to the "zBuffer"
	snprintf(zBuffer, 35, "Press any key to Exit");
	
	//put the text in the "zBuffer" to the "dst" image
	putText(dst, zBuffer, Point(src.cols/4, src.rows/2), CV_FONT_HERSHEY_COMPLEX,1,Scalar(255,255,255));

	//show the black image with the text
	imshow("Smoothed Image", dst);

	//put the text in the "zBuffer" to the "gdst" image
        putText(gdst, zBuffer, Point(src.cols/4, src.rows/2), CV_FONT_HERSHEY_COMPLEX,1,Scalar(255,255,255));

	//show the image where gaussian blur is applied
	imshow("Gaussian Smooth", gdst);

	//put the text in the "zBuffer" to the "mdst" image
        putText(mdst, zBuffer, Point(src.cols/4, src.rows/2), CV_FONT_HERSHEY_COMPLEX,1,Scalar(255,255,255),2);

	//show the image where Median blur is applied
	imshow("Median Smooth", mdst);

	//put the text in the "zBuffer" to the "bdst" image
        putText(bdst, zBuffer, Point(src.cols/4, src.rows/2), CV_FONT_HERSHEY_COMPLEX,1,Scalar(255,255,255),2);

        //show the image where Median blur is applied
        imshow("Bilateral Smooth", bdst);


	//wait for a key press infinitely
	waitKey(0);

	return 0;
}
