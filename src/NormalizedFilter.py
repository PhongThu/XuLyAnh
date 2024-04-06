import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load and blur image
img = cv.imread('resources/rose_gauss.jpg')
img2 = cv.imread('resources/rose_gauss.jpg')
blur = cv.blur(img, (10, 10))
blur2 = cv.blur(img2, (10, 10))

# Convert color from bgr (OpenCV default) to rgb
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)
img_rgb2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
blur_rgb2 = cv.cvtColor(blur2, cv.COLOR_BGR2RGB)

# Display
plt.subplot(121), plt.imshow(img_rgb), plt.title('Gauss Noise')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur_rgb), plt.title('Gauss Noise - Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
