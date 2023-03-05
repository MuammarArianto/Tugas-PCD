import cv2
import numpy as np

# Load the first image
img1 = cv2.imread('gedung11.jpg', cv2.IMREAD_GRAYSCALE)

# Load the second image
img2 = cv2.imread('gedung22.jpg', cv2.IMREAD_GRAYSCALE)

# Compute the absolute difference between the two images
diff = cv2.absdiff(img1, img2)

# Display the difference image
cv2.imshow('Difference foto', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
