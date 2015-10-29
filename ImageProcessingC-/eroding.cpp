#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
	//display the original Image
	Mat img = imread("test.jpg", CV_LOAD_IMAGE_COLOR);
	namedWindow("Original Image", CV_WINDOW_AUTOSIZE);
	imshow("Original Image", img);

	//create a structuring element 
//	int erosion_size = 6;
//	Mat element = getStructuringElement(MORPH_CROSS,Size(2 * erosion_size + 1, 2 * erosion_size + 1),Point(erosion_size, erosion_size) );


//	a = Mat();	
//erode and display the eroded image
	erode(img, img, 0, 2);
	namedWindow("Eroded Image", CV_WINDOW_AUTOSIZE);
	imshow("Eroded Image", img);

	waitKey(0);

	//cleaning up
	destroyAllWindows();

	return 0;
}
