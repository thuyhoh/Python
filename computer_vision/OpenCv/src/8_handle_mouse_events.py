import numpy as np
import cv2


def click_event (event, x, y, flags, param):
    # flags and praram is necessary

    if event == cv2.EVENT_LBUTTONDOWN: # when click left button mouse
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(x) + "," +str(y)
        cv2.putText(img,strXY,(x,y),font, 1, (150,255,0), 2)
        cv2.imshow("img",img)
    if event == cv2.EVENT_RBUTTONDOWN: # when click right button mouse
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strBGR = str(blue) + "," +str(green) + ", "+str(red)
        cv2.putText(img,strBGR,(x,y),font, 1, (0,255,255), 2)
        cv2.imshow("img",img)

#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("messi5.jpg")
cv2.imshow("img",img)

cv2.setMouseCallback("img",click_event)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
