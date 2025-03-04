import cv2     # Thư viện OpenCV
import numpy as np   # Thư viện numy để làm việc dữ liệu kiểu mảng
import matplotlib.pyplot as plt # import thư viện matplotlib để vẽ ảnh

# Định nghĩa hàm Tich_chap() để lọc Trung bình, Trung bình có trọng số và lọc Gaussian
def Tich_chap(img,kernel):
    p = int((np.sqrt(kernel.size) - 1)/2)
    h,w = img.shape
    img = np.pad(img, pad_width= p, mode = "constant", constant_values= 0)
    fimg = np.zeros([w,h])
    for i in range(1 , (h - p+2)):
        for j in range(1 , (w - p+2)):
            img_temp = img[i-p:i+p+1, j-p:j+p+1]
            fimg[i-1,j-1] = np.uint8(np.abs(np.sum(kernel * img_temp)))
            # temp   =  img[i-1, j-1]    * kernel[0, 0]\
            #        +  img[i-1, j]      * kernel[0, 1]\
            #        +  img[i-1, j + 1]  * kernel[0, 2]\
            #        +  img[i, j-1]      * kernel[1, 0]\
            #        +  img[i, j]        * kernel[1, 1]\
            #        +  img[i, j + 1]    * kernel[1, 2]\
            #        +  img[i + 1, j-1]  * kernel[2, 0]\
            #        +  img[i + 1, j]    * kernel[2, 1]\
            #        +  img[i + 1, j + 1]* kernel[2, 2]
            # fimg[i-1,j-1] = np.uint8(np.abs(temp))
    return fimg

# Định nghĩa bộ lọc trung bình
locTB3x3 = np.array(([1/9, 1/9, 1/9],
                     [1/9, 1/9, 1/9],
                     [1/9, 1/9, 1/9]), dtype="float")

# Định nghĩa bộ lọc trung bình có trọng số
locTB3x3_trong_so = np.array(([1/16, 2/16, 1/16],
                              [2/16, 4/16, 2/16],
                              [1/16, 2/16, 1/16]), dtype="float")

# Định nghĩa bộ lọc Gaussian
locGaussian3x3 = np.array(([0.0751/4.8976, 0.1238/4.8976, 0.0751/4.8976],
                           [0.1238/4.8976, 0.2042/4.8976, 0.1238/4.8976],
                           [0.0751/4.8976, 0.1238/4.8976, 0.0751/4.8976]), dtype="float")

# Định nghĩa hàm lọc trung vị
def loc_trung_vi(img):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = [img[i - 1, j - 1],
                    img[i - 1, j],
                    img[i - 1, j + 1],
                    img[i, j - 1],
                    img[i, j],
                    img[i, j + 1],
                    img[i + 1, j - 1],
                    img[i + 1, j],
                    img[i + 1, j + 1]]

            temp = sorted(temp)
            img_new[i, j] = temp[4]
    return img_new

# Định nghĩa hàm lọc Max
def loc_max(img):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = [img[i - 1, j - 1],
                    img[i - 1, j],
                    img[i - 1, j + 1],
                    img[i, j - 1],
                    img[i, j],
                    img[i, j + 1],
                    img[i + 1, j - 1],
                    img[i + 1, j],
                    img[i + 1, j + 1]]

            temp = max(temp)     # nếu lọc min thì thay hàm max bằng min(temp)
            img_new[i, j] = temp
    return img_new

fig = plt.figure(figsize=(16, 9)) # Tạo vùng vẽ tỷ lệ 16:9
(ax1, ax2, ax3), (ax4, ax5, ax6) = fig.subplots(2, 3) # Tạo 6 vùng vẽ con

# Đọc và hiển thị ảnh gốc
image = cv2.imread('test2.tif', 0)
ax1.imshow(image, cmap='gray')
ax1.set_title("Ảnh gốc")

# Lọc TB và hiển thị ảnh
imgTB3x3 = Tich_chap(image, locTB3x3) #Gọi hàm lọc
ax2.imshow(imgTB3x3, cmap='gray')
ax2.set_title("Ảnh lọc Trung bình 3x3")

# Lọc TB có trọng số và hiển thị ảnh
imgTB_TS_3x3 = Tich_chap(image, locTB3x3_trong_so) #Gọi hàm lọc
ax3.imshow(imgTB_TS_3x3, cmap='gray')
ax3.set_title("Ảnh lọc Trung bình có trọng số 3x3")

# Lọc Gaussian và hiển thị ảnh
imgGaussian_3x3 = Tich_chap(image, locGaussian3x3) #Gọi hàm lọc
ax4.imshow(imgGaussian_3x3, cmap='gray')
ax4.set_title("Ảnh lọc Gaussian 3x3")

# Lọc Trung vị và hiển thị ảnh
imgTV_3x3 = loc_trung_vi(image) #Gọi hàm lọc
ax5.imshow(imgTV_3x3, cmap='gray')
ax5.set_title("Ảnh lọc Trung vị 3x3")

imgmax_3x3 = loc_max(image) #Gọi hàm lọc
ax6.imshow(imgmax_3x3, cmap='gray')
ax6.set_title("Ảnh lọc Max 3x3")

# Hiển thị vùng vẽ
plt.show()