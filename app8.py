class Complex:
    def __init__(self):
        pass
    def add(self,a,b,c,d):
        return (a+b,c+d)
    def multiply(self,a,b,c,d):
        return ((a*c-b*d),(a*d+b*c))

p=Complex()
a,b=map(float,input("Enter the two number's real part:").split(","))
c,d=map(float,input("Enter the two number's imaginary part:").split(","))
ch=0
while ch!=3:    
    print("MENU\n1.ADDITION\n2.MULTIPLICATION\n3.EXIT\n:")
    ch=int(input("Select your choice:"))
    if ch==1:
        sumr,sumi=p.add(a,b,c,d)
        print("Sum of complex numbers are ",sumr,"+",sumi,"i")
    else:
        mulr,muli=p.multiply(a,b,c,d)
        print("Product of complex numbers are ",mulr,"+",muli,"i")