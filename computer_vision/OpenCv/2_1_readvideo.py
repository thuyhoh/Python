# read video or use cammera

import cv2

cap = cv2.VideoCapture(0) # use camera of laptop 
# cv2.VideoCapture('name_video')  if you want to watch video 

print(cap.isOpened()) # check camera or video is open 

while (cap.isOpened()): # while True:
    res,frame = cap.read() # res is boolen var
    # res = true -> is have frame 
    
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # print the width of frame
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # print the height of fream

    gray =  cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # comvert frame to gray
    cv2.imshow("frame",gray) 

    if cv2.waitKey(1) & 0xFF == ord('q'): # if you bress 'q' -> close camera's task
        break


cap.release() # clear frame 
cv2.destroyAllWindows() # close all the video windows