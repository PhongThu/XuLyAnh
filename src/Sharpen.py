import cv2
import numpy as np

# Đọc hình ảnh từ tệp
image = cv2.imread('resources/image1.jpg')

# Điều chỉnh độ sáng và độ tương phản
alpha = 1.5  # Tăng độ sáng
beta = 30  # Tăng độ tương phản
brightened_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Hiển thị hình ảnh gốc và hình ảnh đã tăng độ sáng

image = cv2.resize(image, None, fx=0.3, fy=0.3)
brightened_image = cv2.resize(brightened_image, None, fx=0.3, fy=0.3)
cv2.imshow('Original Image', image)
cv2.imshow('Brightened Image', brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Đọc hình ảnh từ tệp
image1 = cv2.imread('resources/rose.jpg')

# Tăng độ sáng bằng cách cộng một giá trị độ sáng cho từng pixel
brightness_value = 50  # Giá trị độ sáng cần tăng
brightened_image1 = np.clip(image1.astype(int) + brightness_value, 0, 255).astype(np.uint8)

image1 = cv2.resize(image1, None, fx=0.3, fy=0.3)
brightened_image1 = cv2.resize(brightened_image1, None, fx=0.3, fy=0.3)
# Hiển thị hình ảnh gốc và hình ảnh đã tăng độ sáng
cv2.imshow('Original Image', image1)
cv2.imshow('Brightened Image', brightened_image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
