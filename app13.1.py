class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}   

    def add_subject(self, subject, mark):
        self.marks[subject] = mark
        print(f"{subject} added.")

    def update_marks(self, subject, mark):
        if subject in self.marks:
            self.marks[subject] = mark
            print(f"{subject} updated.")
        else:
            print("Subject not found!")

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


name = input("Enter student name: ")
s = Student(name)

while True:
    print("\nMENU")
    print("1. Add Subject")
    print("2. Update Marks")
    print("3. Average Marks")
    print("4. Grade")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        subject = input("Enter subject name: ")
        mark = float(input("Enter marks: "))
        s.add_subject(subject, mark)

    elif ch == 2:
        subject = input("Enter subject name to update: ")
        mark = float(input("Enter new marks: "))
        s.update_marks(subject, mark)

    elif ch == 3:
        print("Average Marks:", s.average())

    elif ch == 4:
        print("Grade:", s.grade())

    elif ch == 5:
        break

    else:
        print("Invalid choice!")
