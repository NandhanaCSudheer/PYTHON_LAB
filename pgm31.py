str=input("Enter a string: ")
wcount=dict()
for ch in str:
    wcount[ch]=0
for ch in str:
    wcount[ch]+=1
print(wcount)