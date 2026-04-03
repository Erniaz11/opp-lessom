
class User:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def add_balance(self, amount):
        self.balance += amount

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, id, name, price, warranty):
        super().__init__(id, name, price)
        self.warranty = warranty

class Clothing(Product):
    def __init__(self, id, name, price, size):
        super().__init__(id, name, price)
        self.size = size

class Cart:
    def __init__(self, user):
        self.user = user
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_price(self):
        return sum(p.price for p in self.products)


user = User(1, "Alex", 1000)

phone = Electronics(1, "Телефон", 500, "12 месяцев")
shirt = Clothing(2, "Футболка", 20, "M")

cart = Cart(user)
cart.add_product(phone)
cart.add_product(shirt)

print("Общая сумма:", cart.get_total_price())  # 520

if user.balance >= cart.get_total_price():
    user.balance -= cart.get_total_price()
    print(f"{user.name} купил товары. Остаток баланса:", user.balance)
else:
    print(f"{user.name} не хватает денег для покупки.")


    from abc import ABC, abstractmethod

class User:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, id, name, price, warranty):
        super().__init__(id, name, price)
        self.warranty = warranty

class Clothing(Product):
    def __init__(self, id, name, price, size):
        super().__init__(id, name, price)
        self.size = size

class Cart:
    def __init__(self, user):
        self.user = user
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_price(self):
        return sum(p.price for p in self.products)
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def __init__(self, user):
        self.user = user

    def pay(self, amount):
        if self.user.balance >= amount:
            self.user.balance -= amount
            return True
        return False

class CryptoPayment(Payment):
    def __init__(self, user):
        self.user = user

    def pay(self, amount):
        if self.user.balance >= amount:
            self.user.balance -= amount
            return True
        return False

user = User(1, "Alex", 1000)
phone = Electronics(1, "Телефон", 500, "12 месяцев")
shirt = Clothing(2, "Футболка", 20, "M")
cart = Cart(user)
cart.add_product(phone)
cart.add_product(shirt)
total = cart.get_total_price()
payment = CardPayment(user)
if payment.pay(total):
    print("Покупка успешна. Баланс:", user.balance)
else:
    print("Недостаточно средств.")



    