with open("f2.txt", "r") as f:
    text = f.read()


char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1


word_freq = {}
for word in text.split():
    word_freq[word] = word_freq.get(word, 0) + 1

print("Character Frequency:")
for ch, count in char_freq.items():
    print(ch, ":", count)

print("\nWord Frequency:")
for w, count in word_freq.items():
    print(w, ":", count)
