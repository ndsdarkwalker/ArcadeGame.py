import random

class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def __str__(self):
        return "{}: {}".format(self.name, self.damage)
weapons = [
    Weapon("Có súng đây nè", 100),
    Weapon("Nam Huỳnh Đạo", 50),
    Weapon("Khóa mõm cực mạnh", 200),
    Weapon("Đấm phát chết luôn", 100)
]
class Fighter():
    def __init__(self, name, HP, weapon):
        self.name = name
        self.HP = HP
        self.weapon = weapon

    def __str__(self):
        return "This is: {} HP: {} Weapon: {}".format(self.name, self.HP, self.weapon)

    def attack(self, opponent):
        print("{} attack {}".format(self.name, opponent.name))
        opponent.HP = opponent.HP - self.weapon.damage

player1 = Fighter("Trần Dần", 1000, random.choice(weapons))
player2 = Fighter("Hai Vụ", 1000, random.choice(weapons))

print(player1, "VS", player2)

while player1.HP > 0 and player2.HP > 0:
    player1.attack(player2)
    print(player1, "*" * 5, player2)
    player2.attack(player1)
    print(player1, "*" * 5, player2)
    if player1.HP <= 0:
        print(player1.name, "LOSE!")
    elif player2.HP <= 0:
        print(player2.name, "LOSE!")
    else:
        print("HÒA!")
