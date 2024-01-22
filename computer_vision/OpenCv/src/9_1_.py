import numpy as np
import cv2

def click_even(event, x, y, flags, praram):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y),3,(0,0,155),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(255,0,0),6)
        cv2.imshow("img",img)
    

img = cv2.imread("lena.jpg")
cv2.imshow("img",img)
points = []

cv2.setMouseCallback("img",click_even)
 
cv2.waitKey(0)
cv2.destroyAllWindows()