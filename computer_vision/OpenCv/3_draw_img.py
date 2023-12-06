import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3],np.uint8) # create a frame which has [512,512] and bgr(0,0,0)<black> and datatype of element point 

img = cv2.line(img, (0,0), (255,255), (255,0,0), 5)# draw a blue line stat in point(0,0) and end in poitn (255,255) 
# cv2.line("nameimg","start_point","end_point","color(b,g,r)",'thik_of_line')

img = cv2.arrowedLine(img, (99,56), (255,255), (0,255,0), 5)# draw a gren arrowedline stat in point(0,0) and end in poitn (255,255) 

# draw a rectangle
img = cv2.rectangle(img,(300,100),(78,67),(0,0,255),7)# draw a red rectangel 

#   x1,y1 -----------
#   |                |
#   |                |
#   |                |
#   -------------x2,y2

# cv2.rectangle("name_img","top_point(x1,y1)","end_point(x2,y2)","color","thickness")
# note: if thickness == -1 -> fill all rectangle by color

# draw a circle
img = cv2.circle(img,(300,250),63,(20,50,200),8)
# cv2.circle("name_img","center_point","r",...)

# text
font = cv2.FONT_HERSHEY_DUPLEX # choice font of tex( hershey duplex)
img = cv2.putText(img,"new note",(10,500),font,4,(123,9,78),10,cv2.LINE_AA)
# cv2.putText("name_img","start_point","font_text","font_size","color(b,g,r)","thickness")




cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()