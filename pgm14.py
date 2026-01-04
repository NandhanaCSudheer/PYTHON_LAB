dict={"apple":3,"banana":1,"cherry":2}
print(dict)
items=list(dict.items())
n=len(items)
for i in range(n):
    for j in range(i+1,n):
        if items[i][1]>items[j][1]:
            items[i],items[j]=items[j],items[i]

print("Sorted in ascending order is: ",items)
print("Sorted in descending order is: ",reversed(items))
