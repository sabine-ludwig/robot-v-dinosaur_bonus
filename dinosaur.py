class Dinosaur:

    def __init__(self, name, sttack_power):
        self.name = name
        self.attack_power = 40
        self.health = 100

    def dino_attack(self, robot):
        self.robot = robot
        robot.health -= self.attack_power
        print(f"{self.name} attacks {robot.name}.")
        print(f"{robot.name} loses {self.attack_power} health and now has {robot.health} health reamining.")
