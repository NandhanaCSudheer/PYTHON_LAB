class StudentManager:
    def __init__(self):
        self.students = []  

    def add_student(self, rollno, name, mark):
        student = {
            "rollno": rollno,
            "name": name,
            "mark": mark
        }
        self.students.append(student)
        print("Student added successfully!\n")

    def search_student(self, rollno):
        for s in self.students:
            if s["rollno"] == rollno:
                print("\nStudent Found:")
                print("Roll No:", s["rollno"])
                print("Name   :", s["name"])
                print("Marks  :", s["mark"])
                return
        print("\nStudent not found.\n")

    def display(self):
        print("\n--- Student Details ---")
        if len(self.students) == 0:
            print("No records found.")
            return
        for s in self.students:
            print(s["rollno"], s["name"], s["mark"])
        print()


sm = StudentManager()

while True:
    print("MENU")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        rollno = int(input("Enter roll no: "))
        name = input("Enter name: ")
        mark = float(input("Enter marks: "))
        sm.add_student(rollno, name, mark)

    elif ch == 2:
        rollno = int(input("Enter roll no to search: "))
        sm.search_student(rollno)

    elif ch == 3:
        sm.display()

    elif ch == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice\n")
