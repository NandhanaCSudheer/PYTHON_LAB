d1={"a":1,"b":2}
d2={"c":3,"d":4}
merge={}
for key,value in d1.items():
    merge[key]=value
for key,value in d2.items():
    merge[key]=value
print(merge)

for key in d1:
    merge[key]=d1[key]
for key in d2:
    merge[key]=d2[key]
print(merge)