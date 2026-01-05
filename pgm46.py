import csv
with open("f3.csv","r") as f:
    field=["Rollno","Name","Age","Course"]
    reader=csv.DictReader(f,fieldnames=field)
    for row in reader:
        for col in field:
            print(row[col])
    f.seek(0)
    for row in reader:
        print(row['Name'])