import cv2
import numpy as np
from matplotlib import pyplot as plt

# Đọc hình ảnh từ tệp và chuyển sang thang độ xám
image = cv2.imread('resources/cat.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Thực hiện biến đổi Fourier
f_transform = np.fft.fft2(image_gray)
f_shift = np.fft.fftshift(f_transform)
magnitude_spectrum = 20 * np.log(np.abs(f_shift))

# Hiển thị hình ảnh gốc và biểu đồ phổ tần số

# Ảnh gốc
plt.subplot(221), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# Ảnh xám
plt.subplot(222), plt.imshow(image_gray, cmap='gray')
plt.title('Gray Image'), plt.xticks([]), plt.yticks([])

# Biến đổi Fourier
plt.subplot(2,2,3), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
