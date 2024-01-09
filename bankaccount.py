class BankAccount:
    def __init__(self,acc_holder_name,acc_no,bal):
        self.acc_holder_name=acc_holder_name
        self.acc_no = acc_no
        self.bal = bal
    def deposit(self,amount):
        if(amount>0):
            self.bal=self.bal+amount
    def withdraw(self,amount):
        if(amount>self.bal):
            print("Insufficient funds")
        else:
            self.bal = self.bal - amount
            return self.bal
    def display(self):
        print("Account holder Name:" , self.acc_holder_name)
        print("Account number: ", self.acc_no)
        print("Balance available: ", self.bal)

