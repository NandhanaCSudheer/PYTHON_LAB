str=input("Enter a word or a string: ")
if str[-3: ]=="ing":
    str=str+"ly"
else:
    str=str+"ing"
print(str)