import csv

count = 0

with open("f10.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)      

    for row in reader:
        mark = int(row[1]) 
        if mark > 80:
            count += 1

print("Rows with marks > 80:", count)
