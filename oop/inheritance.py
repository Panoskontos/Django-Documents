
class Mortal:
    # def __init__(self):
    #     self.can_die = 'yes it can'

    def can_this_die(self):
        print('Can die')


class Human:
    def __init__(self, name='unknown', skill='nothing'):
        self.name = name
        self.skill = skill
        self.breathes = True

    def introduce_yourself(self):
        print(f'my name is {self.name} and i am good at {self.skill}')

    def walk(self):
        print('is walking')


class Developer(Human, Mortal):
    pass


d1 = Developer()


# d1.can_this_die()
# d1.introduce_yourself()
print(d1.can_die)
# print(d1.breathes)
