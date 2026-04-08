from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self._name = name 
        self.__salary = 0  
        self.set_salary(salary)

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        if value < 0:
            raise ValueError("Зарплата не может быть меньше 0")
        self.__salary = value

    @abstractmethod
    def work(self):
        pass

    @classmethod
    def create_from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))

    @staticmethod
    def is_valid_name(name):
        return len(name) >= 2

    def __str__(self):
        return f"{self._name} - {self.__salary}"

    def __len__(self):
        return len(self._name)

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.get_salary() == other.get_salary()
        return False
 
class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")


class BonusMixin:
    def add_bonus(self, amount):
        new_salary = self.get_salary() + amount
        self.set_salary(new_salary)


class Developer(Employee, LoggerMixin, BonusMixin):
    def work(self):
        return "Пишет код"


class Manager(Employee, LoggerMixin):
    def work(self):
        return "Управляет командой"

if __name__ == "__main__":
    dev = Developer("Beka", 1000)
    manager = Manager("Aida", 1500)

    dev2 = Developer.create_from_string("Nurs,2000")

    print(Employee.is_valid_name("A"))     
    print(Employee.is_valid_name("Tim"))   
    employees = [dev, manager, dev2]

    for emp in employees:
        print(emp.work())

    print(dev)          
    print(len(dev))      
    print(dev == dev2)   

    dev.log("Разработчик начал работу")
    dev.add_bonus(500)
    print(dev)
