import random 

class Weapons:

    def __init__(self):
        self.choose_weapon()
        self.display_choice()

    def choose_weapon(self):
        self.weapon_types = ["laser", "machine gun", "flame thrower"]
        print()
        print("Below are your weapon options.")
        print()

        self.chosen_weapon = ''

        while True:
            for i, weapon in enumerate(self.weapon_types):
                print(f" {i + 1}. {weapon.title()}")
            print()
            self.weapon_type = int(input("Which type of weapon would you like to use (enter number corresponding to preferred weapon type) > "))
            if self.weapon_type in range(1, (len(self.weapon_types) + 1)):
                self.chosen_weapon += self.weapon_types[self.weapon_type - 1]
                return self.chosen_weapon
            print("Sorry, that is not an option. Please enter the number that corresponds with the weapon you would like to use.")

    def display_choice(self):         
        self.weapon_damage = [30, 40, 50]

        print(f"You have selected the {self.chosen_weapon.title()}")
        print(f"For this round, the {self.chosen_weapon.title()} will have a damage level of {random.choice(self.weapon_damage)}.")





