class Product:
    def __init__(self, name = "codetree", code = "50"):
        self.name = str(name)
        self.code = int(code)

    def printProduct(self):
        print("product " + str(self.code) + " is " + self.name)

p1 = Product()
p2 = Product(*input().split())

p1.printProduct()
p2.printProduct()