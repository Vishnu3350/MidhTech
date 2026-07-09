class BankAcc:
    def __init__(self, owner, bal, acc_type, bank_name):
        self.owner = owner
        self.__bal = bal
        self.acc_type = acc_type
        self.bank_name = bank_name
    def show_balance(self):
        print("Owner name: ", self.owner)
        print("Balance :", self. __bal)
        print("Account type: ", self.acc_type)
        print("Bank name: ", self.bank_name)

account = BankAcc("Vishnu", 6000, "Savings", "Kotak")
account.show_balance()




# Example 2

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._account_type = "Savings"
        self.__balance = balance
    
    def deposit(self, amount):
        
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawl Successful")
        else:
            print("Insufficient Balance")
    
    def show_balance(self):
        print("Balance: ",self.__balance)

account = BankAccount("Vishnu", 6000)
print("Owner_name: ", account.owner)    
print("Account type: ", account._account_type)

account.deposit(5000)
account.withdraw(10000)
account.show_balance()

        
