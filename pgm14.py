dictnry={"apple":3,"banana":1,"cherry":2}
print(dictnry)
items=list(dictnry.items())
n=len(items)
for i in range(n):
    for j in range(i+1,n):
        if items[i][1]>items[j][1]:
            items[i],items[j]=items[j],items[i]

print("Sorted in ascending order is: ",dict(items))
print("Sorted in descending order is: ",dict(reversed(items)))
