
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


acc = BankAccount("Alice", 100)
print(acc.deposit(50))
print(acc.withdraw(30))
print(acc.withdraw(200))


