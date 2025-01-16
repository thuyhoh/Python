import numpy as np
import cv2

# img1 = np.zeros((250,500,3),np.uint8) 
# img1 = cv2.rectangle(img1,(250,0),(500,500),(255,255,255),-1)
img1 = cv2.imread("img.png")
img2 = cv2.imread("image_1.png")

        # bitwise operator
bit_and = cv2.bitwise_and(img1,img2)
bit_or = cv2.bitwise_or(img1,img2)
bit_xor = cv2.bitwise_xor(img1,img2)
bit_not = cv2.bitwise_not(img2)

# cv2.imshow("img1",img1)
# cv2.imshow("img2",img2)
# cv2.imshow("and",bit_and)
# cv2.imshow("or",bit_or)
# cv2.imshow("xor",bit_xor)
# cv2.imshow("not",bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
