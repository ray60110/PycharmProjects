import random

class combat:
    dodge_index= 6
    attack_index=6

    def dodging(self):
        roll= random.randint(1, self.dodge_index)
        return roll > 4
    def attacking(self):
        roll=random.randint(1, self.attack_index)
        return roll > 4
