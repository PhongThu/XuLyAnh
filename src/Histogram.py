import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tính toán histogram của một hình ảnh xám
def compute_hist(img):
    hist = cv2.calcHist([img], [0], None, [256], [0,256])
    return hist.ravel()

# Thực hiện cân bằng histogram
def equal_hist(hist):
    cumulator = np.zeros_like(hist, np.float64)
    for i in range(len(cumulator)):
        cumulator[i] = hist[:i+1].sum()
    new_hist = (cumulator - cumulator.min())/(cumulator.max() - cumulator.min()) * 255
    new_hist = np.uint8(new_hist)
    return new_hist

# Đọc hình ảnh từ tệp
img = cv2.imread("resources/rose.jpg", 0)

# Tính toán histogram của hình ảnh gốc
hist_original = compute_hist(img)

# Cân bằng histogram
new_img = cv2.equalizeHist(img)
hist_equalized = compute_hist(new_img)

# Hiển thị hình ảnh gốc và hình ảnh đã cân bằng histogram
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Original Image')

axes[0, 1].plot(hist_original, color='b')
axes[0, 1].set_title('Original Histogram')

axes[1, 0].imshow(new_img, cmap='gray')
axes[1, 0].set_title('Equalized Image')

axes[1, 1].plot(hist_equalized, color='r')
axes[1, 1].set_title('Equalized Histogram')

plt.tight_layout()
plt.show()