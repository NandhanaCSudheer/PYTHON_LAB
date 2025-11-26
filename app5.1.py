class MathOps:
    def __init__(self):
        pass
    def calc(self, a=None, b=None, c=None, numbers=None):
        if a is not None and b is not None and c is None and numbers is None:
            return a + b
        elif a is not None and b is not None and c is not None and numbers is None:
            return a + b + c
        elif numbers is not None:
            return sum(numbers)
        else:
            return "Invalid input"
m = MathOps()
print(m.calc(5, 10))               
print(m.calc(5, 10, 15))           
print(m.calc(numbers=[1,2,3,4,5]))  
