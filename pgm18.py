n=float(input("Enter the number: "))       
def factorial(n):
    if n<0:
        print("Enter a positive number")
        return None
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))