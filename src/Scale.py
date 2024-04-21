import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

img = cv2.imread('resources/image1.jpg')
print('origin image shape: {}'.format(img.shape))

# Scale image bằng cách gấp đôi width and height
h, w = img.shape[:2]
imgScale = cv2.resize(img, (int(w*2), int(h*2)), interpolation = cv2.INTER_LINEAR)
print('scale image shape: {}'.format(imgScale.shape))

plt.subplot(121),plt.imshow(imgScale),plt.title('Origin Image')
plt.subplot(122),plt.imshow(imgScale),plt.title('Scale Image')
plt.show()
