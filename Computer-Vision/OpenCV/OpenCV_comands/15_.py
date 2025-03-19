import cv2 
import numpy as np


img = cv2.imread("E:\\1.Language\\python\\sudoku.png",0)
_, th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY) # if pixel has value < 100 -> return 0(0->back) else return 1(255->while)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# cv2.ADAPTIVE_THRESH_MEAN_C : tính toán ngưỡng cho mỗi pixel dựa trên giá trị trung bình của các pixel xung quanh (khu vực lân cận).
# -> threshold = mean(neighborhood) - C <mean(neighborhood): giá trị trung bình của các ngưỡng lân cận>


th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C tương tự trên
# threshold = Σ (weight * pixel_value) - C


# cv2.adaptiveThreshold(src,max_value,adapter_method,threshold_type, block_size, c, dst); Applies adaptive thresholding to an image
# max_value: 255 Maximum value for pixels in the output image
# block_size: Size of the neighborhood area for calculating the threshold: (bock_size x block_size) pixels
# c 
# -> threshold = mean(neighborhood) - C



cv2.imshow("image",img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)




cv2.waitKey(0)
cv2.destroyAllWindows()