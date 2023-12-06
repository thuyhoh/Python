import numpy as np

# using numpy.arrannge(start,stop,dtype)
    # start giá trị đầu // nếu ko có mặc định là 0
    # end giá trị kết thúc 
    # step bước nhảy giữa các giá trị
    # dtype kiểu dữ liệu trả về của giá trị
# print(np.arange(5))

# # vi du ham arnge co xac dinh du lieu 
# print(np.arange(5,dtype = float))

# # ham arange voi buoc nhay la 2
# print(np.arange(10,20,2))

#  using numpy.linspace(start,stop,num,endpoint,retstep,dtype)
    # start khoảng giá trị bắt đầu mặc định là 0
    # stop khoảng giá trị kết thúc
    # num số lượng mẫu cách đều sẽ được tạo ra 
    # endpoint mặc ddinhjj là true do đó giá trị dừng dược bao gồm trong chuỗi nếu sai nó không có giá trị đúng
    # rerstep nếu đúng trả về vavs giá trị lấy mẫu và giữa các số liên tiếp
    # dtype kiểu dữ liệu trả về của kết quả

# print(np.linspace(10,20,5))

# # ví dụ hafmm linspace có xác định endpoint
# print(np.linspace(10,20,9,endpoint = False))

# # hàm linspace có tính bước nhảy
# print(np.linspace(1,2,3,retstep = True))

# using numpy.logspace(start, stop, num, endpoint, retstep, dtype)
# start khoảng giá trị đầu 
# khoảng giá trị kết thúc 
# num số lượng mẫu cách đều nhau sẽ được tạo ra mặc định là 50
# endpoint mắc định là True, do đó giá trị dừng được bao gồm chuỗi. Nếu sai thì không có giá trị dùng
# base cố sở không gian tính toán mặc định là 10
# dtyoe: kiểu dữ liệu của kết quả

print(np.logspace(1,10,num = 10)) #10^i

# ví dụ hàm logspace có xác định cơ số
print(np.logspace(1,10,num = 10, base = 2)) # 2^i




