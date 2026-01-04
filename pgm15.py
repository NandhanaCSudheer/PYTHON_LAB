d1={"a":1,"b":2}
d2={"c":3,"d":4}
merge={}
for d in (d1,d2):
    for key,value in d.items():
        merge[key]=value
print(merge)

for key in d1:
    merge[key]=d1[key]
for key in d2:
    merge[key]=d2[key]
print(merge)