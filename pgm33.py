list=input("Enter a list of words: ").split(',')
s=len(list[0])
for word in list:
    if s<len(word):
        s=len(word)
print(s)