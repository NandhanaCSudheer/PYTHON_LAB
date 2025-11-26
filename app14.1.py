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

while True:
    print("\nMENU")
    print("1. Add Product")
    print("2. Save to File")
    print("3. Read & Display File")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))
        pm.add_product(name, price, qty)

    elif ch == 2:
        pm.save_to_file("products.txt")

    elif ch == 3:
        pm.read_and_display("products.txt")

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
