with open("f1.txt","r") as f1:
    with open("f2.txt","w")as f2:
        for lineno,line in enumerate(f1,start=1):
            if lineno % 2!=0:
                f2.write(line)
        print("Copied successfully!!!")


        f1.seek(0)                                            # First one is more accurate or better
        data=f1.readlines()
        for i in range(len(data)):
            if i%2!=0:
                f2.write(data[i])