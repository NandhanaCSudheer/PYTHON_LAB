x=float(input("Enter the side length of square: "))
square=lambda x:x*x
print("Area of square= ",square(x))
y,z=map(int,input("Enter the length and breadth of rectangle: ").split(','))
rectangle=lambda y,z:y*z
print("Area of square= ",rectangle(y,z))
a,b=map(int,input("Enter the base and height of triangle: ").split(','))
triangle=lambda a,b:0.5*a*b
print("Area of square= ",triangle(a,b))


