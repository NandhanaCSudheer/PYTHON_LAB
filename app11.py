class Cat:
    def sound(self):
        print("Meow!!!")

class Dog:
    def sound(self):
        print("Boww!!!")

class Cow:
    def sound(self):
        print("Mbaa!!!")


ch=0
while ch!=4:
    print("MENU\n1.CAT\n2.DOG\n3.COW\n4.EXIT:")
    ch=int(input("Enter your choice:"))
    if ch==1:
        c=Cat()
        c.sound()
    elif ch==2:
        c=Dog()
        c.sound()
    else:
        c=Cow()
        c.sound()