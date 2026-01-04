s=input("Enter a string: ")
count={}
for c in s:
    count[c]=0
for c in s:
    count[c]+=1

print(count)

freq={}
for char in s:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1

print(freq)