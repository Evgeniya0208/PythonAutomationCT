class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("You don't have enough funds.")

    def get_balance(self):
        return self.balance


account = BankAccount("1111", 100.23)
account.deposit(101.03)
print(account.get_balance())
account.withdraw(17.37)
print(account.get_balance())
account.withdraw(1700)
