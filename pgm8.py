n=int(input("Enter the number: "))
l=len(str(n))
print(l)
count=0
while(n!=0):
    n=n//10
    count+=1
print(count)
