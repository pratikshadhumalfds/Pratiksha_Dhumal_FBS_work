###Create a class book with members as bid, bname, price and author. Add following methods - 
# a. constructor (support both parameterized and parameterless)
# b. destructor 
# c. ShowBook

class Book():
    def __init__(self, id=None, name=None, price=None, author=None):
        self.bid = id
        self.bname = name
        self.price = price
        self.author = author
    def showbook(self):
        print("Id:", self.bid)
        print("Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    def __del__(self):
        print(f"Book '{self.bname}' is Destroyed.")

b1 = Book(111, "Secrets of life", 500, "XYZ")    # Using parameterized constructor 
b1.showbook()
del b1

print("\n---------------------------\n")

b2 = Book(112, "ABC", 400, "ASDFGHFGH")      # Using parameterized constructor 
b2.showbook()

print("\n---------------------------\n")

b3 = Book()   # Using parameterless constructor
b3.showbook()