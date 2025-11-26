from math import pi
from abc import ABC, abstractmethod
class Shape(ABC):
    def area(self):
        pass
        
class Rectangle(Shape):
    def area(self,l,w):
        return l*w

class Square(Shape):
    def area(self,a):
        return a*a 

class Triangle(Shape):
    def area(self,b,h):
        return 0.5*b*h 
    
class Circle(Shape):
    def area(self,r):
        return pi*r*r

r=Rectangle()
s=Square()
t=Triangle()  
c=Circle()
ch=0
while ch!=5:
    print("MENU\n1.RECTANGLE\n2.SQUARE\n3.TRIANGLE\n4.CIRCLE\n5.EXIT:")
    ch=int(input("Choose the one for which you have to find the area!!!"))
    if ch==1:
        l,w=map(float,input("Enter the length and breadth of the rectangle:").split(","))
        a=r.area(l,w)
        print("Area of rectangle = ",a)
    elif ch==2:
        x=float(input("Enter the size of thesquare:"))
        a=s.area(x)
        print("Area of square = ",a)
    elif ch==3:
        b,h=map(float,input("Enter the base and height of the triangle:").split(","))
        a=t.area(b,h)
        print("Area of triangle = ",a)
    elif ch==4:
        d=float(input("Enter the radius of the circle:"))
        a=c.area(d)
        print("Area of circle = ",a)
    else:
        print("Invalid choice!!!")