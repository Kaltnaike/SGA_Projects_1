#Creatina a Class called BankAccount
class BankAccount:

    def __init__(self):
        self.balance=0
        print("Welcome to Awonaike Trust Bank!")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("  Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("  Dear Customer You Withdrew:", amount)
        else:
            print("  Insufficient balance  ")
 
    def display(self):
        print("  Net Available Balance=",self.balance)
        print('Thanks for Banking with Us!')
 
 
Customer_1 = BankAccount()


Customer_1 .deposit()
Customer_1 .withdraw()
Customer_1 .display()