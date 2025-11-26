x,y=map(int,input("Enter the two numbers to perform arithmetic operations:").split(','))
print("MENU:\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.MODULUS\n")
n=int(input("Enter your choice: "))
def func(x,y,n):
    if n==1:
        print("The sum = ",x+y)
        return x+y
    elif n==2:
        print("The difference = ",x-y)
        return x-y
    elif n==3:
        print("The product = ",x*y)
        return x*y
    elif n==4:
        print("The quotient = ",x/y)
        return x/y
    elif n==5:
        print("The remainder = ",x%y)
        return x%y
result=func(x,y,n)
print("The result = ",result)