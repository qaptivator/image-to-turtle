import cv2
import numpy as np

def convert_gray_scale(image):
	return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def apply_smoothing(image, kernel_size=15):
	"""
    kernel_size must be postivie and odd
    """
	return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)



def detect_edges(image, low_threshold=50, high_threshold=150):
	return cv2.Canny(image, low_threshold, high_threshold)


def hough_lines(image):
	"""
  `image` should be the output of a Canny transform.
    
  Returns hough lines (not the image with lines)
  """
	return cv2.HoughLinesP(image, rho=1, theta=np.pi / 180, threshold=20, minLineLength=20, maxLineGap=300)



def binary_threshold(image):
  ret, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
  return ret, thresh


def detect_lines(image):
  gray = convert_gray_scale(image)
  edges = apply_smoothing(gray)
  lines = hough_lines(edges)
  return lines
def draw_lines(image, lines, image_name='detectedLines.png'):
  for points in lines:
    # extracted points nested in the list
    x1, y1, x2, y2 = points[0]
    # draw the lines joing the points on the original image
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
  newimage = cv2.imwrite(image_name, image)
  return newimage


