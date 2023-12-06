import cv2

img = cv2.imread(filename= 'jk.jpg',flags= -1) # flags = 0(img's color = gray); = 1(normal); = -1()

print(img)

cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("lena_copyfile.png",img) # create and copy 'img' to newfile "lena_copyfile.png"
    cv2.destroyAllWindows()