import cv2
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1208)  # set cv2.CAP_PROP_FRAME_WIDTH   = 1208
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,700)  # set cv2.CAP_PROP_FRAME_HEIGHT  = 700
# note: python will choice the nearest suitable frame for resolution 


print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        
        cv2.imshow('camera',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()