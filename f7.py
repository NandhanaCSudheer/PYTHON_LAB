vowels = "aeiouAEIOU"
v = c = 0

with open("f2.txt", "r") as f:
    text = f.read()

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)
