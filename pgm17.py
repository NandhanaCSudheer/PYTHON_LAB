l=map(int,input("Enter a list of numbers: ").split(','))
list=[]
for i in l:
    list.append(i)
print("Old list : ",list)
newlist=[]
for i in list:
    if i%2!=0:
        newlist.append(i)

print(newlist)