from character import Character

# ----------------
"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    hero = Character('Hero')
    goblin = Character('Goblin', health=6, power=2)

    while hero.is_alive and goblin.is_alive:
        hero.print_status
        goblin.print_status
        # print("> ",)
        print("""

What do you want to do?
1: fight goblin
2: do nothing
3. flee
>""",)
        user_input = input()
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
            print(f"Invalid input {user_input}")
        if goblin.is_alive:
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")
                exit()

main()
