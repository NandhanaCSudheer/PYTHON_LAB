class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imag + other.imag)

    
    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"



a, b = map(float, input("Enter first complex number (real,imag): ").split(","))
c, d = map(float, input("Enter second complex number (real,imag): ").split(","))

c1 = ComplexNumber(a, b)
c2 = ComplexNumber(c, d)


while True:
    print("\nMENU\n1. ADDITION\n2. MULTIPLICATION\n3. EXIT")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        result = c1 + c2
        print("Sum =", result)

    elif ch == 2:
        result = c1 * c2
        print("Product =", result)

    elif ch == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
