s = input("Enter a string: ")
n = len(s)
flag = 0

for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        flag = 1
        break

if flag == 1:
    print("The string is not a palindrome!!!")
else:
    print("String is a palindrome!!!")
str=s[::-1]

for i in range(n):
    if s[i]!=str[i]:
        print("The string is not a palindrome!!!")
        break
    print("String is a palindrome!!!")

if s==s[::-1]:
    print("String is a palindrome!!!")
else:
     print("The string is not a palindrome!!!")
