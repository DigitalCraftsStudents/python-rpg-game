class Character:
    def __init__(self, name, health=10, power=5):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, other_person):
        other_person.health -= self.power
        print(f'{self.name} does {self.power} damage to {other_person.name}')
        
    def is_alive(self):
        self.health > 0

    def print_status(self):
        print(f'{self.name} has {self.health} and {self.power}.')

    
