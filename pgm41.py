class Time:
    def __init__(self,h=0,m=0,s=0):
        self.__hr=h
        self.__min=m
        self.__sec=s

    def display(self):
        print(self.__hr,":",self.__min,":",self.__sec)
    
    def __add__(self,other):
        h=self.__hr+other.__hr
        m=self.__min+other.__min
        s=self.__sec+other.__sec
        if s>=60:
            s-=60
            m+=1
        if m>=60:
            m-=60
            h+=1
        if h>=24:
            h-=24
        return Time(h,m,s)
    
t1=Time(2,45,30)
t2=Time(1,20,45)
print("First time:")
t1.display()
print("Second time:")
t2.display()
t3=t1+t2
print("Added Time:")
t3.display()
