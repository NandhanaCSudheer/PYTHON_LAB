class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def updatesalary(self, amount):
        self.salary += amount
        print("Salary updated successfully!")
        print("New Salary:", self.salary)
    
    def displaydetails(self):
        print("\n--- Employee Details ---")
        print("ID: ", self.id)
        print("Name: ", self.name)
        print("Salary: ", self.salary)

    def calculatesalary(self, monthsal):
        annual = 12 * monthsal
        print("Annual Salary:", annual)


print("Enter details for Employee 1:")
id1 = int(input("Enter ID: "))
name1 = input("Enter Name: ")
salary1 = int(input("Enter Salary: "))
emp1 = Employee(id1, name1, salary1)

print("\nEnter details for Employee 2:")
id2 = int(input("Enter ID: "))
name2 = input("Enter Name: ")
salary2 = int(input("Enter Salary: "))
emp2 = Employee(id2, name2, salary2)


while True:         # while ch != 4
    print("\nMAIN MENU")
    print("1. Update Salary")
    print("2. Display Details")
    print("3. Calculate Annual Salary")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 4:
        print("Exiting program...")
        break

  
    emp_choice = int(input("Select Employee (1 or 2): "))
    if emp_choice == 1:
        emp = emp1
    elif emp_choice == 2:
        emp = emp2
    else:
        print("Invalid Employee selection!")
        continue

    if ch == 1:
        amount = int(input("Enter amount to update salary: "))
        emp.updatesalary(amount)

    elif ch == 2:
        emp.displaydetails()

    elif ch == 3:
        monthsal = int(input("Enter monthly salary: "))
        emp.calculatesalary(monthsal)

    else:
        print("Invalid choice!")
