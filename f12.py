import json

with open("f12.json", "r") as f:
    data = json.load(f)

sorted_emps = sorted(data, key=lambda x: x["salary"])

print("Employees sorted by salary:")
for emp in sorted_emps:
    print(emp["name"])
