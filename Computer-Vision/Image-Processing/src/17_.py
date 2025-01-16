import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("E:\\1.Language\\python\\smarties.png",cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 250, cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2),np.uint8) # hình chữ nhật độ dài (x,y) np.uint8 
dilation = cv2.dilate(mask, kernal, iterations= 2)
# cv2.dilate(src,kernel,dst) -> hàm biến đổi hình học dựa trên việc phóng đại ứng dụng: loại bỏ nhiễu, liên kết đối tượng rời rạc, tăng độ tương phản
# kernel: khu vực muốn biến đổi hình học
# iterations: số lần thực hiện lặp

erosion = cv2.erode(mask, kernal, iterations= 1)
# cv2.erode(src,kernel,dst) -> hàm cho phép thực hiện phép biến đổi hình học gọi là ăn mòn -> nó làm giảm kích thước của các hình dạng trong ảnh
# -> có ứng dụng tương tự như cv2.dilate()

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
# là hàm có khả năng thực hiện phép biến đổi hình thái trên ảnh bằng cách sử dụng các chức năng da dụng
# cv2.MORPH_OPEN: kết hợp ăn mòn trước rồi phóng đại giúp loại bỏ các lỗ nhỏ và các đối tượng gần nhau

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
# cv2.MORPH_CLOSE: kết hợp phóng đại trước rồi ăn mòn

mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT, kernal)
#cv2.MORPH_GRADIENT : là kết quả của sự khác biệt giữa sói mòn và mở rộng

image = [img, mask, dilation, erosion, opening, closing, mg]

title = ["img","mask", "dilation", "erosion", "opening", "closing", "mg"]
for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(image[i],"gray")
    plt.title(title[i]  )
    plt.xticks([])
    plt.yticks([])

plt.show()