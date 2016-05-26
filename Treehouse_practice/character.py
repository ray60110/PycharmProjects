from combat import combat
import random

class Character(combat):
    attach_index=10
    base_healthpoint=10
    weapon= 'bare hands'
    exp=0

    def attacking(self):
        roll= random.randint(1, self.attach_index)
        if self.weapon=='sword':
            roll+= 1
        elif self.weapon== 'axe':
            roll+= 2
        return roll> 4

    def get_weapon(self):
        weapon_choice= input('[S]word, [A]xe, [B]ow, [K]nife ?' ).lower()
        if weapon_choice in 'sabk':
            if weapon_choice== 's':
                return 'sword'
            elif weapon_choice=='a':
                return 'axe'
            elif weapon_choice=='b':
                return 'bow'
            elif weapon_choice=='k':
                return 'knife'
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name= input('please give your name: ')
        self.occupation=input('what occupation are you: ')
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