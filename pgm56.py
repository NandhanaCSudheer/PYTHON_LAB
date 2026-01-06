str=input("Enter a list of name: ").split(',')
count=0
l=[]
for word in str:
    l.append(word)
print(l)
for ch in l:
    for i in ch:
        if "a" in i:
            count+=1
print(count)