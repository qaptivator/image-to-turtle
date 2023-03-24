# image-to-turtle
Turns image which consists of lines into sequence of turtle commands.

Line detection and turtle converter are on different scripts so you can use them seperately.
Feel free to contribute into this project! It's fully open-source.

The documention will be added later on.
For now, explore the code yourself I guess.

# How to use it?

- Install openCV (cv2) into your project and read image using it:
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
- Then to get sequence of commands for the turtle, use type of sequence. For this example we will use ```goto_setpos_type()```. 
To find out all of them check out the documentaion.
```
sequence = goto_setpos_type(lines)
print(sequence)
```
- To actually draw something, we need to use Turtle. This is a library which lets you draw using 'turtle'. 
```
import turtle
t = turtle.Turtle()
```
- Lastly, paste in the sequence which turtle converter outputted. And you will get the image which turtle drew!

To learn more about this, go to the documentation.
Thanks for your attention!
