
# importing libraries 
import numpy as np 
import cv2 

  
# Reading image
img = cv2.imread('Screenshot 2024-04-05 150156.png') 



# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to binarize the image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

#finding contours on grid
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#applying contours
contour_img = cv2.drawContours(img.copy(), contours, -1, (0, 0, 0),3)

dst=contour_img

  
#denoising first time
dst = cv2.fastNlMeansDenoisingColored(dst, None, 10, 20, 15, 40) 

#making a copy for first processed image
dstcopy=dst  


#Again applying denoising function
result2 = cv2.fastNlMeansDenoisingColored(dstcopy, None, 20, 5, 15, 10) 

#export final processed image
cv2.imwrite('sample_output.jpg', result2)

# Display the result
cv2.imshow('Result', result2)
cv2.waitKey(0)
cv2.destroyAllWindows()


