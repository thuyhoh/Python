# Introductionn opp: classes, instances, attributes

# 1 - decate the class 
# khởi tạo class
class book:
    pass

# 2 - Initate or declarehe instances of the created class
# khởi tạo và khai báo đối tượng
book_1 = book()
book_2 = book()

# print memmory of object
print(book_1)
print(book_2)


# 3 - add attributes to the class
# tạo và thêm mới các thuộc tính bất kỳ vào trong class
book_1.title = "quyen sach 1"
book_1.authors = ["thuy","a buch of other people"]
book_1.form = "commics"

print(book_1.form)