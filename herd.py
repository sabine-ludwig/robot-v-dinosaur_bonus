from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.dinosaurs = []
        self.herd_health = 0
        self.create_herd()

    def create_herd(self):
        while True:
            print()
            add_dino = input("Would you like to add a dinosaur to your herd? (Y/N) > ")
            if add_dino == "n".lower():
                break
            elif add_dino == "y".lower():
                print()
                new_dino_type = input("What type of dinosaur would you like to add to your herd? > ").title()
                print()
                new_dino_name = input("What would you like to name your dinosaur? > ").title()
                new_dino = Dinosaur((new_dino_name + " the " + new_dino_type))
                self.dinosaurs.append(new_dino)
                self.herd_health += new_dino.health
            else:
                print("Please type either 'Y' or 'N'.")
                print()
                
        print("Below is your herd of dinosaurs:")
        for dino in self.dinosaurs:
            print(dino.name)
            



