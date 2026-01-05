start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

result = []

for i in range(start, end + 1):
    if 1000 <= i <= 9999:
        root = int(i ** 0.5)
        if root * root == i:          # perfect square
            even = True
            for d in str(i):
                if int(d) % 2 != 0:   # check all digits even
                    even = False
                    break
            if even:
                result.append(i)

print(result)
