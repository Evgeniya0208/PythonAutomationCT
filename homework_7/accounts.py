from itertools import count


class Account:
    id_obj = count(start=26001)

    def __init__(self, balance: float):
        self.account_number = next(Account.id_obj)
        self._balance = balance

    def deposit(self, amount: float):
        self._balance += amount

    def withdraw(self, amount: float):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("You don't have enough funds.")

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value


class SavingsAccount(Account):
    def __init__(self, balance: float, interest_rate: float):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        self._balance += self.interest_rate * self._balance / 100


class CheckingAccount(Account):
    def __init__(self, balance: float, transaction_fee: float):
        super().__init__(balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        self._balance -= self.transaction_fee

    def withdraw(self, amount: float):
        if self._balance >= amount:
            self._balance -= amount
            self.deduct_transaction_fee()
        else:
            print("You don't have enough funds.")

    def deposit(self, amount: float):
        self._balance += amount
        self.deduct_transaction_fee()


def account_summary(account: Account):
    print(f"Account type: {account}, Account number: {account.account_number}, Balance: {account.get_balance()}")


checking_account = CheckingAccount(500.25, 7.15)
account_summary(checking_account)
checking_account.deposit(200)
account_summary(checking_account)
checking_account.withdraw(50)
account_summary(checking_account)
checking_account.withdraw(12.71)
account_summary(checking_account)

savings_account = SavingsAccount(750, 8)
account_summary(savings_account)
savings_account.calculate_interest()
account_summary(savings_account)
