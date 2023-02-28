class bank():
    def __init__(self):
        self.name=input("Enter the name:")
        self.bid=int(input("Enter the id:"))
        self.type=input("Account type:")
        self.balance=0
        print("SBI")
    def deposit(self):
        self.amount=int(input("Enter the amount:"))
        self.balance=self.balance+self.amount
        print("Succesfull depositing")
    def withdraw(self):
        self.wamount=int(input("Enter amount to withdraw"))
        if(self.balance>=self.wamount):
            self.balance=self.balance-self.wamount
            print("after withdrawal",self.balance)
        else:
            print("sorry")
    def show(self):
        print(self.name)
        print(self.bid)
        print(self.type)
        print(self.balance)
obj=bank()
repeat=True
while(repeat):
    ch=int(input("Enter the choice  [1.deposit,2.withdraw,3.show]:"))
    if(ch==1):
        obj.deposit()
    elif(ch==2):
        obj.withdraw()
    elif(ch==3):
        obj.show()
    else:
        print("INVALID")