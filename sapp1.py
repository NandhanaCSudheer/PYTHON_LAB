class Bank:
    def __init__(self,acc_no,acc_name,bal=0):
        self.acc_no=acc_no
        self.acc_name=acc_name
        self.bal=bal
        
    def deposit(self,amount):
            self.bal+=amount
            print("amount credited successfully")
            
            
    def withdraw(self,amount):
            self.bal-=amount
            print("amount debited successfully")
            
    def balance(self):
            print("Your current balance: ",self.bal)
            
ano=input("Enter your account number: ")
aname=input("\nenter your name: ")              
balan=float(input("\nEnter you account balance: "))
acc= Bank(ano,aname,balan)
print("MENU\n1.Deposit\n2.Withdraw\n3.Balance: ")  
i=int(input("enter your choice")) 
if i==1:
        amount=float(input("Enter your amount:"))
        acc.deposit(amount)  
        acc.balance()
        
elif i==2:
        amount=float(input("Enter your amount to debit:"))
        acc.withdraw(amount)  
        acc.balance()
        
else:
        acc.balance()
      
        

        