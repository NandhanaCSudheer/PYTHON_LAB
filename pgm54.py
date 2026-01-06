str=input("Enter a word: ")
vowels="aeiouAEIOU"
list=[]
for i in str:
    if i in vowels:
        print(i)
        list.append(i)
print(list)