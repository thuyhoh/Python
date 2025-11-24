# Open CV - Python
### Install
- install thư viện
``` shell
pip install opencv2-python
pip install opencv-contrib-python
```
- import thư viện 
``` Python
import cv2
```
- tutorial course: [youtube-playlist link](https://www.youtube.com/playlist?list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K)
### I. Windown
#### 1. Khởi tạo một cửa sổ hiển thị
``` Python
"""
@param[flags]
   cv2.WINDOW_NORMAL : Cửa sổ có thể thay đổi kích thước bằng chuột.
   Hữu ích khi hình ảnh/video lớn hơn màn hình.
   cv2.WINDOW_AUTOSIZE: Cửa sổ tự động điều chỉnh kích thước theo nội dung (hình ảnh/video).
   Không thể thay đổi kích thước bằng tay.
   cv2.WINDOW_FULLSCREEN: Cửa sổ hiển thị toàn màn hình.
   cv2.WINDOW_KEEPRATIO: Giữ tỷ lệ khung hình khi thay đổi kích thước (kết hợp với WINDOW_NORMAL).
"""
cv2.namedWindow(winname, flags=None)
```
#### 2. Hủy toàn bộ cửa sổ
``` Python
cv2.destroyAllWindows() 
```
#### 3. Chờ phím được nhấn
``` Python
"""
@brief: đợi một phím được nhấn từ bàn phím 
@param[delay]: 
   Nếu delay=0: Đợi vô hạn cho đến khi có phím được nhấn.
   Nếu delay>0: Đợi số mili-giây được chỉ định
@retval: trả về mã ASCII của phím được nhấn
"""
cv2.waitKey(delay=0)

"""
@brief: chuyển một ký tự đơn thành mã ASCII
@retval: trả về mã ASCII của ký tự c
"""
ord(c)
```
#### 4. Trackbar
``` Python
"""
@brief: Tạo Trackbar(thanh trượt)
@param[trackbarName]: tên của thanh trượt
@param[windowName]: Cửa sổ chưa thanh chượt
@param[value]: Giá trị ban đầu của thanh trượt
@param[count]: Giá trị tối đa của thanh trượt [0, count]
@param[onChange]: Hàm callback được gọi mỗi khi thanh trượt thay đổi.
"""
cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
"""
@brief: lấy giá trị từ Trackbar
@retval: giá trị Trackbar
"""
Trackbar_val = cv2.getTrackbarPos(trackbarname, winname)
```
### II. Ảnh
#### 1. Đọc ảnh
``` Python
"""
@param[flags]:
   cv2.IMREAD_COLOR: Đọc hình ảnh dưới dạng màu BGR
   cv2.IMREAD_GRAYSCALE: Đọc hình ảnh dưới dạng ảnh xám
   cv2.IMREAD_UNCHANGED: Đọc hình ảnh nguyên bản, bao gồm kênh alpha
"""
img = cv2.imread(filename,flags)
```
#### 2. Ghi lại ảnh
``` Python
cv2.imwrite(filename, img, params=None)
``` 
#### 3. Chuyển đổi không gian ảnh 
``` Python
"""
@param[code]: 
   cv2.COLOR_BGR2RGB: Chuyển từ BGR (mặc định trong OpenCV) sang RGB.
   cv2.COLOR_RGB2BGR: Chuyển từ RGB sang BGR.
   cv2.COLOR_BGR2GRAY: Chuyển từ BGR sang ảnh xám (grayscale).
   cv2.COLOR_RGB2GRAY: Chuyển từ RGB sang ảnh xám.
   cv2.COLOR_BGR2HSV: Chuyển từ BGR sang HSV (Hue, Saturation, Value).
   cv2.COLOR_RGB2HSV: Chuyển từ RGB sang HSV.
@retval: hình ảnh đã được chuyển đổi
"""
dst = cv2.cvtColor(img, code)
```
#### 4. Hiển thị hình ảnh
``` Python
cv2.imshow(winname,img)
```
#### 5. Lấy thông số của hình ảnh
- Kích thước ảnh
``` Python
height, width, channels = img.shape # kích thước của ảnh
size = img.size                     # tổng pixel của ảnh
```
- Tách kênh màu
``` Python
blue, green, red = cv2.split(img)
``` 
- trích xuất một phần (crop) của hình ảnh
``` Python
crop_img = img[280:340, 330:390] 
```
- định hình lại độ phân giải(kích thước) ảnh
``` Python
cv2.resize(img,(height x width))
```
- Tăng/giảm độ phân giải(height x width) của ảnh
``` Python 
cv2.pyrDown(img) # giảm độ phân giải của ảnh xuống một nửa 
cv2.pyrUp(img) # tăng độ phân giải của ảnh xuống một nửa 
```
#### 6. Phép toán trên ảnh
##### a. Phép toán
- Phép cộng
``` Python
img = cv2.add(img1, img2)
```
- Phép cộng có trọng số
``` Python
# dst = %_src1 * src1 + %_src2 * src2 + gamma
cv2.addWeighted(src1, %_src1, src2, %_src2, dst, gamma) 
```
- Phép trừ
``` Python
img = cv2.subtract(img1, img2) 
```
- phép trừ tuyệt đối
``` Python
dst = cv2.absdiff(src1, src2) # dst = abs(src1-src2)
```
##### b. Phép bitwise
- phép and
``` Python
bit_and = cv2.bitwise_and(img1,img2)
```
- Phép or
``` Python
bit_or = cv2.bitwise_or(img1,img2)
```
- Phép not
``` Python
bit_not = cv2.bitwise_not(img1)
```
- Phép xor
``` Python 
bit_xor = cv2.bitwise_xor(img1,img2)
```
##### c. Phép giãn nở
``` Python
"""
@brief: áp dụng mạnh trên ảnh nhị phân 
   Phép giãn nở lấy giá trị tối đa trong vùng được bao phủ bởi kernel tại mỗi vị trí pixel.
   Nếu bất kỳ pixel nào trong vùng kernel là 255 (trắng), pixel trung tâm sẽ thành 255.
@param[kernel]: Ma trận cấu trúc (structuring element) xác định hình dạng và kích thước của phép giãn nở.
@param[iterations]: Số lần lặp của phép giãn nở (mặc định là 1)
@retval: Ảnh kết quả sau khi giãn nở
"""
dst = cv2.dilate(src, kernel, iterations=1, borderType=cv2.BORDER_DEFAULT, borderValue=None)
```
##### d. Phép toán hình thái học
- tạo ra cấu trúc 
``` Python
"""
@brief: tạo một đối tượng phân tách nền (background subtractor) 
   dựa trên mô hình hỗn hợp Gaussian (Mixture of Gaussians - MOG)
@history (mặc định: 200): Số lượng khung hình trước đó được sử dụng để xây dựng mô hình hậu cảnh
nmixtures (mặc định: 5): Số lượng phân phối Gaussian tối đa cho mỗi pixel
backgroundRatio (mặc định: 0.7): 
   Tỷ lệ xác định ngưỡng để phân loại một pixel là hậu cảnh. 
   Nếu tổng trọng số của các Gaussian thuộc hậu cảnh vượt quá ngưỡng này, pixel được coi là hậu cảnh.
oiseSigma (mặc định: 0): Độ lệch chuẩn của nhiễu Gaussians
"""
fgbg = cv.bgsegm.createBackgroundSubtractorMOG(history=200, nmixtures=5, backgroundRatio=0.7, noiseSigma=0)
"""
```
- phép toán hình thái học
``` Python
"""
op: Phép toán hình thái học được thực hiện. Các giá trị có thể là:
   cv.MORPH_OPEN: Phép mở (erosion rồi dilation) - loại bỏ nhiễu nhỏ, giữ các đối tượng lớn.
   cv.MORPH_CLOSE: Phép đóng (dilation rồi erosion) - lấp đầy lỗ nhỏ, kết nối các vùng gần nhau.
   cv.MORPH_GRADIENT: Gradient hình thái (dilation trừ erosion) - trích xuất biên của đối tượng.
   cv.MORPH_TOPHAT: Top-hat (ảnh gốc trừ phép mở) - làm nổi bật các chi tiết sáng nhỏ.
   cv.MORPH_BLACKHAT: Black-hat (phép đóng trừ ảnh gốc) - làm nổi bật các chi tiết tối nhỏ.
   cv.MORPH_HITMISS: Hit-or-miss (tìm kiếm mẫu cụ thể) - ít dùng hơn, yêu cầu kernel đặc biệt.
kernel: Phần tử cấu trúc (structuring element)
    thường được tạo bằng cv.getStructuringElement().
"""
dst = cv.morphologyEx(src, op, kernel, anchor=None, iterations=1, borderType=cv.BORDER_CONSTANT, borderValue=None)
```
#### 7. Vẽ trên ảnh
##### a.vẽ đường thăngt
``` Python
"""
@param[pt1]: Tọa độ điểm đầu của đường thẳng (tuple (x1, y1))
@param[pt2]: Tọa độ điểm cuối của đường thẳng (tuple (x2, y2))
@param[color]: Màu của đường thẳng (tuple (B, G, R)
@param[thickness]: Độ dày của đường thẳng (integer), mặc định là 1
@param[lineType]: Kiểu đường thẳng:
   cv2.LINE_4: Đường 4 kết nối
   cv2.LINE_8: Đường 8 kết nối
   cv2.LINE_AA: Đường khử răng cưa 
"""
cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
```
##### b.vẽ hình chữ nhật
``` Python
"""
@param[pt1]: Tọa độ góc trên bên trái của hình chữ nhật (tuple (x1, y1))
@param[pt2]: Tọa độ góc dưới bên phải của hình chữ nhật (tuple (x2, y2))
"""
cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
```
##### c.Vẽ hình tròn
``` Python
"""
@param[center]: Tọa độ tâm của đường tròn (tuple (x, y))
@param[radius]: Bán kính của đường tròn 
"""
cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
```
##### d. Viết ký tự
``` Python
"""
@param[text]: Chuỗi văn bản cần vẽ
@param[fontFace]: Kiểu phông chữ
   cv2.FONT_HERSHEY_SIMPLEX: Phông đơn giản, dễ đọc.
   cv2.FONT_HERSHEY_PLAIN: Phông nhỏ, gọn.
   cv2.FONT_HERSHEY_DUPLEX: Phông đôi nét.
   cv2.FONT_HERSHEY_COMPLEX: Phông phức tạp, giống serif.
   cv2.FONT_HERSHEY_TRIPLEX: Phông ba nét.
@param[fontScale]: Tỷ lệ kích thước phông chữ (float)
@param[color]: Màu của văn bản (tuple (B, G, R))
@param[bottomLeftOrigin]: 
   Nếu True, điểm gốc (x, y) sẽ là góc dưới bên trái của văn bản
   Nếu False, điểm gốc là góc trên bên trái.
"""
cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)
```
### III. Video
#### 1. Mở và đọc video/camera
``` Python
# mở camera
cap = cv2.VideoCapture(index)
# đọc video
cap = cv2.VideoCapture(filename)
```
#### 2. Đọc khung hình trong video
``` Python
"""
ret: True nếu đọc thành công, False nếu thất bại
frame: Mảng NumPy chứa dữ liệu khung hình
"""
res,frame = cap.read() 
```
#### 3. Ghi lại video
- Tạo mã FourCC (Four-Character Code)
``` Python
"""
@param["FourCC"]: 
   "XVID": Xvid - Codec MPEG-4, hiệu quả nén tốt, thường dùng cho AVI.
   "MP4V": MPEG-4 Video - Thường dùng cho MP4.
"""
fourcc = cv2.VideoWriter_fourcc(*"FourCC")
```
- Ghi lại video
``` Python
"""
@param[filename]: 
   "XVID" -> filename.avi
   "MP4V" -> filename.mp4
@param[fourcc]: mã FourCC
@param[fps]: Tốc độ khung hình trên giây
@param[frameSize]: (width, height)
@param[isColor]: 
   True: Ghi video màu
   False: Ghi lại video xám
@retval: Trả về một đối tượng VideoWriter để ghi video
"""
output = cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=True)

"""
@brief: Ghi lại khung hình vào video output
"""
output.write(frame)
```
#### 4. Lấy/đặt thuộc tính của video
- Lấy/đặt thuộc tính của video
``` Python
"""
@brief: Lấy thuộc tính của video/webcam
@param[propId]:
   cv2.CAP_PROP_FRAME_WIDTH: Chiều rộng của khung hình (pixel).
   cv2.CAP_PROP_FRAME_HEIGHT: Chiều cao của khung hình (pixel).
   cv2.CAP_PROP_FPS: Tốc độ khung hình mỗi giây fps.
   cv2.CAP_PROP_FRAME_COUNT: Tổng số khung hình trong video(!= webcam)
   cv2.CAP_PROP_POS_FRAMES: Vị trí khung hình hiện tại (bắt đầu từ 0).
   cv2.CAP_PROP_POS_MSEC: Vị trí hiện tại tính bằng mili-giây (thời gian kể từ đầu video).
   cv2.CAP_PROP_FORMAT: Định dạng của dữ liệu khung hình.
   cv2.CAP_PROP_BRIGHTNESS: Độ sáng (chỉ áp dụng cho camera nếu hỗ trợ).
   cv2.CAP_PROP_CONTRAST: Độ tương phản (chỉ áp dụng cho camera nếu hỗ trợ).
"""
cap.get(propId)

"""
@brief: Đặt thuộc tính của video/webcam
"""
cap.set(propId, value) 
```
- Kiểm tra video đã mở thành công hay chưa
``` Python
while cap.isOpened(): # while ret:
```
#### 5. Giải phóng tài nguyên video
``` Python
video.release()
```
#### Code mẫu
``` Python
# đọc video
cap = cv2.VideoCapture(0) 
res,frame = cap.read() 

# ghi lại video
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
output = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480)) 

# Kiểm tra mở video thành công hay không
while (cap.isOpened()): 
   res,frame = cap.read()
   cv2.imshow("frame", frame)
   output.write(frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
        break

output.release()
cap.release()
cv2.destroyAllWindows() 
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
##### a. Bộ lọc trung vị
``` Python
"""
ksize: Kích thước của cửa sổ lọc (chỉ nhận giá trị lẻ,
"""
dst = cv2.medianBlur(src, ksize)
```
##### b. Bộ lọc trung bình
##### c. Bộ lọc Gaussian
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
"""
@param[ddepth]: Độ sâu (data type) của ảnh đầu ra (ví dụ: cv2.CV_64F để tránh mất dữ liệu do giá trị âm).
@param[ksize]: Kích thước của kernel Sobel dùng để tính đạo hàm (mặc định là 1, phải là số lẻ: 1, 3, 5, ...).
@param[scale]: Hệ số tỉ lệ áp dụng cho kết quả (mặc định là 1).
@param[delta]: Giá trị cộng thêm vào kết quả trước khi trả về (mặc định là 0).
@param[borderType] : Phương pháp xử lý biên ảnh (mặc định là cv2.BORDER_DEFAULT)
"""
dst = cv2.Laplacian(src, ddepth, [ksize], [scale], [delta], [borderType])
```
#### 3. Thuật toán Canny
``` Python
"""
@param[threshold1]: Ngưỡng thấp (lower threshold) để xác định cạnh yếu.
@param[threshold2]: Ngưỡng cao (upper threshold) để xác định cạnh mạnh.
@param[apertureSize]: Kích thước của bộ lọc Sobel (mặc định là 3).
@param[L2gradient]: 
   Nếu True, dùng công thức L2 để tính gradient; 
   nếu False, dùng L1.
"""
edges = cv2.Canny(image, threshold1, threshold2, [apertureSize], [L2gradient])
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
### VII. Phát hiện vật thể
#### 1. tìm các đường viền
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
```
#### 2. Thu thập đường viên thành đa giác đơn 
``` Python
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
```
#### 3. vẽ và tô màu một đa giác (polygon) trên ảnh
``` Python
"""
@param[pts]: Danh sách các mảng chứa tọa độ các đỉnh của đa giác. Mỗi mảng là một tập hợp các điểm (x, y) kiểu NumPy array 
@param[color]: Màu sắc để tô đa giác, định dạng (B, G, R) cho ảnh màu hoặc giá trị xám cho ảnh grayscale.
@param[shift]: Số bit dịch phải của tọa độ 
"""
cv2.fillPoly(img, pts, color, [lineType], [shift])
```
#### 3. Tìm tọa dộ hình chữ nhật nhỏ nhất bao quanh vật thể
``` Python
"""
@brief: sử dụng để tính toán hình chữ nhật bao quanh (bounding rectangle) một đường viền (contour)
@retval:
   x: Tọa độ x của góc trên bên trái hình chữ nhật.
   y: Tọa độ y của góc trên bên trái hình chữ nhật.
   w: Chiều rộng (width) của hình chữ nhật.
   h: Chiều cao (height) của hình chữ nhật.
"""
x, y, w, h = cv2.boundingRect(contour)
```
#### 4. Tính toán diện tích viền bao quanh vật thể
``` Python
"""
@brief: tính diện tích của một đường viền (contour)
@retval: trả về diện tích của một đường viền
"""
cv2.contourArea(contour)
```
#### 5. Vẽ đường biên 
``` Python
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

#### 6. Phát hiện đoạn thẳng trong ảnh
``` Python
"""
@brief: phát hiện các đoạn thẳng trong ảnh dựa trên phiên bản Hough Transform
rho: Độ phân giải của ρ (khoảng cách) tính bằng pixel (thường là 1).
theta: Độ phân giải của θ (góc) tính bằng radian 
threshold: Ngưỡng số phiếu tối thiểu để một đường được coi là hợp lệ.
srn, stn : Độ phân giải tinh chỉnh cho phiên bản Probabilistic Hough Transform 
min_theta, max_theta : Phạm vi góc θ để giới hạn các đường cần tìm (mặc định là 0 đến π).
"""
lines = cv2.HoughLines(image, rho, theta, threshold, [srn], [stn], [min_theta], [max_theta])
"""
@brief: phát hiện các đoạn thẳng trong ảnh dựa trên phiên bản Probabilistic Hough Transform
minLineLength : Độ dài tối thiểu của đoạn thẳng (tính bằng pixel)
maxLineGap : Khoảng cách tối đa giữa hai đoạn thẳng để chúng được nối thành một
"""
lines = cv2.HoughLinesP(image, rho, theta, threshold, [minLineLength], [maxLineGap])
```
#### 7. Phát hiện hình tròn trong ảnh
``` python
"""
@brief: Phát hiện các đường tròn trong ảnh bằng phương pháp Biến đổi Hough
method: Phương pháp phát hiện, chỉ hỗ trợ cv2.HOUGH_GRADIENT.
dp: Tỉ lệ giảm kích thước ảnh. Nếu dp=1, ảnh không bị giảm, nếu dp=2, ảnh bị giảm một nửa trước khi xử lý.
minDist: Khoảng cách tối thiểu giữa tâm của các đường tròn được phát hiện.
param1: Ngưỡng trên cho bộ lọc cạnh Canny (thường khoảng 100-200).
param2: Ngưỡng để phát hiện đường tròn (giá trị càng thấp càng dễ phát hiện nhiều đường tròn).
minRadius: Bán kính tối thiểu của đường tròn cần phát hiện.
maxRadius: Bán kính tối đa của đường tròn cần phát hiện.
"""
circles = cv2.HoughCircles(image, method, dp, minDist, param1=None, param2=None, minRadius=0, maxRadius=0)
```
#### 8. Khớp ảnh
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
#### 9. Phát hiện góc trong ảnh
``` Python
"""
@brief
src	Ảnh đầu vào (ảnh xám - grayscale, kiểu float32).
blockSize	Kích thước của vùng cửa sổ để tính ma trận gradient (thường là 2 hoặc 3).
ksize	Kích thước của bộ lọc Sobel (chỉ nhận giá trị lẻ: 3, 5, 7).
k	Tham số Harris detector (thường từ 0.04 đến 0.06).
@retval: danh sách các tọa độ (x, y) của các góc được phát hiện trong ảnh.
"""
dst = cv.cornerHarris(src, blockSize, ksize, k)

"""
@brief: các góc quan trọng (good features/corners) trong ảnh bằng thuật toán Shi-Tomasi Corner Detection
maxCorners	Số lượng góc tối đa cần phát hiện (đặt 0 để không giới hạn).
qualityLevel	Ngưỡng chất lượng góc (từ 0 đến 1, thường khoảng 0.01 - 0.1).
minDistance	Khoảng cách tối thiểu giữa hai góc (nếu quá nhỏ, các góc gần nhau sẽ bị loại bỏ).
mask	(Tùy chọn) Ảnh mask để giới hạn vùng phát hiện.
blockSize	Kích thước cửa sổ để tính toán ma trận gradient.
useHarrisDetector	True nếu muốn dùng Harris Corner Detection thay vì Shi-Tomasi.
k	Tham số của Harris Detector (chỉ dùng nếu useHarrisDetector=True).
@retval: danh sách các tọa độ (x, y) của các góc được phát hiện trong ảnh.
"""
corners = cv.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, mask=None, blockSize=3, useHarrisDetector=False, k=0.04)

