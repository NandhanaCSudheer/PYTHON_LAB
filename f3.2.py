with open ("f2.txt","r") as f:
    count=dict()
    text=f.read()
    for i in text:
        count[i]=0
    for i in text:
        count[i]=count[i]+1
    for i in text:
        print(i,"=",count[i])
