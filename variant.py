from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self, monster):
        pass

# Классы конкретных типов оружия
class Sword(Weapon):
    def attack(self, monster):
        print("Боец наносит удар мечом.")
        monster.defeat()

class Bow(Weapon):
    def attack(self, monster):
        print("Боец наносит удар из лука.")
        monster.defeat()

# Класс Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self, monster):
        self.weapon.attack(monster)

# Класс Monster
class Monster:
    def defeat(self):
        print("Монстр побежден!")

# Пример использования

# Создаем оружие
sword = Sword()
bow = Bow()

# Создаем бойца с мечом
fighter = Fighter(sword)

# Создаем монстра
monster = Monster()

# Боец атакует монстра мечом
fighter.attack(monster)

# Боец меняет оружие на лук
fighter.changeWeapon(bow)

# Боец атакует монстра из лука
fighter.attack(monster)

