from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self, target):
        pass

# Классы конкретных типов оружия
class Sword(Weapon):
    def attack(self, target):
        print("Боец наносит удар мечом.")
        target.health -= 10

class Bow(Weapon):
    def attack(self, target):
        print("Боец наносит удар из лука.")
        target.health -= 7

# Класс Fighter
class Fighter:
    def __init__(self, weapon: Weapon, health: int = 100):
        self.weapon = weapon
        self._health = health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health <= 0:
            self._health = 0
            print("Боец побежден!")

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self, target):
        self.weapon.attack(target)

# Класс Monster
class Monster:
    def __init__(self, health: int = 50):
        self._health = health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health <= 0:
            self._health = 0
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
print(f"Здоровье монстра: {monster.health}")

# Боец меняет оружие на лук
fighter.changeWeapon(bow)

# Боец атакует монстра из лука
fighter.attack(monster)
print(f"Здоровье монстра: {monster.health}")

# Монстр атакует бойца (пример использования, можно реализовать атаку для монстра)
monster_attack_damage = 20
fighter.health -= monster_attack_damage
print(f"Здоровье бойца: {fighter.health}")

# Еще одна атака бойца
fighter.attack(monster)
print(f"Здоровье монстра: {monster.health}")
