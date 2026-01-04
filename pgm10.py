from cmath import sqrt
a=complex(input("Enter the coefficient of x^2: "))
b=complex(input("Enter the coefficient of x: "))
c=complex(input("Enter the value of constant: "))
d=(sqrt(b**2-(4*a*c)))
r1=(-b+d)/(2*a)
r2=(-b-d)/(2*a)
print(f"The roots of the quadratic equation {a}x^2+{b}x+{c} are {r1} and {r2}")