import csv
n=int(input("Enter the no. of entries needed in the dictionary: "))
dictnry={}
for i in range(1,n+1):
    key=input("Enter your name:")
    value=int(input("Enter your age:"))
    dictnry[key]=value
print(dictnry)
with open("f4.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Age"])
    for key,value in dictnry.items():
        writer.writerow([key,value])
f.close()
with open("f4.csv","r") as f1:
    reader=csv.reader(f1)
    for row in reader:
        print(row)