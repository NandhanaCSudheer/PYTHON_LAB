str=input("Enter a no.of lines: ")
count=0
i=0
j=0
for line in str:
    count+=1
    words=line.split()
    i+=len(words)
    j+=len(line)