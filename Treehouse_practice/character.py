from combat import combat

class Character(combat):
    healthpoint=10
    weapon= 'bare hands'

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
            return get_weapon()

    def __init__(self, **kwargs):
        self.name= input('please give your name: ')
        self.occupation=input('what occupation are you: ')
        self.weapon=get_weapon()
        for key, value in kwargs:
            setattr(self, key, value)

