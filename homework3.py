class BankAccount:
    def __init__(self, owner, currency, balance=0):
        self.owner = owner
        self._currency = currency
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if self.ccan_withdraw(amount):
            self.__balance -= amount

    def can_withdraw(self, amount):
        return amount > 0 and amount <= self.__balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value


acc = BankAccount("Alex", "USD", 100)

acc.deposit(50)
print(acc.balance)

acc.withdraw(30)
print(acc.balance)

from abc import ABC, abstractmethod

class AuthSystem(ABC):
    @abstractmethod
    def login(self, username, password):
        pass


class EmailAuth(AuthSystem):
    def login(self, username, password):
        return f"Email login for {username}"


class GoogleAuth(AuthSystem):
    def login(self, username, password):
        return f"Google login for {username}"


class TelegramAuth(AuthSystem):
    def login(self, username, password):
        return f"Telegram login for {username}"


auth = EmailAuth()
print(auth.login("user1", "1234"))

auth2 = GoogleAuth()
print(auth2.login("user2", "abcd"))

