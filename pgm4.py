x,y=map(int,input("Enter the two numbers to perform arithmetic operations:").split(','))
while True:
    print("MENU:\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.MODULUS\n6.FLOOR DIVISION\n7.EXIT\n")
    n=int(input("Enter your choice: "))
    if n==1:
        print("The sum = ",x+y)
    elif n==2:
        print("The difference = ",x-y)
    elif n==3:
        print("The product = ",x*y)
    elif n==4:
        print("The quotient = ",x/y)
    elif n==5:
        print("The remainder = ",x%y)
    elif n==6:
        print("The result = ",x//y)
    elif n == 7:
        print("Exiting program")
        break
    else:
        print("Invalid choice")