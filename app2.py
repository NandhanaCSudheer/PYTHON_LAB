class Bank:
    def __init__(self,acc_no,acc_name,bal=0):
        self.acc_no=acc_no
        self.acc_name=acc_name
        self.bal=bal
        
    def deposit(self,amount):
            self.bal+=amount
            print("amount credited successfully")
            
            
    def withdraw(self,amount,minbal):
            self.bal-=amount
            if self.bal<minbal:
                   self.bal+=amount
                   print("Your account requires minumum balance...Withdrawal is not possible!!!")
            else:
                   print("amount debited successfully")
            
    def balance(self):
            print("Your current balance: ",self.bal)
            
ano=input("Enter your account number: ")
aname=input("\nenter your name: ")              
balan=float(input("\nEnter you account balance: "))
acc= Bank(ano,aname,balan)
i=0
while i!=4:
    print("MENU\n1.Deposit\n2.Withdraw\n3.Balance\n4.Exit: ")  
    i=int(input("enter your choice")) 
    if i==1:
        amount=float(input("Enter your amount:"))
        acc.deposit(amount)  
        acc.balance()
        
    elif i==2:
        amount=float(input("Enter your amount to debit:"))
        minbal=float(input("Enter minimum balance of your account:"))
        acc.withdraw(amount,minbal)  
        acc.balance()
        
    else:
        acc.balance()
      
        

        
    
    