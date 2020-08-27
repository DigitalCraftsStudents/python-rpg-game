"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
class Charachter:

    def __init__(self, power, health, name):
        self.power = power
        self.health = health
        self.name = name
    
    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))


    def alive(self):
        if self.health > 0:
            return True
        else:
            return False      
class Hero(Charachter): 

    def attack(self, enemy):
        # Hero attacks enemy
        enemy.health -= self.power
        print("Hero does %d damage to the %s." % (self.power, enemy.name))
        if enemy.health <= 0:
            print("The %s is dead." % enemy.name)


hero = Hero(10, 50, 'Hero')

class Goblin(Charachter): #a class always has two things, it has attributes[height,weight,power] and methods[code which can be inputed]. 
    
    def attack(self,hero):
        # Goblin attacks hero
        hero.health -= self.power
        print("The goblin does %d damage to %s." % (self.power, hero.name))
        if hero.health <= 0:
            print(" Hero is dead.")
goblin = Goblin(15,100,'Goblin')



class Zombie(Charachter):
    def attack(self, hero):
        # zombie attacks hero
        hero.health -= self.power
        print("The zombie does %d damage to %s." % (self.power, hero.name))
        if hero.health <= 0:
            print(" Hero is dead.")

zombie = Zombie(10,1000,'Zombie')

# class Falconman(Charachter):
#     def attack(self, zombie)
#     zombie.


def main():

    while goblin.alive() and hero.alive() and zombie.alive():
        hero.print_status()
        goblin.print_status()
        zombie.print_status()

        # print("You have %d health and %d power." % (hero.health, hero.power))
        # print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("1.5 fight the zombie who appeared out of nowhere.")
        print("1.75 attack the zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack(goblin)
            if goblin.health > 0:
                goblin.attack(hero)
        elif user_input =="1.5":
            zombie.attack(hero)
        elif user_input == "2":
                goblin.attack(hero)
        elif user_input == "1.75":
            hero.attack(zombie)
        elif user_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        
            

main()