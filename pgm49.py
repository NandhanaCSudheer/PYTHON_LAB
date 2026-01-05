num=int(input("enter a number: "))
l=len(str(num))
n=num
sum=0
while n>0:
    digit=n%10
    sum+=digit**l
    n//=10
print(sum)
if num==sum:
    print("The given number is an armstrong number!!!")
else:
     print("The given number is not an armstrong number!!!")