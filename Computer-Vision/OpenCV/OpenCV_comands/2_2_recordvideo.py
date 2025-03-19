import cv2

cap = cv2.VideoCapture(0) 

fourcc = cv2.VideoWriter_fourcc(*'XVID') #() ('X','V','I','D)-> ,avi/ *'mp4v' -> .mp4
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) # record and exploxe video in new file 
# cv2.VideoWriter('name_file','fourcc code', 'frame per seconds', "size of frame")

print(cap.isOpened()) # check camera or video is open 
while (cap.isOpened()):
    res,frame = cap.read()
    if res == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

        output.write(frame) # save frame in output file

        
        cv2.imshow("frame",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break
output.release() # clear output memory
cap.release()  
cv2.destroyAllWindows() 