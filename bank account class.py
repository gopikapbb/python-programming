class bankaccount:
    def __init__(self):
        self.balance=0
        print("CANARA BANK")
    def deposite(self):
        amount=int(input("Enter the amount:"))
        self.balance=self.balance+amount
        print("Deposite amount is:",amount)
    def withdraw(self):
        amount=int(input("Enter the amount to withdraw:"))
        if(self.balance>=amount):
            self.balance=self.balance-amount
            print("Withdrawed",amount)
        else:
            print("Insufficiant balance")
    def display(self):
        print("BALANCE:",self.balance)

s=bankaccount()
s.deposite()
s.withdraw()
s.display()