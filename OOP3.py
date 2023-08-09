# in python, unlike C++, its normal to keep classes and definitions within the same file as the working programme
import random

class Player(object):
    # The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach.
    # The __init__ function is called every time an object is created from a class.
    # The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.
    def __init__(self, name):
        self.name = name
        self._lives = 3  # lets make this underscore lives to invoke name mangling, somewhat hiding this variable
        self.level = 1 # default values
        self._score = 0

    def __str__(self):
        return (f"Name is {self.name}, lives are {self.lives}, level is {self.level}, score is {self.score}")
        # when we print a class object, python searches for the __str__ function and executes it
    # now we can create getters and setters to create some kind of encapsulation of the level variable

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives > 0:
            self._lives = lives
        else:
            print("Invalid number of lives!")

    # now we have to make the lives variable a member of the class
    lives = property(_get_lives,_set_lives)  # you don't need to include self in here, or parenthesis
    # now when someone tries to change lives, the get lives and set lives methods are invoked.
    # the data attribute must never have the same name as the property, or else recursive overflow error
    # for a property method, you only provide the names of the get and set functions, dont include parenthesis as we dont want to call them

    # lets also make score accessible via the property decorator
    @property  # the decorator comes before the method, this is the decorator for the getter
    def score(self):
        return self._score

    @score.setter  # decorator for the setter
    def score(self, score):
        self._score = score

   # so we have two overloads for the score() method, one getter and one setter
   #Overall, the difference between attributes and properties in Python is that attributes are simply data members of an object,
   # while properties are methods that are accessed like attributes but actually perform some computation when called.

Asad = Player("Asad")

print(Asad.name)
Asad.level = 16 # not protected, can be changed wherever we want from outside the class
# in python, this is considered the correct way to do things
# in python, if you need getters and setters, you can make the variables begin with an underscore
# this will help hide them and then you can create get and set methods in the class to access them
print(Asad.level)

print(Asad)  # executes the __str__ method

Asad.lives = 20  # okay
Asad.lives = 0 # not okay

Asad.score = 1000
print(Asad)

# in python, classes can inherit directly from multiple superclasses, this is multiple inheritance

#class Enemy:
class Enemy(object):  # same thing

    def __init__(self, name="Enemy", hit_points = 0, lives = 1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True
        self.stored_hit_points = hit_points

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            self.hit_points = self.stored_hit_points  # reset the hit points when a life is lost
            if self.lives == 0:
                self.alive = False
                print(f"{self.name} is dead!")


    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, hit points: {self.hit_points}"

# now lets create an enemy object
print()


minion = Enemy("minion", 12, 1)
print(minion)
minion.take_damage(7)
print(minion)

# lets try creating a troll class which inherits from the enemy class

# an important point is that python does not have the concept of overloaded methods
# the last one you define is teh one used, regardless of the number of parameters you now define


class Troll(Enemy): # this is inheritance syntax in python

    def __init__(self, name = "None"):  # as soon as we add this init to the derived class, the base method of the superclass will not be used
        # but we can add the init method for the superclass in here instead by using the super keyword
        super().__init__(name = name, lives = 2, hit_points= 25)

    def grunt(self):
        print(f"{self.name} is grunting!")


basic_troll = Troll() # no args given, default values used (will use the init for the superclass if the init in derived class is not defined
print(basic_troll)
brute = Troll("Brute") # all args given
print(brute)
# since python doesnt have overloadng of methods, there are no extra constructors you can define
# so the same constructor is used for the two above methods
# we can get the same behaviour as overloaded functions in C++ by using named parameters with default values, as above
# but if you tried to pass no arguments for an object when its constructor does not have default values, you will get an error

brute.grunt()

class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodge(self):  # we can build this behaviour into the class, by redefining the take damage method
        if random.randint(1,3) == 3:
            print(f"{self.name} dodges the attack!")
            return True
        else:
            return False
    # in python, method overriding is done by simply creating a new method with the same name
    # the parameters and number of them don't matter, only the name

    def take_damage(self, damage):
        if not self.dodge():  # now a third of all attacks are dodged
            super().take_damage(damage=damage)

vamp = Vampire("Vlad")
print(vamp)

while vamp.alive:
    vamp.take_damage(1)
    print(vamp)

# inheritance is useful because the derived classes take in all useful behaviour from the superclass
# we can then extend this behaviour as we see above

class VampireKing(Vampire): # vampire king extends vampire, so the vampire methods are called, not enemy
    # however the calls are passed up, so where vampire calls enemy, the enemy function is called too

    def __init__(self, name):
        super().__init__(name)  # so super() here is allowing us to access the superclass which is vampire
        self.hit_points = 140

    def take_damage(self, damage):  # vampire king takes less damage
        super().take_damage( damage // 4)  # integer division

drac = VampireKing("dracula")
while drac.alive:
    drac.take_damage(120)
    print(drac)

# you don't always need to use inheritance, it should be obvious when to use it
# python relies heavily on polymorphism
# for example, all python objects inherit from a base class called object which defines a __str__ method
# polymorphism allows the print function to accept arguments of any type, and have the ability to print them
# all objects behave the same way as far as the print() function is concerned
print()

class Wing():
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wheeeeeee")
        else:
            print("I'll just walk")

class Duck(object): # the object arg here is not necessary

    def __init__(self):
        self._wing = Wing(1.8) # ducks now have a wing, so we can apply a wing object as a member of the duck class

    def walk(self):
        print("waddle")

    def swim(self):
        print("paddle")

    def quack(self):
        print("quack")

    def fly(self):
        self._wing.fly()  # call the fly function via the wing object that's part of the class

class Penguin(object): # penguin does not extend duck but has same method names

    def walk(self):
        print("penguin waddle")

    def swim(self):
        print("swim better")

    def quack(self):
        print("no chance mate")

def test_duck(duck):
    duck.swim()
    duck.quack()
    duck.walk()

# inheritance is used when something has a 'is a' relationship with another object
# aggregation and composition are used when something has a 'has/uses a' relationship with another object
# above where the duck class contains a wing object as a member, this is called composition
# aggregation is where we create the object seperately, and then pass it into the constructor of another object
# so in composition, the object is responsible for the lifespan of the object it contains
# in aggregation, this is not the case, the lifespans are independent



if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    pingu = Penguin()
    test_duck(pingu)  # we can call the same method with a different object as they have the same method names
    # this is how python deals with objects due to its dynamic typing
    # if the object has the required characteristics, it can be used
    # we know pingu is not a duck, but python only cares about what something can do, now what it is
    # this is polymorphism in python
    donald.fly() # donald can fly



