import cv2
import numpy as np
from matplotlib import pyplot as plt

f_tb_3x3 = np.float16(1/9 * np.ones([3,3]))

# Định nghĩa Robert Cross theo hướng chéo 1
loc_Robert_Cross1 = np.array((
                              [-1, 0],
                              [ 0, 1]), dtype="float")

# Định nghĩa Robert Cross theo hướng chéo 2
loc_Robert_Cross2 = np.array((
                              [ 0,-1],
                              [1, 0]), dtype="float")


# Định nghĩa Sobel theo hướng X
locSobelX = np.array(([-1,-2,-1],
                      [ 0, 0, 0],
                      [ 1, 2, 1]), dtype="float")

# Định nghĩa bộ lọc Sobel theo hướng Y
locSobelY = np.array(([-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]), dtype="float")

# kirsch_a

kirsch_1 = np.array(([ 5, 5, 5],
                     [-3, 0, -3],
                     [-3, -3, -3]   ), dtype = float)

kirsch_2 = np.array(([-3, 5, 5],
                     [-3, 0, 5],
                     [-3,-3, -3]   ), dtype = float)

kirsch_3 = np.array(([ -3, -3, 5],
                     [-3, 0, 5],
                     [-3, -3, 5]   ), dtype = float)

kirsch_4 = np.array(([ -3, -3, -3],
                     [-3, 0, 5],
                     [-3, 5, 5]   ), dtype = float)

kirsch_5 = np.array(([ -3, -3, -3],
                     [-3, 0, -3],
                     [5, 5, 5]   ), dtype = float)           

kirsch_6 = np.array(([ -3, -3, -3],
                     [5, 0, -3],
                     [5, 5, -3]   ), dtype = float)        

kirsch_7 = np.array(([ 5, -3, -3],
                     [5, 0, -3],
                     [5, -3, -3]   ), dtype = float)             

kirsch_8 = np.array(([ 5, 5, -3],
                     [5, 0, -3],
                     [-3, -3, -3]   ), dtype = float)   



# bộ lọc prewith
prewith_x = np.array(([ 1, 1, 1],
                      [ 0, 0, 0 ],
                      [ -1,-1, -1 ]   ), dtype = float
)

prewith_y = np.array(([ -1, 0, 1],
                      [-1, 0,1],
                      [ -1, 0, 1]   ), dtype = float
)


def tich_chap(img , kernel):
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


img = cv2.imread(r"D:\\Program_Languages\\Python\\Computer-Vision\\Image-Processing\\python_src\\lena.png")
R = img[:,:,2]
B = img[:,:,1]
G = img[:,:,0]

gray = np.uint8(0.298*R+0.588*B+0.114*G)


# loc robert
rbc1 = tich_chap(gray, loc_Robert_Cross1)

rbc2 = tich_chap(gray, loc_Robert_Cross2)

rbc = np.sqrt(rbc1**2 + rbc2**2)

# loc sobel
sobx = tich_chap(gray, locSobelX)
soby = tich_chap(gray, locSobelY)

sob =  np.sqrt(sobx**2 + soby**2)

# loc prewith
prewx = tich_chap(gray, prewith_x)
prewy = tich_chap(gray, prewith_y)

prew = np.sqrt(prewx**2 + prewy**2)

# loc Kirsch 
kir1 = tich_chap(gray, kirsch_1)
kir2 = tich_chap(gray, kirsch_2)
kir3 = tich_chap(gray, kirsch_3)
kir4 = tich_chap(gray, kirsch_4)
kir5 = tich_chap(gray, kirsch_5)
kir6 = tich_chap(gray, kirsch_6)
kir7 = tich_chap(gray, kirsch_7)
kir8 = tich_chap(gray, kirsch_8)

h, w = kir1.shape
kir = np.zeros([h,w])

for i in range(h):
    for j in range(w):
        kir[i,j] = max(kir1[i,j], kir2[i,j], kir3[i,j], kir4[i,j], kir5[i,j], kir6[i,j], kir7[i,j], kir8[i,j])

plt.subplot(2,3,1)
plt.imshow(img[:,:,::-1])
plt.title("Ảnh màu")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(gray, cmap= "gray")
plt.title("Ảnh màu")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(rbc, cmap= "gray")
plt.title("Ảnh lọc robert")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(sob, cmap= "gray")
plt.title("Ảnh lọc sobel")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(prew, cmap= "gray")
plt.title("Ảnh lọc prewith")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(kir, cmap= "gray")
plt.title("Ảnh lọc Kirsch")
plt.axis("off")

plt.show()
