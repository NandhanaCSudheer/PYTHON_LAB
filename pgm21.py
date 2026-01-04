s=input("Ente a string: ")
if s[-3: ]=='ing':
    s=s+"ly"
else:
    s=s+"ing"
print(s)