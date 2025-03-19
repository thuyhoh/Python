import cv2 
import numpy as np

ing = cv2.imread("gradient.png")

img = cv2.imread("D:/Program_Languages/Python/Computer-Vision/OpenCV/lena.png",0)
_, th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY) # if pixel has value < 100 -> return 0(0->back) else return 1(255->while)
_, th2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV) # th2 = inv(th1) 
_, th3 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC) # if pixel > 100 ->  return 100
_, th4 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO) # if pixel < 100 -> return 0 
_, th5 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV) #if pixel > 100 -> return 0



cv2.imshow("image",img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.imshow("th4",th4)
cv2.imshow("th5",th5)



cv2.waitKey(0)
cv2.destroyAllWindows()