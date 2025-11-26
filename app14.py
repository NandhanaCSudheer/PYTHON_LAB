class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, qty):
        p = Product(name, price, qty)
        self.products.append(p)
        print("Product added.")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for p in self.products:
                f.write(f"{p.name},{p.price},{p.qty}\n")
        print("Saved to file.")

    def read_and_display(self, filename):
        print("\nProducts from file:")
        with open(filename, "r") as f:
            for line in f:
                name, price, qty = line.strip().split(",")
                print("Name:", name, "| Price:", price, "| Qty:", qty)



pm = ProductManager()
pm.add_product("Pen", 10, 50)
pm.add_product("Book", 100, 20)

pm.save_to_file("products.txt")
pm.read_and_display("products.txt")
