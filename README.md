# image-process
This repository contain functions used for Image Processing and Robotic Vision.
Modules in this repository are made using-:
1.Python
2.Opencv
3.sagemath
4.matplotlib
5.numpy
6.scipy
7.skimage
modules-:
blob.py (this program finds blue color bolobs in image)
1.count_colors.py ( this module contain function to count no. of colors and their value) 
2.get.py ( this module contain functions to detect color , find shape and some more )
  getcolor.txt ( this file contain color range for being used in get.py )
3.getshape.sage ( this module contain functions to detect color , find shape and some more but in sage)
4.3.moment1.py (This module contain function to find moment of binary image) 
5.monadic.py (This module contain function for contrast, brightness,posterization and negative on image)


programs-:
1.doc.sage(this program find maxima and minma in color list and 
  transform image into one with only color within maxima)
2.find_no_color_sir.sage ( this program find no. colors in image using particular place for all color values )
3.hist.sage( this program finds maxima and minima in image using sage)
4.histGray.sage ( this program find maxima and minma in color list and 
  transform image into one with only color within maxima for gray image )
5.iterate_findnoofcolors.sage (this program find no of color by adding every element in list #inefficient)
6.optimum.sage ( this program finds total no of maximum which are less than specified by user using sage)
7.robotic_vision.py (this program uses get.py and find color and shape in image)
8.videos_detection.py (this program uses get.py and find color and shape using webcam)
