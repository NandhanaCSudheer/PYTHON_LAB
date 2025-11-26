class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age :", self.age)


class Employee(Person):
    def __init__(self, name, age, salary, emp_id):
        super().__init__(name, age)   
        self.salary = salary
        self.emp_id = emp_id

    def display(self):  
        super().display()
        print("Salary:", self.salary)
        print("Employee ID:", self.emp_id)


class Manager(Employee):
    def __init__(self, name, age, salary, emp_id, bonus, dept):
        super().__init__(name, age, salary, emp_id) 
        self.bonus = bonus
        self.dept = dept

    def display(self): 
        super().display()
        print("Bonus:", self.bonus)
        print("Department:", self.dept)



m = Manager("Ravi", 40, 50000, "E101", 10000, "Sales")
m.display()
n=input("Name of employee:")
ag=int(input("Age of the Empoyee:"))
sal=float(input("Salary of the employee:"))
id=int(input("ID of the employee:"))
bonus=float(input("Bonus for the employee:"))
dept=input('Department of the employee:')
m1=Manager(n,ag,sal,id,bonus,dept)
m1.display()