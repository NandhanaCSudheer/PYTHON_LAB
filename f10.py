import csv

highest_total = -1
top_student = ""

with open("f10.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)         

    for row in reader:
        name = row[0]
        marks = list(map(int, row[1:]))
        total = sum(marks)

        if total > highest_total:
            highest_total = total
            top_student = name

print("Top Student:", top_student)
print("Highest Total Marks:", highest_total)
