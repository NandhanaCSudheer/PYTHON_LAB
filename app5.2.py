class MathOps:
    def __init__(self):
        pass
    def calc(self, a=None, b=None, c=None, numbers=None):
        if a is not None and b is not None and c is None and numbers is None:
            return a + b
        elif a is not None and b is not None and c is not None and numbers is None:
            return a + b + c
        elif numbers is not None:
            return sum(numbers)
        else:
            return "Invalid input"

m = MathOps()

print("\nSelect option:")
print("1. Sum of two integers")
print("2. Sum of three integers")
print("3. Sum of list of integers")

choice = int(input("\nEnter your choice (1/2/3): "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", m.calc(a, b))



elif choice == 2:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = int(input("Enter number 3: "))
    print("Sum =", m.calc(a, b, c))



elif choice == 3:
    n = int(input("How many numbers? "))
    lst = []
    for i in range(1, n + 1):
        value = int(input(f"Enter number {i}: "))
        lst.append(value)
    print("Sum =", m.calc(numbers=lst))

else:
    print("Invalid choice")
