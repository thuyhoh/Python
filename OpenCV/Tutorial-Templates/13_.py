import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")

cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)

cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while True:
    frame = cv2.imread("D:/Program_Languages/Python/Computer-Vision/OpenCV/lena.png")

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # convert frame from BGR ->  HSV

    l_h = cv2.getTrackbarPos("LH","Tracking")
    l_s = cv2.getTrackbarPos("LS","Tracking")
    l_v = cv2.getTrackbarPos("LV","Tracking")

    u_h = cv2.getTrackbarPos("UH","Tracking")
    u_s = cv2.getTrackbarPos("US","Tracking")
    u_v = cv2.getTrackbarPos("UV","Tracking")


    low_blue = np.array([l_h,l_s,l_v])    # the lowest of blue
    up_blue = np.array([u_h,u_s,u_v])   # the highest of blue

    mask = cv2.inRange(hsv,low_blue,up_blue) # create a mask for blue pixels in the frame
    # cv2,imRange() -> will return the binary frame from lower ->uper


    result = cv2.bitwise_and(frame ,frame, mask = mask) # result = mask & (frame and frame)
    # cv2.bitwise_and(src1, src2, dst, mask )
    # mask is the frame which pixels will be retained in the result

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result",result)
    


    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()