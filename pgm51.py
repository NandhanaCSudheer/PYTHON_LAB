l1=map(int,input("Enter a list of numbers: ").split(','))
list1=[]
tot1=0
for i in l1:
    list1.append(i)
    tot1+=i
l2=map(int,input("Enter another list of numbers: ").split(','))
list2=[]
tot2=0
for i in l2:
    list2.append(i)
    tot2+=i
len1=len(list1)
len2=len(list2)
if len1==len2:
    print("Both lists are of same length")
else:
    print("Both lists have different lengths")
if tot1==tot2:
    print("Both lists have same sum")
else:
    print("Both lists have different sums")
    same=False
for i in list1:
    if i in list2:
        same=True
        break
if same:
    print("Both lists have same value occuring")
else:
    print("Both lists have entirely different values")