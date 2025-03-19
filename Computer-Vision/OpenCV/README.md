# Open CV - Python
## Install
- install thư viện
``` shell
pip install opencv2-python
```
- import thư viện 
``` Python
import cv2
```
tutorial course: [youtube-playlist link](https://www.youtube.com/playlist?list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K)
### II. Ảnh
#### 1. Đọc và ghi ảnh
``` Python
cv2.imread(filename= "image_path",flags= flags)
cv2.imwrite(filename= "image_path",img= flags)
``` 
#### 2. Hiển thị hình ảnh
``` Python
cv2.imshow("tên của cửa sổ hiển thị",img)
cv2.cv2.waitKey(0)
cv2.destroyAllWindows() 
```
#### 3. Lấy thông số của hình ảnh
``` Python
img = cv2.imread("image_path")
img.shape
img.size
img.dtype
cv2.split(img) 
crop_img = img[280:340, 330:390] 
cv2.resize(img,(512, 512))
cv2.add(img1,img2)
cv2.addWeighted(src1, %_src1, src2, %_src2, dst, gamma) # dst = %_src1 * src1 + %_src2 * src2 + gamma
cv2.pyrDown(img) # giảm độ phân giải của ảnh xuống một nửa 
cv2.pyrUp(img) # tăng độ phân giải của ảnh xuống một nửa 
cv2.cvtColor(image, mode)
```
#### 4. Phép toán trên ảnh
``` Python
img = cv2.add(img1, img2)
img = cv2.subtract(img1, img2) 
dst = cv2.absdiff(src1, src2) # dst = abs(src1-src2)
bit_and = cv2.bitwise_and(img1,img2)
bit_or = cv2.bitwise_or(img1,img2)
bit_xor = cv2.bitwise_xor(img1,img2)
bit_not = cv2.bitwise_not(img1)
"""
@brief: 
   Phép giãn nở lấy giá trị tối đa trong vùng được bao phủ bởi kernel tại mỗi vị trí pixel.
   Nếu bất kỳ pixel nào trong vùng kernel là 255 (trắng), pixel trung tâm sẽ thành 255.
@param[kernel]: Ma trận cấu trúc (structuring element) xác định hình dạng và kích thước của phép giãn nở.
@param[iterations]: Số lần lặp của phép giãn nở (mặc định là 1)
@retval: Ảnh kết quả sau khi giãn nở
"""
dst = cv2.dilate(src, kernel, iterations=1, borderType=cv2.BORDER_DEFAULT, borderValue=None)
```
#### 5. Vẽ trên ảnh
``` Python
cv2.line("nameimg","start_point","end_point","color(b,g,r)",'thik_of_line')

#   x1,y1 -----------
#   |                |
#   |                |
#   |                |
#   -------------x2,y2
cv2.rectangle("name_img","top_point(x1,y1)","end_point(x2,y2)","color","thickness") #thickness == -1 -> fill all rectangle by color

cv2.circle("name_img","center_point","r",...)

cv2.putText("name_img","start_point","font_text","font_size","color(b,g,r)","thickness")
```
### III. Video
#### 1. Đọc video/camera
``` Python
cap = cv2.VideoCapture(0) # camera
# cap = cv2.VideoCapture("video_path", img) # read video
res,frame = cap.read() # đọc từng frame trong video/camera
#   res-> boolean : true đọc được hình ảnh
#   frame -> matrix: ảnh đọc tại lúc gọi cap.read() 

while (cap.isOpened()): # while res==True:
   res,frame = cap.read()
   cv2.imshow("frame", frame)
   if cv2.waitKey(1) & 0xFF == ord('q'): # if you bress 'q' -> close camera's task
        break
cap.release()
cv2.destroyAllWindows() 
```
#### 2. Ghi lại video
``` Python
fourcc = cv2.VideoWriter_fourcc(*'XVID') #() ('X','V','I','D)-> ,avi/ *'mp4v' -> .mp4
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) # record and exploxe video in new file 
while (cap.isOpened()):
   res,frame = cap.read()
   if res:
      output.write(frame) # save frame in output file
   else:
      break
output.release()
cv2.destroyAllWindows() 
```
#### 3. Thay đổi thông số hiển thị camera
```
# lấy giá trị của khung hình hiển thị camera
cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

## thay đổi giá trị của cửa sổ hiển thị camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1208) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,700)  
```

### Windown
``` Python
cv2.namedWindow("Windown_name")
def callBack_funct:
   pass
cv2.createTrackbar("name_of_trackbar","Windown_name",start_point, end_point, callBack_funct)
cv2.getTrackbarPos("name_of_trackbar", "Windown_name")
```
### IV. Cải thiện ảnh
#### 1. histogram của ảnh
```Python
"""
@brief: tính histogram của một ảnh
"""
hist = cv2.calcHist()

"""
@brief: Cân bằng histogram
"""
hist_equal = cv2.equalHist(img)
```
#### 2. Áp dụng bộ lọc 
##### a. Bộ lọc Gaussian
```Python
"""
@brief: Áp dụng bộ lọc Gaussian lọc mịn ảnh
@param[ksize]: kích thước bộ lọc gaussian
@param[sigmaX]: Độ lệch chuẩn (standard deviation) của phân phối Gaussian theo trục X
@param[sigmaY]: Độ lệch chuẩn (standard deviation) của phân phối Gaussian theo trục Y
@retval: ảnh được lọc mịn
"""
dst = cv2.GaussianBlur(src, ksize, sigmaX, sigmaY=None, borderType=cv2.BORDER_DEFAULT)
```

### V. Xác định biên ảnh
#### 1. Gradient
##### a. Robert
##### b. Prewith 
##### c. Sobel 
#### 2. Laplacian
``` Python
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
```
#### 3. Thuật toán Canny
``` Python
edges = cv2.Canny(img,100,200)
```
### VI. Ngưỡng ảnh
``` Python
"""
@brief:
@param[thresh]
   Giá trị ngưỡng
@param[maxval]
   Giá trị tối đa được gán cho các pixel thỏa mãn điều kiện ngưỡng
@param[type]:
   cv2.THRESH_BINARY: Pixel ≥ thresh → maxval, ngược lại → 0.
   cv2.THRESH_BINARY_INV: Pixel ≥ thresh → 0, ngược lại → maxval.
   cv2.THRESH_TRUNC: Pixel > thresh → thresh, ngược lại giữ nguyên.
   cv2.THRESH_TOZERO: Pixel < thresh → 0, ngược lại giữ nguyên
   cv2.THRESH_TOZERO_INV: Pixel > thresh → 0, ngược lại giữ nguyên.
@retval:
   thresh: kết quả ảnh đã được đặt ngưỡng
   ret: true->thành công
"""
ret, thresh = cv2.threshold(src, thresh, maxval, type)
```
### VII. Vẽ đường viền của vật thể
``` Python
"""
@brief: tìm các đường viền (contours) trong một ảnh. findContours sẽ coi các vùng trắng (255) là đối tượng và vùng đen (0) là nền.
@param[mode]:
   cv2.RETR_EXTERNAL: Chỉ lấy các đường viền ngoài cùng
   cv2.RETR_LIST: Lấy tất cả đường viền, không xây dựng phân cấp
   cv2.RETR_CCOMP: Tổ chức đường viền thành hai cấp (ngoài và trong)
   cv2.RETR_TREE: Lấy tất cả đường viền và xây dựng cây phân cấp đầy đủ
@param[method]:
   cv2.CHAIN_APPROX_NONE: Lưu tất cả các điểm trên đường viền
   cv2.CHAIN_APPROX_SIMPLE: Chỉ lưu các điểm cần thiết, tiết kiệm bộ nhớ.
@retval:
   contours: Danh sách các đường viền mỗi đường viền là một tập hợp các điểm (point) biểu diễn ranh giới của một đối tượng
   hierarchy: Mảng phân cấp mô tả mối quan hệ giữa các đường viền
"""
contours, hierarchy = cv2.findContours(image, mode, method)

"""
@brief: xấp xỉ một đường viền (contour) thành một đa giác đơn giản hơn với ít điểm hơn
@param[curve]: cv2.findContours(image, mode, method)
@param[epsilon] = k * cv2.arcLength(curve, True), với k là hằng số
   Độ chính xác của phép xấp xỉ (khoảng cách tối đa giữa contour gốc và contour xấp xỉ).
   Giá trị nhỏ → xấp xỉ chi tiết hơn (giữ nhiều điểm hơn).
   Giá trị lớn → xấp xỉ thô hơn (ít điểm hơn).
@param[closed]:
   True: Contour được coi là khép kín (đa giác kín).
   False: Contour là đường cong hở
@retval: Contour xấp xỉ, là mảng NumPy chứa các điểm của đa giác đơn giản hơn.
"""
approx = cv2.approxPolyDP(curve, epsilon, closed)

"""
@brief: sử dụng để tính toán hình chữ nhật bao quanh (bounding rectangle) một đường viền (contour)
@retval:
   x: Tọa độ x của góc trên bên trái hình chữ nhật.
   y: Tọa độ y của góc trên bên trái hình chữ nhật.
   w: Chiều rộng (width) của hình chữ nhật.
   h: Chiều cao (height) của hình chữ nhật.
"""
x, y, w, h = cv2.boundingRect(contour)

"""
@brief: tính diện tích của một đường viền (contour)
@retval: trả về diện tích của một đường viền
"""
cv2.contourArea(contour)

"""
@brief:
@param[contours]: Danh sách các đường viền mỗi đường viền là một tập hợp các điểm (point) biểu diễn ranh giới của một đối tượng
@param[contourIdx]: 
   Nếu là -1: Vẽ tất cả các đường viền trong contours
   Nếu là một số cụ thể (ví dụ: 0, 1): Chỉ vẽ đường viền tương ứng với chỉ số đó (ví dụ: contours[0], contours[1])
@param[color]: Màu của đường viền, định dạng BGR (Blue, Green, Red).
@param[thickness]: Độ dày của đường viền (tính bằng pixel).
@retval:
"""
cv2.drawContours(image, contours, contourIdx, color, thickness)
```

### VIII. Khớp ảnh
```Python
"""
@brief: 
   sử dụng để thực hiện khớp mẫu (template matching),
   tìm kiếm vị trí của một mẫu (template) nhỏ trong một ảnh lớn hơn. 
   Nó trượt mẫu qua ảnh và tính toán độ tương đồng tại mỗi vị trí
@param[templ]:Mẫu (template) cần tìm, cũng là ảnh
@param[method]:
   cv2.TM_SQDIFF: Tổng bình phương sai (nhỏ hơn = khớp tốt hơn).
   cv2.TM_SQDIFF_NORMED: Tổng bình phương sai chuẩn hóa.
   cv2.TM_CCORR: Tương quan chéo (lớn hơn = khớp tốt hơn).
   cv2.TM_CCORR_NORMED: Tương quan chéo chuẩn hóa (giá trị từ 0 đến 1).
   cv2.TM_CCOEFF: Hệ số tương quan.
   cv2.TM_CCOEFF_NORMED: Hệ số tương quan chuẩn hóa.
@retval: Ma trận (mảng NumPy 2D) chứa giá trị độ tương đồng tại mỗi vị trí
"""
result = cv2.matchTemplate(image, templ, method, mask=None)
```


28