from weapons import Weapons

class Robot:

    def __init__(self, name):
        self.name = name
        self.active_weapon = Weapons()
        self.health = 100

    def robo_attack(self, dinosaur):
        self.dinosaur = dinosaur 
        dinosaur.health -= self.active_weapon.weapon_damage
        print(f"{self.name} has attacked {dinosaur.name}.")
        print(f"{dinosaur.name} loses {self.active_weapon.weapon_damage} and now has {dinosaur.health} health remaining.")
