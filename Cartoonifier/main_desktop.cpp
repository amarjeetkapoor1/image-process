//header files
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/opencv.hpp"
#include<iostream>

//namespaces
using namespace cv;
using namespace std;

int main()
{
	//read the image data in the file "me.jpg" and store it in 'img'
        Mat img = imread("me.jpg", CV_LOAD_IMAGE_UNCHANGED); 

	//check whether the image is loaded or not
        if(img.empty()) 
        {
                cout<<"Error:Image cannot be loaded..!!"<<endl;
		//wait for a key press
                system("pause");   
               // return -1;
        }
	
	//create windows to display the image
        namedWindow("OriginalWindow", CV_WINDOW_AUTOSIZE);
	namedWindow("MyWindow", CV_WINDOW_AUTOSIZE);
	namedWindow("MyWindow2", CV_WINDOW_AUTOSIZE);	

	//display the image which is stored in the 'img' in the "MyWindow" window
        imshow("OriginalWindow", img);   

		
	Mat gray;
	Mat edges;
	Mat mask;

	cvtColor(img, gray, CV_BGR2GRAY);
//	const int MEDIAN_BLUR_FILTER_SIZE = 7;
	medianBlur(gray, gray, 7);//MEDIAN_BLUR_FILTER_SIZE);
	
	const int LAPLACIAN_FILTER_SIZE = 5;
	Laplacian(gray, edges, CV_8U, LAPLACIAN_FILTER_SIZE);
	
	const int EDGES_THRESHOLD = 80;
	threshold(edges, mask, EDGES_THRESHOLD, 255, THRESH_BINARY_INV);
	
	imshow("MyWindow", mask);
	
	//For painting
	Size size = img.size();
	Size smallSize;
	smallSize.width = size.width/2;
	smallSize.height = size.height/2;
	Mat smallImg = Mat (smallSize, CV_8UC3);
	resize(img, smallImg, smallSize, 0, 0, INTER_LINEAR);

	Mat tmp = Mat (smallSize, CV_8UC3);
	// Repetitions for strong cartoon effect.
	int repetitions = 7;
	for (int i=0; i<repetitions; i++) {
	//Filter size. Has a large effect on speed.
	int ksize = 9;
	double sigmaColor = 19;
	double sigmaSpace = 17;
	bilateralFilter (smallImg, tmp, ksize, sigmaColor, sigmaSpace);
	bilateralFilter (tmp, smallImg, ksize, sigmaColor, sigmaSpace);
	}

	Mat bigImg;
	Mat mask1;
	resize(smallImg, bigImg, size, 0, 0, INTER_LINEAR);

	bigImg.copyTo(mask1);

	imshow("MyWindow2", mask1);

        waitKey(0);   //wait infinite time for a keypress
        destroyWindow("MyWindow");  //destroy the window with the name, "MyWindow"

        return 0;
}
