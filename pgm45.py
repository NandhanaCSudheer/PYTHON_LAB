import csv
with open("f3.csv","r") as f:
    reader=csv.reader(f)       #can use DictReader also instead of reader
    for row in reader:
        print(row)