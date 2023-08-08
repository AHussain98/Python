# in python, unlike C++, its normal to keep classes and definitions within the same file as the working programme

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
