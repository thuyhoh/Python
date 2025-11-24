import numpy as np
import cv2

img = cv2.imread("messi5.jpg")
img2 = cv2.imread("opencv-logo.png")

print(img.shape) # return a tuple of number of  rows, columns, and channels
print(img.size)  # return total number of pixels is accessed
print(img.dtype) # return image datatype is obtained

sequen = []
b,g,r = cv2.split(img)      # frame will split into blue/green/red

img = cv2.merge((b,g,r))    # merge (b,g,r) to frame 



img = cv2.imread("messi5.jpg")
ball = img[280:340, 330:390]       # cut from (280,340) to (330,390) of frame -> ball
img[273:333 , 100:160] = ball     

img = cv2.resize(img,(512, 512))    # set size of frame
img2 = cv2.resize(img2,(512,512))   # set size of frame

# frame = cv2.resize(frame_name,(width,height))


dst = cv2.add(img2,img) # add two frame
# cv2.add(src1, src2, dst) => dst = cv2.add(src1, src2)

cv2.imshow('img1',dst)

dst2 = cv2.addWeighted(img, 0.9, img2, 0.1, 0) # dst = 0.9*img + 0.1*img2 + 0
# cv2.addWeighted(src1, %_src1, src2, %_src2, dst, gamma)
# dst = %_src1 * src1 + %_src2 * src2 + gamma


cv2.imshow('img2',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


