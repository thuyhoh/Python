# @staticmenthod & doesn't need the self argurment
# @ is a function decorator


class book:
    # adding the class variables
    paperBased = True
    language = "US"

    @staticmethod
    def is_expesive(prive):
        if prive > 10:
            return True
        else:
            return False
        

book_1 = book()
book_2 = book()

print(book_1.is_expesive(19))
print(book_2.is_expesive(9))
