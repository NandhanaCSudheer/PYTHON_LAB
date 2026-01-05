class Bank:
    def __init__(self,accno,accname,type,bal=0):
        self.accno=accno
        self.accname=accname
        self.type=type
        self.bal=bal

    def deposit(self,amount):
        self.bal+=amount
        print("Amount credited successfully!!!")
    
    def withdraw(self,amount,minbal):
        self.bal-=amount
        if self.bal<=minbal:
            print("Insufficient minimum balance!!!!")
            self.bal+=amount
        elif amount>self.bal:
            print("Insufficient minimum balance!!!!")
        else:
            print("Amount debited successfully!!!")
    
    def display(self):
        print("Account holder's name: ",self.accname)
        print("Account Number: ",self.accno)
        print("Type of Account: ",self.type)
        print("Balance: ",self.bal)

ano=int(input("Enter your account number: "))
aname=input("Enter your account holder's name: ")
atype=input("Enter your account type: ")
balan=int(input("Enter your current balance: "))
b=Bank(ano,aname,atype,balan)
while(True):
    print("MENU\n1.DEPOSIT\n2.WITHDRAW\n3.DISPLAY BALANCE\n4.EXIT\n")
    ch=int(input("Enter your choice: "))
    if ch==1:
        amt=int(input("Enter the amount to be deposited: "))
        b.deposit(amt)
        b.display()
    elif ch==2:
        amt=int(input("Enter the amount to be withdrawed: "))
        min=int(input("Enter your minimum balance: "))
        b.withdraw(amt,min)
        b.display()
    elif ch==3:
        b.display()
    elif ch==4:
        break
    else:
        print("Enter a valid number!!!")
    
        
