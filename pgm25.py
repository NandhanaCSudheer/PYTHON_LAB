n=int(input("Enter the no. of entries in first dictionary: "))
dict={}
for i in range(1,n+1):
    name=input("Enter name: ")
    rollno=int(input("Enter rollno: "))
    dict[name]=rollno
m=int(input("Enter the no. of entries in second dictionary: "))
dicty={}
for i in range(1,m+1):
    name=input("Enter name: ")
    rollno=int(input("Enter rollno: "))
    dicty[name]=rollno
print(dict)
print(dicty)
merge={}
for key,value in dict.items():
    merge[key]=value
for key,value in dicty.items():
    merge[key]=value
print(merge)