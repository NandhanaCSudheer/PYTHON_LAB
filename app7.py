class Rectangle:
    def __init__(self, length=0, width=0):
        if width == 0:
            self.length = length
            self.width = length  
        else:
            self.length = length
            self.width = width

    def area(self):
        return self.length * self.width

a,b=map(float,input("Enter length and breadth of rectangle:").split(","))
if a==b:
    r1 = Rectangle(a)
    print("Square area:", r1.area())
else:
    r2 = Rectangle(a,b)
    print("Rectangle area:", r2.area())
