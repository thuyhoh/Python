import xlsxwriter
import pandas as pd
import os


# Tạo file
wb = xlsxwriter.Workbook("file excel được tao.xlsx")
ws1 = wb.add_worksheet("Dữ liệu sheet")
ws1.write(1,0,"Số TT")
ws1.write(1,1,"Môn học")    
ws1.write(1,2,"Điểm")

ws1.write(2,0,1)
ws1.write(2,1,"Toán")
ws1.write(2,2,7.4)

ws1.write(3,0,2)
ws1.write(3,1,"Văn")
ws1.write(3,2,7.8)

ws1.write(4,0,3)
ws1.write(4,1,"Tiếng Anh")
ws1.write(4,2,8.3)

ws1.write(5,0,4)
ws1.write(5,1,"Lý")
ws1.write(5,2,7.2)

ws1.write(6,0,5)
ws1.write(6,1,"Hóa")
ws1.write(6,2,6.3)

ws1.write(7,0,6)
ws1.write(7,1,"Sinh")
ws1.write(7,2,8.9)

ws1.write(8,0,7)
ws1.write(8,1,"Sử")
ws1.write(8,2,5.8)

ws1.write(9,0,8)
ws1.write(9,1,"Địa")
ws1.write(9,2,8.4)

i = 9
ws1.write(i,0,9)
ws1.write(i,1,"Điểm tb")
ws1.write(i,2,round((7.4+7.8+8.3+7.2+6.3+8.9+5.8+8.4)/8,2))
print(wb)
wb.close()

# Đọc file

file_read = pd.read_excel("file excel được tao.xlsx", sheet_name="Dữ liệu sheet")
print(file_read)   # xuất toàn bộ sheet
print(file_read.columns.ravel())   # Xuất tên các cột

# file_read=pd.read_excel("file excel được tao.xlsx",sheet_name='Dữ liệu sheet', usecols=['Môn học'])
# print(file_read)