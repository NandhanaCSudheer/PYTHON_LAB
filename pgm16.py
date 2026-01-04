x,y=map(int,input("Enter the numbers whode GCD is to be found: ").split(','))
l1=[]
l2=[]
gcd=0
for i in range(1,x+1):
    if(x%i==0):
        l1.append(i)
for i in range(1,y+1):
    if(y%i==0):
        l2.append(i)
for i in l1:
    for j in l2:
        if i==j:
            gcd=i

print(f"GCD of ({x},{y}) = {gcd}")

while y!=0:
    x,y=y,x%y
print("GCD = ",x)
            
    
