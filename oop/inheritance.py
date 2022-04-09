class Mortal:
    def __init__(self, lifespan=80):
        self.lifespan = lifespan

    def is_breathing(self):
        print('Yes it can breath')

    def eats(self):
        print('It is eating')

    def what_is_this():
        print('it is a Mortal function')


class Earthling:
    def __init__(self, planet='earth'):
        self.lifespan = 50
        self.planet = planet

    def lives_in_earth(self):
        print('Yes it leaves in earth')


class Animal(Mortal, Earthling):
    def __init__(self, lifespan, species='mammal'):
        super().__init__(lifespan)
        self.species = species

    def log(self):
        print('. . .Random animal sound. . .')


class Rat(Animal):
    def sound(self):
        print(' . making rat sounds  ')


class Human(Mortal):

    def introduce(self):
        print(f'My name is {self.name}')

    # make it a private property getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, name):
        self._name = name

    # deleter
    @name.deleter
    def name(self):
        del self._name

    # static method

    def describe_class():
        print('This is a test class to learn oop')

    # when you convert to string
    # If tou don't have this everytme you print it will show onject in memory
    def __str__(self):
        print('converting to string')
        return 'this is a class Human with name ' + self.name

    # Comparing to objects
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


# h1 = Human('Ricardo')
# h1.introduce()

# You can add atributes
# h1.can_fly = True

# Static method, methods are that are not attched to object but to class
# Human.describe_class()

# h2 = Human()
# print(h1 == h2)

# h1.is_breathing()

# a1 = Animal(101)
# a1.is_breathing()
# a1.log()


# print(a1.lifespan)
# print(h1.lifespan)


# Use print(help( class )) to see the class
# print(help(Animal))

# All methods and magic methods of object
# print(dir(a1))

# Animal.what_is_this()
# print(a1.lifespan)

r1 = Rat(10, 'hybrid')
# r1.eats()
# r1.lives_in_earth()
# r1.sound()
# print(help(Rat))
# print(dir(r1.__class__.__class__.__itemsize__.__add__))


# Why there is no error??
print(dir(r1.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__))
