import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load low-quality image
image_low = Image.open("gambar_rendah.jpg")

# Convert image to grayscale
image_low = image_low.convert("L")

# Convert image to numpy array
data_low = np.asarray(image_low)

# Create histogram for low-quality image
plt.hist(data_low.ravel(), bins=256, range=(0, 255))

# Add low-quality image to histogram
plt.imshow(data_low, cmap=plt.cm.gray, alpha=0.5)

# Show the plot for low-quality image
plt.show()

# Load normal-quality image
image = Image.open("gambar_normal.jpg")

# Convert image to grayscale
image = image.convert("L")

# Convert image to numpy array
data = np.asarray(image)

# Create histogram for normal-quality image
plt.hist(data.ravel(), bins=256, range=(0, 255))

# Add normal-quality image to histogram
plt.imshow(data, cmap=plt.cm.gray, alpha=0.5)

# Show the plot for normal-quality image
plt.show()

# Load high-quality image
image_high = Image.open("gambar_tinggi.jpg")

# Convert image to grayscale
image_high = image_high.convert("L")

# Convert image to numpy array
data_high = np.asarray(image_high)

# Create histogram for high-quality image
plt.hist(data_high.ravel(), bins=256, range=(0, 255))

# Add high-quality image to histogram
plt.imshow(data_high, cmap=plt.cm.gray, alpha=0.5)

# Show the plot for high-quality image
plt.show()
