#include "opencv2/highgui/highgui.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    VideoCapture cap("ThePower.mp4"); // open the video file for reading

    if ( !cap.isOpened() )  // if not success, exit program
    {
         cout << "Cannot open the video file" << endl;
//         return 9;
    }

    //cap.set(CV_CAP_PROP_POS_MSEC, 3000); //start the video at 300ms

    double fps = cap.get(CV_CAP_PROP_FPS); //get the frames per seconds of the video

    double fcc = cap.get(CV_CAP_PROP_FOURCC); //get four character code of codec

     cout << "Frame per seconds : " << fps << endl;

    namedWindow("MyVideo",CV_WINDOW_AUTOSIZE); //create a window called "MyVideo"

    while(1)
    {
        Mat frame;

        bool bSuccess = cap.read(frame); // read a new frame from video

        if (!bSuccess) //if not success, break loop
        {
                        cout << "Cannot read the frame from video file" << endl;
                       break;
        }

        imshow("MyVideo", frame); //show the frame in "MyVideo" window

        if(waitKey(30) == 27) //wait for 'esc' key press for 30 ms. If 'esc' key is pressed, break loop
       {
                cout << "esc key is pressed by user" << endl; 
                break; 
       }
    }

    return 0;

}
