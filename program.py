#import actors
import random
import time
from actors import Wizard, Creature

#test commit
def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------------------')
    print('         Wizard Battle           ')
    print('---------------------------------')





def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Morgana', 75)

    while True:

        active_creature = random.choice(creatures)
        print('\nA {} of level {} has appeared!'.format(active_creature.name, active_creature.level))
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('Wizard takes a nap.')
                time.sleep(1)
                print('ZzZ')
                time.sleep(1)
                print('zZz')
                time.sleep(1)
                print('Wizard returns revitalized!')
        elif cmd == 'r':
            print('Wizard dips.')
        elif cmd == 'l':
            print('Wizard looks around and sees:')
            for c in creatures:
                print(' - A {} of level {}'.format(c.name, c.level))
        else:
            print('exiting game')
            break


if __name__ == '__main__':
    main()