n=int(input("Enter the no.of terms needed in thr Fibonacci series: "))
fterm=0
sterm=1
for i in range(0,n+1):
    nterm=fterm+sterm
    print(fterm)
    fterm=sterm
    sterm=nterm
