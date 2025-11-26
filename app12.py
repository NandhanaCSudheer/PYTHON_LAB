class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Address(Person):
    def __init__(self, name, age,addr):
        super().__init__(name, age)
        self.addr=addr
    def display(self,name,age,addr):
        print("Name of person is: ",self.name)
        print("Age of person is: ",self.age)
        print("Address of person is: ",self.addr)


n=input("Enter your name:")
age=int(input("Enter your age:"))
ad=input("Enter your address:")
a=Address(n,age,ad)
a.display(n,age,ad)