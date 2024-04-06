import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Đọc hình ảnh từ tệp
img = cv.imread('resources/image1.jpg')

# Làm mờ hình ảnh bằng bộ lọc Gaussian
blurred_image = cv.GaussianBlur(img, (5, 5), 0)

# Lọc sắc cạnh bằng bộ lọc Laplacian
laplacian = cv.Laplacian(img, cv.CV_64F)

# Chuyển đổi ảnh từ dạng float64 sang uint8
laplacian = cv.convertScaleAbs(laplacian)

# Thay đổi kích thước ảnh
img = cv.resize(img, None, fx=0.3, fy=0.3)
blurred_image = cv.resize(blurred_image, None, fx=0.3, fy=0.3)
laplacian = cv.resize(laplacian, None, fx=0.3, fy=0.3)

# Hiển thị ảnh
cv.imshow('Original', img)
cv.imshow('Gaussian', blurred_image)
cv.imshow('Laplacian', laplacian)
cv.waitKey(0)
cv.destroyAllWindows()
# sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
# sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)

# plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
#
# plt.subplot(1, 3, 2), plt.imshow(blurred_image, cmap='gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
#
# plt.subplot(1,3,3), plt.imshow(laplacian, cmap='gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

# plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
#
# plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
