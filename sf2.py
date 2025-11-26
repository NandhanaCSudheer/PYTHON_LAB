import csv
f=open("f10.csv","r")
with open("f10w.csv","w") as f2:
    reader=csv.DictReader(f)   #reader/DictReader
    writer=csv.writer(f2)
    for i in reader:
        writer.writerow(i)
        print(i)
    f.close()