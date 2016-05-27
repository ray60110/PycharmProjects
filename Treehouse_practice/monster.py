import random
from combat import combat
COLORS=['yellow', 'black', 'green', 'gold']

class monster(combat):
    min_healthpoint=1
    max_healthpoint=10
    min_exp=1
    max_exp=10
    roar='roar'
    attack=1

    def __init__(self, **kwargs):
        self.color= random.choice(COLORS)
        self.healthpoint= random.randint(self.min_healthpoint, self.max_healthpoint)
        self.exp= random.randint(self.min_exp, self.max_exp)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{} {}, HP: {}, EXP: {}".format(self.color,
                                               self.__class__.__name__,
                                               self.healthpoint,
                                               self.exp)

    def battlecry(self):
        return self.roar.upper()
class goblin(monster):
    max_healthpoint = 5
    max_exp = 4
    attack=2
    roar = 'golin'

class slime(monster):
    max_healthpoint = 3
    max_exp = 2

class dragon(monster):
    min_healthpoint = 50
    max_healthpoint = 100
    min_exp = 40
    max_exp = 200
    attack=5
    roar = 'hoaarrrrrr'

