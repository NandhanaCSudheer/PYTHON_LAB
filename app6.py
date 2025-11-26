class Student:
    def __init__(self):
        pass
    def calculate_mark(self,m,t,p):
        if m>=p:
            print("You passed the exam with if you get marks greater than pass mark")
        else:
            print(" Else you failed!!!")
    
class PostGraduateStudent(Student):
    def __init__(self):
        super().__init__()
    def calculate_mark(self,m,t,p):
        if ((m*100)/t) >= p:
            print("You passed the exam with" ,((m*100)/t),"%")
        else:
            print("You failed!!!")

s=PostGraduateStudent()
m=float(input("Enter your mark: "))
t=float(input("Enter your total mark: "))
p=float(input("Enter your passing percentage: "))
s.calculate_mark(m,t,p)