import cv2
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from matplotlib import pyplot as plt

url = 'https://images8.alphacoders.com/929/929986.jpg'


def _downloadImage(url):
    resp = requests.get(url)
    img = np.asarray(bytearray(resp.content), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img


img = cv2.imread('resources/digital_art.jpg')
print('origin image shape: {}'.format(img.shape))

rows, cols = img.shape[:2]
# Dịch chuyển hình ảnh xuống góc dưới bên phải
tx, ty = (200, 200)
M1 = np.array([[1, 0, tx],
               [0, 1, ty]], dtype=np.float32)
tran1 = cv2.warpAffine(img, M1, (cols, rows))

# Dịch chuyển hình ảnh xuống góc dưới bên trái
M2 = np.array([[1, 0, -tx],
               [0, 1, ty]], dtype=np.float32)
tran2 = cv2.warpAffine(img, M2, (cols, rows))

# Dịch chuyển hình ảnh xuống góc dưới bên trái
M3 = np.array([[1, 0, tx],
               [0, 1, -ty]], dtype=np.float32)
tran3 = cv2.warpAffine(img, M3, (cols, rows))

# Dịch chuyển hình ảnh xuống góc dưới bên trái
M4 = np.array([[1, 0, -tx],
               [0, 1, -ty]], dtype=np.float32)
tran4 = cv2.warpAffine(img, M4, (cols, rows))

plt.figure(figsize=(16, 4))
plt.subplot(151), plt.imshow(img), plt.title('Origin Image')
plt.xticks([]), plt.yticks([])
plt.subplot(152), plt.imshow(tran1), plt.title('Translate to Bottom Right')
plt.xticks([]), plt.yticks([])
plt.subplot(153), plt.imshow(tran2), plt.title('Translate to Bottom Left')
plt.subplot(154), plt.imshow(tran3), plt.title('Translate to Up Right')
plt.subplot(155), plt.imshow(tran4), plt.title('Translate to Up Left')
plt.show()