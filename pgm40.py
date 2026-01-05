class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth

    def area(self):
        return self.__length*self.__breadth
    
    def __lt__(self, other):
        return self.area() < other.area()

    
a=int(input("Enter the length of the first rectangle :"))
b=int(input("Enter the breadth of the first rectangle :"))
c=int(input("Enter the length of the second rectangle :"))
d=int(input("Enter the breadth of the second rectangle :"))
r1=Rectangle(a,b)
r2=Rectangle(c,d)
A1=r1.area()
A2=r2.area()
print("Area of first rectangle: ",A1)
print("Area of second rectangle: ",A2)
if r1 < r2:
    print("Second rectangle has larger area!!!")
else:
    print("First rectangle has larger area!!!")