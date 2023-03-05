import cv2
import matplotlib.pyplot as plt

# Load the low quality image
img1 = cv2.imread('gambar_rendah.jpg', cv2.IMREAD_GRAYSCALE)

# Load the high quality image
img2 = cv2.imread('gambar_tinggi.jpg', cv2.IMREAD_GRAYSCALE)

# Equalize the histograms of the 2 images
img1_eq = cv2.equalizeHist(img1)
img2_eq = cv2.equalizeHist(img2)

# Plot the original and equalized histograms of the low quality image
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].imshow(img1, cmap=plt.cm.gray)
axs[0, 0].set_title('kualitas rendah')
axs[0, 1].hist(img1.ravel(), 256, [0, 256], color='r')
axs[0, 1].set_title('Histogram kualitas rendah')
axs[1, 0].imshow(img1_eq, cmap=plt.cm.gray)
axs[1, 0].set_title('Equalized kualitas rendah')
axs[1, 1].hist(img1_eq.ravel(), 256, [0, 256], color='r')
axs[1, 1].set_title('Equalized Histogram kualitas rendah')

# Plot the original and equalized histograms of the high quality image
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].imshow(img2, cmap=plt.cm.gray)
axs[0, 0].set_title('kualitas tinggi')
axs[0, 1].hist(img2.ravel(), 256, [0, 256], color='r')
axs[0, 1].set_title('Histogram kualitas tinggi')
axs[1, 0].imshow(img2_eq, cmap=plt.cm.gray)
axs[1, 0].set_title('Equalized kualitas tinggi')
axs[1, 1].hist(img2_eq.ravel(), 256, [0, 256], color='r')
axs[1, 1].set_title('Equalized Histogram kualitas tinggi')

plt.show()
