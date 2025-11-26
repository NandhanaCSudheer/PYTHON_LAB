
text = input("Enter text to append: ")

with open("f2.txt", "a") as f:
    f.write(text + "\n")

print("Text appended successfully.")
