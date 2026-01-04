x,y,z=map(int,input("Enter 3 numbers to find the largest: ").split(','))
print("x = ",x," , y = ",y," , z = ",z)
if x>y:
    if x>z:
        print(x," is the largest")
    else:
        print(z," is the largest")
else:
    if y>z:
        print(y," is the largest")
    else:
        print(z," is the largest")

if x>=y and x>=z:
    print(x," is the largest")
elif y>=x and y>=z:
    print(y," is the largest")
else:
    print(z," is the largest")