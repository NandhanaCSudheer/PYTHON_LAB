old = input("Enter word to replace: ")
new = input("Enter new word: ")

with open("f2.txt", "r") as f:
    data = f.read()

data = data.replace(old, new)

with open("f2.txt", "w") as f:
    f.write(data)

print("Replacement done.")
