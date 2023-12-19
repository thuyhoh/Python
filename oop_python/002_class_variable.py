class book:
    # adding the class variables
    paperBased = True
    language = "US"
    pass


book_1 = book()
book_2 = book()

print(book_1)
print(book_2)

print(book_1.language, end = " ")
print(book_1.paperBased)

print(book_2.language, end = " ")
print(book_2.paperBased)

# change information of variable class
book_1.paperBased = False

book_2.language = "JP"

print(book_1.language, end = " ")
print(book_1.paperBased)

print(book_2.language, end = " ")
print(book_2.paperBased)
