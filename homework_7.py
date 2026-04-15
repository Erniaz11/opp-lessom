import random
import sqlite3

class Gladiator:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self):
        return random.randint(0, self.damage * 2)

g1 = Gladiator("Танк", 100, 10)
g2 = Gladiator("Берсерк", 70, 20)

db = sqlite3.connect("arena.db")
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS results (winner TEXT, loser TEXT, rounds INTEGER)")

round_count = 0
while g1.hp > 0 and g2.hp > 0:
    round_count += 1
    
    dmg1 = g1.attack()
    g2.hp -= dmg1
    print(f"{g1.name} ударил {g2.name} на {dmg1}. У {g2.name} осталось {max(0, g2.hp)}")
    
    if g2.hp <= 0: break
    
    dmg2 = g2.attack()
    g1.hp -= dmg2
    print(f"{g2.name} ударил {g1.name} на {dmg2}. У {g1.name} осталось {max(0, g1.hp)}")

if g1.hp > 0:
    winner, loser = g1.name, g2.name
else:
    winner, loser = g2.name, g1.name

print(f"Победил {winner}!")

cur.execute("INSERT INTO results VALUES (?, ?, ?)", (winner, loser, round_count))
db.commit()
db.close()
