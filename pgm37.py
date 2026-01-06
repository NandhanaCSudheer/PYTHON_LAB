class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
a=int(input("Enter the length of the first rectangle :"))
b=int(input("Enter the breadth of the first rectangle :"))
c=int(input("Enter the length of the second rectangle :"))
d=int(input("Enter the breadth of the second rectangle :"))
r1=Rectangle(a,b)
r2=Rectangle(c,d)
A1=r1.area()
A2=r2.area()
P1=r1.perimeter()
P2=r2.perimeter()
print("Area of first rectangle: ",A1)
print("Perimeter of first rectangle: ",P1)
print("Area of second rectangle: ",A2)
print("Perimeter of second rectangle: ",P2)
if r1.area()>r2.area():
    print("Area of first rectangle is larger!!!")
elif r1.area()<r2.area():
    print("Area of seconf rectangle is larger!!!")
else:
    print("Both are equal!!!")
