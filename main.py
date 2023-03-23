import cv2
import numpy as np

offset = 450 #  offset for the image so you would actually see it

# Read image
image = cv2.imread('testimage.png')
height,width,c = image.shape
newimage = np.zeros((height,width,3), np.uint8)

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use canny edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Apply HoughLinesP method to
# to directly obtain line end points
lines_list = []
lines = cv2.HoughLinesP(
    edges,  # Input edge image
    1,  # Distance resolution in pixels
    np.pi / 180,  # Angle resolution in radians
    threshold=100,  # Min number of votes for valid line
    minLineLength=5,  # Min allowed length of line
    maxLineGap=10  # Max allowed gap between line for joining them
)

# stuff it should output:
# forward(), backward(), left(), right()
# goto()
turtle_sequence = []

#drawLine function
#def drawLine(x1, y1, x2, y2):
  #t.penup()
  #t.setposition(x1, y1)
  #t.pendown()
  #t.goto(x2, y2)

# Iterate over points
for points in lines:
    # Extracted points nested in the list
    x1, y1, x2, y2 = points[0]
    turtle_sequence.append('drawLine({0},{1},{2},{3})'.format(x1-offset, y1-offset, x2-offset, y2-offset))
    # Draw the lines joing the points
    # On the original image
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.line(newimage, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # Maintain a simples lookup list for points
    lines_list.append([(x1, y1), (x2, y2)])

# Save the result image
cv2.imwrite('detectedLines.png', image)
cv2.imwrite('detectedLinesBlank.png', newimage)

for el in turtle_sequence:
  print(el)  