```
#### 10. Phát hiện đối tượng
``` Python
"""
@brief: phát hiện đối tượng trong ảnh hoặc video bằng phương pháp Haar Cascade Classifier
@param[filename]: file huấn luyện Haar Cascade.xml
"""
cascade = cv2.CascadeClassifier(filename)
"""
@brief:  phát hiện các đối tượng trong ảnh, như khuôn mặt, mắt, nụ cười, v.v., bằng cách sử dụng các mô hình Haar Cascade hoặc LBP

image	Ảnh đầu vào (phải là ảnh xám - grayscale).
scaleFactor	Hệ số thay đổi kích thước mỗi lần quét (thường từ 1.1 - 1.3).
minNeighbors	Số lần một đối tượng cần được phát hiện trước khi xác nhận (giá trị lớn giúp giảm phát hiện sai).
flags	Thường đặt là 0 hoặc cv2.CASCADE_SCALE_IMAGE (mặc định).
minSize	Kích thước nhỏ nhất của đối tượng cần phát hiện.
maxSize	Kích thước lớn nhất của đối tượng cần phát hiện (có thể bỏ qua).
"""
objects = cascade.detectMultiScale(image, scaleFactor, minNeighbors, flags, minSize, maxSize)
```
#### 11. Phân tách nền
``` Python

