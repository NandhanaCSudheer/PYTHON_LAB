c1=input("Enter a list of colours: ").split(',')
c2=input("Enter another list of colours: ").split(',')
l=[]
for i in c1:
    if i not in c2:
        l.append(i)
for i in l:
    print(i)