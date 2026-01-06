syr=int(input("Enter current year: "))
lyr=int(input("Enter final year: "))
list=[]
for i in range(syr,lyr+1):
    if (i%4==0 and i%100!=0) or (i%400==0):
        list.append(i)
print(list)
for i in list:
    print(i)
