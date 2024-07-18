from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Классы конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")

# Класс Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self):
        self.weapon.attack()

# Класс Monster
class Monster:
    def __init__(self, health: int):
        self.health = health

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {self.health} здоровья.")

# Пример использования

# Создаем оружие
sword = Sword()
bow = Bow()

# Создаем бойца с мечом
fighter = Fighter(sword)

# Создаем монстра с 100 единицами здоровья
monster = Monster(100)

# Боец атакует монстра мечом
fighter.attack()
monster.take_damage(50)  # Предположим, что меч наносит 50 урона

# Боец меняет оружие на лук
fighter.changeWeapon(bow)

# Боец атакует монстра из лука
fighter.attack()
monster.take_damage(50)  # Предположим, что лук наносит 50 урона



