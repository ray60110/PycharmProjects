from combat import combat
from monster import monster
import random

class Character(combat):
    attach_index=10
    base_healthpoint=10
    attack=1
    exp=0

    def attacking(self):
        roll= random.randint(1, self.attach_index)
        if self.weapon=='sword':
            roll+= 1
            self.attack+=1
        elif self.weapon== 'axe':
            self.attack+=3
        elif self.weapon=='knife':
            roll+=3
        return roll> 4

    def get_weapon(self):
        weapon_choice= input('Pick a weapon you like: [S]word, [A]xe, [K]nife ?' ).lower()
        if weapon_choice in 'sabk':
            if weapon_choice== 's':
                return 'sword'
            elif weapon_choice=='a':
                return 'axe'
            elif weapon_choice=='k':
                return 'knife'
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name= input('Hello hero, please tell me your name: ')
        self.occupation=input('What occupation are you: ')
        self.weapon= self.get_weapon()
        self.healthpoint= self.base_healthpoint
        for key, value in kwargs:
            setattr(self, key, value)

    def __str__(self):
        return "{} {}, HP:{}, EXP:{}".format(self.name,
                                             self.occupation,
                                             self.healthpoint,
                                             self.exp)

    def rest(self):
        if self.healthpoint<= self.base_healthpoint:
            self.healthpoint +=1

    def leveled_up(self):
        if self.exp>=5:
            self.attach_index+=1
            self.base_healthpoint+=5
            self.dodge_index+=1

    def got_hit(self):
        self.healthpoint-= self.monster.attack
        return self.healthpoint