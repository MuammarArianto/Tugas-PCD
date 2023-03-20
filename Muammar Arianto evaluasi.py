import matplotlib, cv2
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# import numpy
# import matplotlib.pyplot as plt
img = cv2.imread('ammar.JPG')
img = mpimg.imread('ammar.JPG')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()