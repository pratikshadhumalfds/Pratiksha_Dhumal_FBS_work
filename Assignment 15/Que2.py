###Create a class Product with members as pid, pname, price and quality.
#  Add following methods - 
# a. Constructor (support both parameterized and parameterless)
# b. Destructor 
# c. ShowProduct

class Product:
    def __init__(self, pid=None, pname=None, price=None, quality=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quality = quality

    def showproduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quality:", self.quality)

    def __del__(self):
        print(f"Product is destroyed.")

p1 = Product(101, "Laptop", 50000, "High")
p1.showproduct()
del p1                 #destructor called

print("\n---\n")

p2 = Product()
p2.showproduct()
del p2  
