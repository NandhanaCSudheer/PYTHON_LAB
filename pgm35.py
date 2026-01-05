n=int(input("Enter a number or an integer: "))
list=[]
for i in range(1,n+1):
    if n%i==0:
        list.append(i)
print("Factors of ",n,"are ",list)