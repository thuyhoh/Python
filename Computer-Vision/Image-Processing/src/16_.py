import cv2
from matplotlib import pyplot as plt

img = cv2.imread("E:\\1.Language\\python\\lena_copy.jpg")
cv2.imshow("img",img) # read img(BGR)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # chuyen tu BGR -> RGB

plt.imshow(img) # read img(RGB)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
