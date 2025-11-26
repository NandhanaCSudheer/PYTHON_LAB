class Address:
    def __init__(self, addr):
        self.addr = addr

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address 

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address.addr)


n = input("Enter your name: ")
age = int(input("Enter your age: "))
ad = input("Enter your address: ")

addr_obj = Address(ad)
p = Person(n, age, addr_obj)
p.display()
