# image-to-turtle
Turns image which consists of lines into string sequence of Turtle commands.

Line detection and turtle converter are on different scripts so you can use them separately.
Feel free to contribute into this project! It's fully open-source.

# How to use it?
- Install OpenCV (cv2) into your project and load image using it:
```
import cv2 
image = cv2.imread('<path-to-image>.png')
```
- Import the line detection and turtle convertion into your script, like so:
```
import * from linedetection, turtleconverter 
```
- Use ```detect_lines()``` to get array of lines in the image, like so:
```
lines = detect_lines(image)
```
- Then we should convert our lines into sequence of commands for Turtle.
```
sequence = goto_setpos_type(lines)
print(sequence)
```
- Lastly, paste the sequence into your Turtle project and look how it draws!

For visualizing the lines, use ```draw_lines()```
Now it's your time to find out where to use this!

# Documentation
image-to-turtle is python script which turns images filled with lines into sequence of commands for [Turtle](https://docs.python.org/3/library/turtle.html#module-turtle).

There are 2 different parts, line detection and turtle converter.
First module turns image into array of lines. Second part turns array of lines into sequence of commands for Turtle. That means you can use them separately.

This project is fully open-source so feel free to contribute!

## Overview of all functions
Line Detection:
```detect_lines()```
```draw_lines()```
```convert_gray_scale()```
```apply_smoothing()```
```binary_threshold()```
```detect_edges()```
```hough_lines()```

Turtle:
```setpos_type()```
```goto_type()```
```move_spin_type()```

## Line Detection
Detect lines on the image so you can feed it to Turtle module.

### detect_lines(image)
Arguments:
- image - loaded image from a file, can be received using ```cv2.imread('file.png')```

Returns array of start and end points of lines, but you input just the image.
It uses Grayscaling, Gaussian Blur, Canny Edge Detection and Hough lines.

### draw_lines(image, lines, image_name)
Arguments:
- image - loaded image from a file, can be received using ```cv2.imread('file.png')```
- lines - array of start and end points of lines, can be received using ```detect_lines()``` or ```hough_lines()```
- image_name - name of output image

Draws lines on the image. It can be used for visualizing the modified version of line detection if you make one. Returns a new image with the lines.

### convert_gray_scale(image)
Arguments:
- image - loaded image from a file, can be received using ```cv2.imread('file.png')```

Convert loaded image into grayscale for future computations. Returns grayscaled version of image.

### apply_smoothing(image, kernel_size)
Arguments:
- image - grayscale image
- kernel_size - bluryness of image. **it must be positive and odd**

Smooths out edges of pixels so that it won't be too noisy. Returns smoothed out version.
 Gaussian Blur is explained [here](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
 
 ### binary_threshold(image)
Arguments:
- image - grayscale image

Smoothes out image but uses a different method, you can learn more about it [here](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html)
Returns smoothed out image.
### detect_edges(image, low_threshold, high_threshold)
Arguments:
- image - grayscale image (could be with smoothed out edges)
- low_threshold - lowest value for thresholding
- high_threshold - highest value for thresholding

Takes two threshold values and returns detected edges.
Canny edge detection is explained [here](http://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html)

### hough_lines(edges)
Arguments:
- edges - should be output of detect_edges (Canny Transform)

Returns array of start and end points of lines, which are called hough lines.
It doesn't output image with the lines.

## Turtle
You can have different methods of visualizing image using Turtle.
All of the functions return string sequence of different Turtle commands.
### setpos_type(lines, turtle_name)
Arguments:
- lines - array of start and end points of lines
- turtle_name - name of variable which stores your turtle

This type returns the shortest sequence. It consists of ```setposition()``` and ```goto()```

### goto_type(lines, turtle_name)
Arguments:
- lines - array of start and end points of lines
- turtle_name - name of variable which stores your turtle

This type returns medium sequence, but it's more visualized. It consists of ```penup()```, ```pendown()```and ```goto()```

### move_spin_type(lines, turtle_name)
Arguments:
- lines - array of start and end points of lines
- turtle_name - name of variable which stores your turtle

This type returns large sequence, but it's even more visualized and doesn't use ```goto()```
It consists of ```penup()```, ```pendown()```, ```right()```, ```towards()```, ```distance()``` and ```forward()```
