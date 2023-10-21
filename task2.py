import cv2
import numpy as np

def detect_color(image, color):
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  lower_bound = np.array(color[0])
  upper_bound = np.array(color[1])
  mask = cv2.inRange(hsv, lower_bound, upper_bound)
  extracted_pixels = cv2.bitwise_and(image, image, mask=mask)
  return extracted_pixels



cap = cv2.VideoCapture("C:/Users/LAPTOP/Desktop/shahd/pic/Data Structures(phase2).mp4")
while True:
  ret, frame = cap.read()
  # If the frame is empty, break the loop
  if not ret:
    break

  red_pixels = detect_color(frame, [(0, 100, 100), (10, 255, 255)])
  cv2.imshow("Red Pixels", red_pixels).
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
# Close all windows.
cv2.destroyAllWindows()