"""
dùng để tạo một đối tượng phân tách nền dựa trên thuật toán GMG
"""
fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
"""

"""
fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=True)
"""
dùng để tạo một đối tượng phân tách nền dựa trên thuật toán KNN
"""
fgbg = cv.createBackgroundSubtractorKNN(detectShadows=True)
```
- tạo mặt nạ tiền cành
``` Python
"""
@brief: được sử dụng để áp dụng thuật toán phân tách nền lên một khung hình (frame) của ảnh hoặc video, từ đó tạo ra một mặt nạ tiền cảnh
image: Khung hình đầu vào, thường là ảnh xám (grayscale) hoặc ảnh màu tùy thuộc vào thuật toán. Đối với BackgroundSubtractorMOG, ảnh xám thường được sử dụng.
learningRate (mặc định: -1): Tốc độ học của mô hình, nằm trong khoảng [0, 1]
   0: Không cập nhật mô hình hậu cảnh (chỉ phân tách mà không học thêm).
   1: Cập nhật mô hình hoàn toàn dựa trên khung hình hiện tại.
   -1: Tự động chọn tốc độ học dựa trên thiết kế của thuật toán.
@retval: Một ảnh nhị phân (binary mask) cùng kích thước với image
"""
fgbg.apply(image, learningRate=-1)
```