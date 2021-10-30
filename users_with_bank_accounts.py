class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance" + ' $' + str(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(0,0)
    def display_balance(self):
        print("User: " + self.name, " Balance: " + str(self.account.balance))
        return self

clown = User("Clown")
orange = User("Orange")
apple = User("Apple")
clown.account.deposit(12).deposit(17).deposit(143).withdraw(4020)
clown.display_balance()
orange.account.deposit(4080).deposit(1000).withdraw(70).withdraw(50)
orange.display_balance()
apple.account.deposit(1000).withdraw(857).withdraw(2000).withdraw(7)
apple.display_balance()