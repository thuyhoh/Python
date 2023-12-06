import cv2
import datetime
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_PLAIN
        
        # put text in the frame 

        # print width and height of frame into display
        text = "Width: "+ str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+" Height: " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cv2.putText(frame,text,(420,50),font,1,(0,255,255),2)
        
        # print the time into the display
        date = str(datetime.datetime.now())
        cv2.putText(frame,date,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        
        
        cv2.imshow('camera',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()