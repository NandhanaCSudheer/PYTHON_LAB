n=int(input("Enter the limit of which multiples is to be found: "))
mul=1
for i in range (1,n+1):
    mul=mul*i
print("The first ",n," multiples = ",mul)