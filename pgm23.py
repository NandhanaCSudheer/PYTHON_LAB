n=int(input("Enter the no. of entries: "))
dict={}
for i in range(1,n+1):
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    dict[name]=age
print (dict)
for key,value in dict.items():
    print(key,value)
