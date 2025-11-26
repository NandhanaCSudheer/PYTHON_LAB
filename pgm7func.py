n=int(input("Enter the number whose factorial is to be find: "))
def func(n):
    fact=1
    if n<=0:
        print("Enter a positive number")
        return None
    elif n==1:
        print("Factorial of ",n," = 1")
        return 1
    else:
        for i in range(1,n+1):
            fact=fact*i
        return fact
fact=func(n)
print("Factorial of ",n," =",fact)

