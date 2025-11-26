import csv

count = 0

with open("f10.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        total = sum(map(int, row[1:]))

        if total > 80:
            count += 1

print("Rows where total marks > 80:", count)
