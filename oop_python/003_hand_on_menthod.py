# the normal menthod in python

class book:
    # adding the class variables
    paperBased = True
    language = "US"

    # adding a normal method: amethond is a fuction attached to thee instances
    # it have a special format by introducing the new variable self
    # return some stuff, same as a normal fuction
    def authorsSTR(self):
        return ", ".join(self.authors)   
    
    #initiate a object attribute

    def addFavorite(self):
        self.isfavorite = True
    
    # transform an attribute
    def improveRate(self):
        self.rating = min(10,self.rating+1)

    def downgradeRate(self):
        self.rating = max(0,self.rating - 1)

book_1 = book()
book_2 = book()

book_1.title = "quen sach 1"
book_1.authors = ["thuy","nam"]
book_1.rating = 5

book_2.title = "quyen sach 2"
book_2.authors = ["vinh rau"]
book_2.rating = 5


book_1.improveRate()
print(book_1.authorsSTR())
print(book_1.rating)

book_2.downgradeRate()
print(book_2.rating)
