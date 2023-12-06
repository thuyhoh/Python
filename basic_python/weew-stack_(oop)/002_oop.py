# add the variable in the class

class book:
    language = ""
    ispaper = True

# change the data in the object
book_1 = book()
book_2 = book()

book_1.language = "english"
book_2.language = "japanses"

book_1.ispaper = False



# add attributed to the object

book_1.title = "intro to the weew"
book_1.authors = ["weew", "a buch of the other people"]

book_2.title = "7 habits"
book_2.authors = ["Stephen Covey"]

# print the data in the object book_1 and book_2
print( book_1.title , book_1.authors , book_1.language  , book_1.ispaper, sep =  "  ")
print( book_2.title , book_2.authors , book_2.language  , book_2.ispaper, sep =  "  ")

