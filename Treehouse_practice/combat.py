import random

class combat:
    dodge_index= 6
    attack_index=6

    def dodging(self):
        roll= random.randint(1, self.dodge_index)
        return self.dodge_index> roll
    def attacking(self):
        roll=random.randint(1, self.attack_index)
        return self.attack_index> roll
