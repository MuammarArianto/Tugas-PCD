import cv2
import numpy as np

# Load the first image
img1 = cv2.imread('bunga11.jpg')

# Load the second image
img2 = cv2.imread('bunga22.jpg')

# Load the third image
img3 = cv2.imread('bunga33.jpg')

# Compute the average of the three images
avg = cv2.addWeighted(cv2.addWeighted(img1, 0.5, img2, 0.5, 0), 2/3, img3, 1/3, 0)

# Display the average image
cv2.imshow('Average Image', avg)
cv2.waitKey(0)
cv2.destroyAllWindows()
