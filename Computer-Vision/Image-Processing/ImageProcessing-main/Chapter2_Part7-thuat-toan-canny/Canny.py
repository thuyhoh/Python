import cv2
import numpy as np
from matplotlib import pyplot as plt

# Bộ lọc trung bình
f_tb_3x3 = np.float16(1/9 * np.ones([3,3]))

# Định nghĩa Sobel theo hướng X
locSobelX = np.array(([-1,-2,-1],
                      [ 0, 0, 0],
                      [ 1, 2, 1]), dtype="float")

# Định nghĩa bộ lọc Sobel theo hướng Y
locSobelY = np.array(([-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]), dtype="float")

# bộ lọc prewith
prewith_x = np.array(([ 1, 1, 1],
                      [ 0, 0, 0 ],
                      [ -1,-1, -1 ]   ), dtype = float
)

prewith_y = np.array(([ -1, 0, 1],
                      [-1, 0,1],
                      [ -1, 0, 1]   ), dtype = float
)


def gaussian_kernal(size, signal = 1):
    size = int(size)//2
    x,y = np.mgrid[-size: size+1, -size : size +1]
    normal = 1/(2.0 * np.pi * signal**2)
    g = np.exp(-((x**2 + y**2) / (2.0* signal**2))) * normal
    return g

def tich_chap(img , kernel):
    k = int(np.sqrt(kernel.size))
    p = int((np.sqrt(kernel.size) - 1)/2)
    h,w = img.shape
    img = np.pad(img, pad_width= p, mode = "constant", constant_values= 0)
    fimg = np.zeros([w,h])
    for i in range(h):
        for j in range(w):
            img_temp = img[i:i+k, j:j+k]
            fimg[i,j] = np.uint8(np.abs(np.sum(kernel*img_temp)))
            
    return fimg

def NMS(img, edgeX, edgeY):
    h, w = edgeX.shape
    result = np.zeros([h,w])
    for i in range(h):
        for j in range(w):
            try:
                angle = np.arctan(edgeY[i,j]/edgeX[i,j]) * 180. / np.pi
                if(angle < 0):
                    angle += 180
                p = 0
                r = 0
                # 0/180 do
                if (0 <= angle< 22.5) or (157.5 <= angle<= 180):
                    p = img[i-1,j]
                    r = img[i+1,j]
                # 45 do
                elif (22.5 <= angle< 67.5):
                    p = img[i+1, j+1]
                    r = img[i-1, j-1]
                # 90 do
                elif (67.5 <= angle< 112.5):
                    p = img[i, j+1]
                    r = img[i, j-1]
                # 135
                elif (112.5 <= angle< 157.5):
                    p = img[i+1, j-1]
                    r = img[i-1, j+1]

                if((img[i,j] >= p ) and (img[i,j] >= r)):
                    result[i,j] = img[i,j] 
                else:
                    result[i,j] = 0
            
            except IndexError as e:
                pass
    return result

def Thresholding(img, lowThresholdRatio = 0.05, highThresholdRatio= 0.25):
    highThreshold = img.max() * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio
    
    M, N = img.shape
    res = np.zeros((M,N), dtype=np.int32)
    
    weak = np.int32(25)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    return (res, weak, strong)                

def HysteresisTracking(img, weak, strong = 255):
    M, N = img.shape  
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (img[i,j] == weak):
                try:
                    if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                        or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                        or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return img

img = cv2.imread(r"D:\\Program_Languages\\Python\\Computer-Vision\\Image-Processing\\python_src\\lena.png")
R = img[:,:,2]
B = img[:,:,1]
G = img[:,:,0]

gray = np.uint8(0.298*R+0.588*B+0.114*G)

# lọc mịn ảnh
gauKernal = gaussian_kernal(5,1)
fgaus_img = tich_chap(gray, gauKernal)

# loc sac net sobel
SobelX = tich_chap(fgaus_img, locSobelX)
SobelY = tich_chap(fgaus_img, locSobelY)
Sobel = np.uint8(np.sqrt(SobelX**2 + SobelY**2))

# Loại bỏ các điểm cực đại
NMS_img = NMS(Sobel, SobelX, SobelY)

newimg, weak, strong  = Thresholding(NMS_img)

newimg1 = HysteresisTracking(newimg, weak, strong)


plt.subplot(2,4,1)
plt.imshow(img[:,:,::-1])
plt.title("Ảnh Màu")
plt.axis("off")

plt.subplot(2,4,2)
plt.imshow(gray, cmap = "gray")
plt.title("Ảnh da mức xám")
plt.axis("off")

plt.subplot(2,4,3)
plt.imshow(fgaus_img, cmap = "gray")
plt.title("Ảnh làm trơn")
plt.axis("off")

plt.subplot(2,4,4)
plt.imshow(Sobel, cmap = "gray")
plt.title("Ảnh biên độ và hướng")
plt.axis("off")

plt.subplot(2,4,5)
plt.imshow(NMS_img, cmap = "gray")
plt.title("Ảnh lọc cực đại giả")
plt.axis("off")

plt.subplot(2,4,6)
plt.imshow(newimg, cmap = "gray")
plt.title("Ảnh đã lọc ngưỡng")
plt.axis("off")


plt.subplot(2,4,7)
plt.imshow(newimg1, cmap = "gray")
plt.title("lọc kết quả cuối")
plt.axis("off")

plt.show()

