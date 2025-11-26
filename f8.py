with open("f2.txt", "r") as f:
    content = f.read()

rev = content[::-1]

with open("f2rev.txt", "w") as f:
    f.write(rev)

print("File reversed successfully.")
