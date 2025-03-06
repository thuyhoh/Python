# Phân đoạn ảnh bằng kỹ thuật cắt ngưỡng theo 1 ngưỡng toàn cục
import cv2
import numpy as np
from matplotlib import pyplot as plt

def phan_doan_bang_cat_nguong(img,nguong): # Định nghĩa hàm phân đoạn bằng cắt ngưỡng
    m, n = img.shape
    img_phan_doan_cat_nguong = np.zeros([m, n])
    for i in range(m):
        for j in range(n):
            if (img[i,j] < nguong):
                img_phan_doan_cat_nguong[i,j] = 0
            else:
                img_phan_doan_cat_nguong[i,j] = 225 # tương đương gt 1 trong công thức 1
    return img_phan_doan_cat_nguong

if __name__ == "__main__":
    # reading image in gray scale
    img_goc = cv2.imread('test2.tif', 0)
    nguong = 110

    img_phan_doan=phan_doan_bang_cat_nguong(img_goc,nguong)

    # Vẽ và hiển thị ảnh gốc, histogram ảnh gốc và ảnh phân đoạn
    fig2 = plt.figure(figsize=(16, 9))  # Tạo vùng vẽ tỷ lệ 16:9
    # Tạo 4 vùng vẽ con
    (ax1, ax2), (ax3, ax4) = fig2.subplots(2, 2)
    # Hiển thị ảnh gốc
    ax1.imshow(img_goc, cmap='gray')
    ax1.set_title('Ảnh gốc')
    ax1.axis('off')

    # Hiển thị histogram ảnh gốc
    ax2.hist(img_goc.flatten(), bins=256)
    ax2.set_title('Hitogram ảnh gốc')

    # Hiển thị ảnh phân đoạn
    ax3.imshow(img_phan_doan, cmap='gray')
    ax3.set_title('Ảnh phân đoạn dựa vào tìm ngưỡng Otsu')
    ax3.axis('off')

    # Hiển thị histogram ảnh phân đoạn
    ax4.hist(img_phan_doan.flatten(), bins=256)
    ax4.set_title('Hitogram ảnh phân đoạn')
    plt.show()