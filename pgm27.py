n=int(input("Enter the no. of terms required: "))
fterm=0
lterm=1
for i in range(1,n+1):
    sterm=fterm+lterm
    print(fterm)
    fterm=lterm
    lterm=sterm
   