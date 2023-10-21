import cv2
import numpy as np

def detect_color(image, color):
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  lower_bound = np.array(color[0])
  upper_bound = np.array(color[1])
  mask = cv2.inRange(hsv, lower_bound, upper_bound)
  extracted_pixels = cv2.bitwise_and(image, image, mask=mask)
  return extracted_pixels


image = cv2.imread("C:/Users/LAPTOP/Desktop/shahd/pic/p2.png")
#cv2.imshow("Red Pixels", image)
red_pixels = detect_color(image, [(0, 100, 100), (10, 255, 255)])
cv2.imshow("Red Pixels", red_pixels)
cv2.waitKey(0)
