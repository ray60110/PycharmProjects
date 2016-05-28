from character import Character
from monster import slime, goblin, dragon
import sys
import random

class game(Character):
    print('''
    Welcome to the relative RPG game! you are the
    only hero that can slave the monster in this
    world. good luck!
    ''')

    def __init__(self):
        self.setup()
        while self.player.healthpoint and (self.monster or self.monsters):
            print('\n' + '=' * 30)
            print(self.player)

            self.monster_turn()

            print('-' * 20)

            self.player_turn()
            self.cleanup()

            print('\n' + '=' * 30)

        if self.player.healthpoint:
            print('You win!')
        else:
            print('You lose!')
            sys.exit(
            )

    def got_hit(self):
        self.player.healthpoint -= self.monster.attack
        return self.player.healthpoint

    def setup(self):
        self.player= Character()
        self.monsters= [slime(), goblin(), dragon()]
        self.monster= self.get_next_monster()


    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None


    def cleanup(self):
        if self.monster.healthpoint <= 0:
            self.player.exp += self.monster.exp
            print('You have killed {}!'.format(self.monster))
            self.monster = self.get_next_monster()


    def monster_turn(self):
        if self.monster.attacking():
            print("\n{} is attacking!".format(self.monster))
            if input('Dodge? (Y/n)').lower() =='y':
                if self.player.dodging():
                    print('You dodge that!')
                else:
                    print('You was hit!')
                    self.got_hit()
            else:
                print('{} hit you for 1 point!'.format(self.monster))
                self.got_hit()
        else:
            print("{} is missing".format(self.monster))


    def player_turn(self):
        self.player.leveled_up()
        player_choice= input('[R]est, [A]ttack, [Q]uit? \n >').lower()
        try:
            if player_choice == 'a':
                print('You are attacking {}'.format(self.monster))

                if self.player.attacking():
                    if self.monster.dodging():
                        print('\n {} is dodged your attack!'.format(self.monster))
                    else:
                        print('\n {} was hit by you, and you cause {} damage with your {} weapon.'.format(
                            self.monster, self.player.attack, self.player.weapon))
                        self.monster.healthpoint -= self.player.attack
                else:
                    print('\nYou miss!')
            elif player_choice == 'r':
                self.player.rest()
            elif player_choice == 'q':
                sys.exit(

                )
                # exit belong to sys library. that you should import sys.
            else:
                return self.player_turn()
        except:
            pass
game()