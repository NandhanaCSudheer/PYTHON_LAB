n=int(input("Enter the no. of entries: "))
dicty={}
for i in range(1,n+1):
    name=input("Enter name: ")
    rollno=int(input("Enter rollno: "))
    dicty[name]=rollno
print (dicty)
items=list(dicty.items())
l=len(items)
for i in range (0,l):
    for j in range(i+1,l):
        if items[i][1]>items[j][1]:
            items[i],items[j]=items[j],items[i]
print(items)
print(dict(reversed(items)))