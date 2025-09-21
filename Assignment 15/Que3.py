###Create a class Shirt with members as sid, sname,type(formal etc.), price and size(small, large etc).
#  Add following methods - 
# a. Constructor (support both parameterized and parameterless)
# b. Destructor 
# c. ShowShirt

class Shirt:
    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def showshirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)

    def __del__(self):
        print(f"Shirt '{self.sname}' is destroyed.")

s1 = Shirt(201, "Classic Fit", "Formal", 1200, "Large")
s1.showshirt()
del s1

print("\n################################################\n")

s2 = Shirt()
s2.showshirt()
del s2
