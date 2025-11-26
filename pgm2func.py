a,b=map(int,input("Enter 2 numbers to swap:").split(','))
def func(x,y):
    print("x = ",x)
    print("y = ",y)
    x,y=y,x
    return x,y
x,y=func(a,b)
print("x = ",x)
print("y = ",y)