import cv2
import numpy as np

# Đọc ảnh và chuyển sang xám
img = cv2.imread('D:/Program_Languages/Python/Computer-Vision/OpenCV/lena.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Tạo ảnh nhị phân
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Giãn nở
dilated = cv2.dilate(thresh, None, iterations=3)

# Hiển thị
cv2.imshow('Threshold', thresh)
cv2.imshow('Dilated', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()