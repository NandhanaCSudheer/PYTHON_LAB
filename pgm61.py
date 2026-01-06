n = int(input("Enter number of lines: "))

line_count = 0
word_count = 0
char_count = 0

for _ in range(n):
    line = input()
    line_count += 1
    words = line.split()
    word_count += len(words)
    char_count += len(line)

print("No. of lines =", line_count)
print("No. of words =", word_count)
print("No. of characters =", char_count)
