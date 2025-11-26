with open("f2.txt", "r") as f:
    count = 0       
    i = 0            
    j = 0            

    for line in f.readlines():
        count = count + 1
        print(line)

        words = line.split()      
        i = i + len(words)        

        j = j + len(line)         

print("No. of lines = ", count)
print("No. of words = ", i)
print("No. of characters = ", j)
