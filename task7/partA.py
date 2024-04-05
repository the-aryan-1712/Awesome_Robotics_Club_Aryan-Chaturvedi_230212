
# importing libraries 
import numpy as np 
import cv2 

  
# Reading image from folder where it is stored 
img = cv2.imread('Screenshot 2024-04-05 150156.png') 




# for contour
# Read the image


# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to binarize the image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
contour_img = cv2.drawContours(img.copy(), contours, -1, (0, 0, 0),3)
# cv2.imshow('Result', contour_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# Display the result
dst=contour_img

  
# denoising of image saving it into dst image 
dst = cv2.fastNlMeansDenoisingColored(dst, None, 10, 20, 15, 40) 
dstcopy=dst  
# Plotting of source and destination image 
# cv2.imshow('Result', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import numpy as np

# Read the image


# Convert image to HSV color space
hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the color you want to isolate (in HSV)
lower_color = np.array([100, 50, 50])
upper_color = np.array([130, 255, 255])

# Create a mask using inRange function
mask = cv2.inRange(hsv, lower_color, upper_color)

# Apply morphological operations (optional)
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Apply the mask to the original image
result = cv2.bitwise_and(dst, dst, mask=mask)
result2 = cv2.fastNlMeansDenoisingColored(dstcopy, None, 20, 5, 15, 10) 
cv2.imwrite('contour_grid_image.jpg', result2)
# Display the result
cv2.imshow('Result', result2)
cv2.waitKey(0)
cv2.destroyAllWindows()


