import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread("D:/Program_Languages/Python/Computer-Vision/OpenCV/lena.png")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5),np.float32)/25

dst = cv2.filter2D(img, -1, kernal)

# locj tan so thap
blur = cv2.blur(img, (5,5))

# loc gaussian tan so cao
gblur = cv2.GaussianBlur(img, (5,5), 0)

# loc trung vi
median = cv2.medianBlur(img, 5) # doi so thu 2 luon la so le

# loc song phuong -> muon giu nguyen vien 
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ["image", "2D Convolution", "blur", "GaussianBlur", "median", "bilateralFilter"]
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()