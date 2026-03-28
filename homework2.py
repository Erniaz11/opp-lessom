from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, target):
        pass

    def take_damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            print("Персонаж погиб")


class Warrior(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self, target):
        target.take_damage(self.strength)


class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def attack(self, target):
        target.take_damage(self.mana)


class Archer(Character):
    def __init__(self, name, health, arrows):
        super().__init__(name, health)
        self.arrows = arrows

    def attack(self, target):
        target.take_damage(5)


w = Warrior("A", 100, 20)
m = Mage("B", 80, 15)
a = Archer("C", 90, 10)

chars = [w, m, a]

for c in chars:
    c.attack(w)
