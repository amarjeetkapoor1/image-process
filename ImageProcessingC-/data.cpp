#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
	Mat A,C;
	A = imread("test.jpg", CV_LOAD_IMAGE_COLOR);
	Mat B(A);
	
	namedWindow("Image", CV_WINDOW_AUTOSIZE);
	C = A;

	Mat D(A, Rect(10,10,100,100));
	Mat E = A(Range::all(), Range(1,3));

	imshow("Image", A);
	waitKey(0);
	return 0;
}
