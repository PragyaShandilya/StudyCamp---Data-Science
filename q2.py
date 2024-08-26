#Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
class bank:
    def __init__(self, acc_no,bal=1000):
        self.acc_no = acc_no
        self.bal = bal
        ch = int(input("Select\n1.Withdrawl\n2.Deposit\n"))
        if ch==1:
            self.withdrawl()
        elif ch==2:
            self.deposit()
        else:
            print("Incorrect Choice")
    
    def withdrawl(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount< self.bal: 
            self.bal = self.bal - amount
            print("Balance updated\nBalance = ", self.bal)
        else:
            print("Not enough balance")
    
    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.bal = self.bal + amount
        print("Amount updated\n Balance = ", self.bal)

obj1 = bank(1234,5000)

        

