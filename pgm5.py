n=float(input("Enter the number: "))
mul=int(input("Enter the no. of multiples: "))

for i in range(1,mul+1):
    pro=n*i
    print(f"The {i}th multiple of {n} is = {pro}")