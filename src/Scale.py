import cv2
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

url = 'https://images8.alphacoders.com/929/929986.jpg'
def _downloadImage(url):
    resp = requests.get(url)
    img = np.asarray(bytearray(resp.content), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img

img = _downloadImage(url)
print('origin image shape: {}'.format(img.shape))

# Scale image bằng cách gấp đôi width and height
h, w = img.shape[:2]
imgScale = cv2.resize(img, (int(w*2), int(h*2)), interpolation = cv2.INTER_LINEAR)
print('scale image shape: {}'.format(imgScale.shape))

plt.subplot(121),plt.imshow(imgScale),plt.title('Origin Image')
plt.subplot(122),plt.imshow(imgScale),plt.title('Scale Image')

