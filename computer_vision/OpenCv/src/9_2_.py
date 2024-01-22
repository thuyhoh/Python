import numpy as np
import cv2

def click_even(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        
        blue = img[x,y,0]   # get value of blue in the point(x,y)
        green = img[x,y,1]  # get value of blue in the point(x,y)
        red = img[x,y,2]    # get value of blue in the point(x,y)
        print(str(blue)+" "+str(green)+" "+str(red))

        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolor_img = np.zeros((512,512,3),np.uint8)
        mycolor_img[:] = [blue,green,red] # set color of mycolor_img = (blue,green,red) 

        cv2.imshow("color",mycolor_img) # show color in the new tab
    

img = cv2.imread("jk.jpg")
cv2.imshow("img",img)
points = []

cv2.setMouseCallback("img",click_even)
 
cv2.waitKey(0)
cv2.destroyAllWindows()