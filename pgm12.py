colors=input("Enter a number of colors seperating by commas: ").split(',')
list=[]
for i in colors:
    list.append(i)
print(f"First colour: {list[0]}\nSecond colour: {list[-1]}")
print(list)