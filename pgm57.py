str=input("Enter a word: ")
s1=str[0]
s2=str[1: ].replace(s1,"$")
new=s1+s2
print(new)