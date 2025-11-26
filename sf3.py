import csv
with open('f3.csv','r')as file:
    field=['Name','Age','Dept']
    reader=csv.DictReader(file,fieldnames=field)
    for i in reader:
        print(i['Dept'])