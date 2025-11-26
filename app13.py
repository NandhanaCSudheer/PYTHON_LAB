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



s = Student("Arun")
s.add_subject("Math", 95)
s.add_subject("English", 88)
s.update_marks("English", 90)
print("Average:", s.average())
print("Grade:", s.grade())
