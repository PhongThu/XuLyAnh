import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("resources/image1.jpg", 0)

def compute_hist(img):
    hist = np.zeros((256,), np.uint8)
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i][j]] += 1
    return hist

def equal_hist(hist):
    cumulator = np.zeros_like(hist, np.float64)
    for i in range(len(cumulator)):
        cumulator[i] = hist[:i+1].sum()  # Thêm 1 vào chỉ số i
    new_hist = (cumulator - cumulator.min())/(cumulator.max() - cumulator.min()) * 255
    new_hist = np.uint8(new_hist)
    return new_hist

hist = compute_hist(img).ravel()
new_hist = equal_hist(hist)

h, w = img.shape[:2]
for i in range(h):
    for j in range(w):
        img[i,j] = new_hist[img[i,j]]

fig = plt.figure(figsize=(12, 6))

ax = plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Equalized Image')

plt.subplot(122)
plt.plot(new_hist)
plt.title('Equalized Histogram')
plt.show()