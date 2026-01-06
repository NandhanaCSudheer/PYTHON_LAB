line = input("Enter a line of text: ")

words = line.split()
print(words)
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print("Word occurrences:")
for word in count:
    print(word, ":", count[word])
