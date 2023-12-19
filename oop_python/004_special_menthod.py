# a đunẻ or magic method shaoe: __specialMethodName__


class book:
    # adding the class variables
    paperBased = True
    language = "US"

# menthod __init__()
    def __init__(self,title,authros,rating):
        self.title = title
        self.authors = authros
        self.rating = rating
# __str__()
    def __str__(self) :
        return self.title +" cua "+ self.authors

book_1 = book("cuoi sach 1","toi",5)
print(book_1.language)

# __dir__ special menthod: list all of attributes of obj
print(book_1.__dir__())

# __str__ : return the string 
print(book_1)

# __dict__ :  trả về dưới dạng attributes : value
print(book_1.__dict__)