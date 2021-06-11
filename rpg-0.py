from character import Character

# ----------------


def main():
    user_hero = input('What would you like to name your hero? ')
    # hero = Character(user_hero)
    goblin = Character('Goblin', health=20, power=4)
    special  = int(input(f"""
What special would you like, {user_hero}?
1. Max HP
2. + 10 Power
3. Cuddly Pet
> """))
    if special == 1:
        hero = Character(user_hero, health=99999)
        print("\nYOU NOW HAVE 99999 HP.")
    elif special == 2:
        hero = Character(user_hero, health=25, power=15)
        print("\n*10 POWER HAS BEEN ADDED*")
    elif special == 3:
        hero = Character(user_hero)
        cuddlypet = Character('Cuddly Pet', health=999, power=500)
        print(f"\n{cuddlypet.name} stored in inventory.")

    while hero.is_alive and goblin.is_alive:
        print(f'''
~~~~~~~~~~CURRENT STATS~~~~~~~~~~~
{hero}
{goblin}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        print("> ",)
        print("""What do you want to do?
1: fight goblin
2: do nothing
3. flee """)
        user_input = input('> ')
        if user_input == '1':
            hero.attack(goblin)
            if goblin.health <= 0:
                print("The goblin is dead.")
                exit()
        elif user_input == '2':
            pass
        elif user_input == '3':
            print("GOODBYE")
            break
        else:
            # line below not working ?
            print(f"Invalid input {user_input}")
        if goblin.is_alive:
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")
                exit()

main()
