import cv2
import numpy as np

# Load image
image = cv2.imread('image.jpg')

# Convert image to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range of color in HSV
lower_color = np.array([0, 50, 50])
upper_color = np.array([10, 255, 255])

# Threshold the HSV image to get only desired color
mask = cv2.inRange(hsv_image, lower_color, upper_color)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(image, image, mask=mask)

# Display the original and result images
cv2.imshow('Original Image', image)
cv2.imshow('Color Detected', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
