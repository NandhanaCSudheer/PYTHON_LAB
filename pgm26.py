n=float(input("Enter a number: "))
def factorial(n):
    if n<0:
        print("Enter a positive integer!!!")
        return None
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
fact=factorial(n)
print(fact)

m=int(input("Enter a number: "))
def factor(m):
    prod=1
    if m<0:
        print("Enter a positive integer!!!")
        return None
    elif m==0 or m==1:
        return 1
    else:
        for i in range(1,m+1):
            prod=prod*i
        return prod
fac=factor(m)
print(fac)