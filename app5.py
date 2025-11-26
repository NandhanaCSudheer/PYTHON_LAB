class Mathops:
    def __init__(self):
        pass
    def calc(self,*args):
        sum=0
        for i in args:
            sum=sum+i
        return sum
x=int(input("enter the no. of elements to be added:"))
m=Mathops()
a=[]
for i in range (1,x+1):
    s=int(input("Enter the no. of elements one by one!!!"))
    a.append(s)
sum=m.calc(*a)
print(sum)

