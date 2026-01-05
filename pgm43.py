with open("f1.txt","r") as f:
    list=[]
    for data in f.readlines():
        list.append(data)
    print(list)
    f.seek(0)
    file=f.readlines()
    print(file)