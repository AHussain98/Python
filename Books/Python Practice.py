# Like a def, a class statement is an object builder, and an implicit assignment—when run, it generates a class object and stores a reference to it in the name used in the header
class sharedSpam:
    spam = 50

x = sharedSpam()
y = sharedSpam()

x.spam = 60
print(x.spam, y.spam, sharedSpam.spam)  # only x is changed, we can also access spam through the class

print(sharedSpam.__dict__)  # objects have this attribute which is a dictionary showing what their attributes are mapped to
print(x.__dict__) # same for the instance x
print(x.__class__) # we can see x's class

# we can set a bunch of attributes per class which acts as operator overloading in Python, such as __add__ which defines what happens when one object is + to another
# also can provide facilities for custom indexing of classes etc...

#  the iterator object (with a __next__) produced by an iterable may be defined as a separate class with its own state information to more directly support multiple active iterations over the same data

#  the __init__ constructor is called whenever an instance is generated (and noted how __new__ is run first to make the object). 
#  Its counterpart, the destructor method __del__, is run automatically when an instance’s space is being reclaimed (i.e., at “garbage collection” time):

class Life:
 def __init__(self, name='unknown'):
     print('Hello ' + name)
     self.name = name
 def live(self):
     print(self.name)
 def __del__(self):
     print('Goodbye ' + self.name)

# Because Python automatically reclaims all memory space held by an instance when the instance is reclaimed, destructors are not necessary for space management.

class C:
 def meth(self, x):
     pass
 def meth(self, x, y, z):
     pass
# This code will run, but because the def simply assigns an object to a name in the class’s scope, the last definition of the method function is the only one that will be retained.
# Put another way, it’s just as if you say X = 1 and then X = 2; X will be 2. Hence, there can be only one definition of a method name.

# Name mangling happens only for names that appear inside a class statement’s code,and then only for names that begin with two leading underscores. It works for every
# name preceded with double underscores, though—both class attributes (including method names) and instance attribute names assigned to self. For example, in a class
# named Spam, a method named __meth is mangled to _Spam__meth, and an instance attribute reference self.__X is transformed to self._Spam__X.

x.ape = 10  # added the ape member object after creation of the instance x
print(x.__dict__)
# slots prevent this

class limiter:
   def __init__(self) -> None:
       pass
   __slots__ = ['age', 'name', 'height']  # now the members of limiter class can only be one of these, saves memory and avoids potential code breaks
   
# properties in a class are like getters and setters
class properties(object): # Need object in 2.X for setters
     def getage(self):
         return 40
     def setage(self, value):
         print('set age: %s' % value)
         self._age = value
     age = property(getage, setage, None, None)
     
prop1 = properties()
prop1.age = 50 # runs setage
print(prop1.age)  # returns the age using getage

# it is possible to define two kinds of methods within a class that can be called without an instance: static methods work roughly like simple instance-less
# functions inside a class, and class methods are passed a class instead of an instance. Both are similar to tools in other languages (e.g., C++ static methods).
# static methods cannot access any instance or class data
# class methods can access class data but not instance data

class static_demo:
    num = 10  # num is the same for all instances of the class
    @staticmethod  # declare demo as a static function using this decorator, this is used to make new python work with python 2
    def demo(): 
        print("can be called without an instance as there's no self!")
    def class_demo():  # standard class function
        print("I can access num!" + str(static_demo.num))
    def __init__(self) -> None:
        static_demo.num  = static_demo.num + 10  # so for every instance of the static_demo class, the num variable belonging to the static_demo class increases   


static_demo.demo() # class method called without an instance
a = static_demo()
b = static_demo()

print(b.num)  # num has increased by 20 


# e function decorator syntax:
# @decorator
# def func(args): ...
# is automatically translated to this equivalent by Python, to rebind the function name to the result of the decorator callable:
# def func(args): ...
# func = decorator(func)

# Decoration is a way to specify management or augmentation code for functions and classes. Decorators themselves take the form of callable objects (e.g., functions) that process other callable objects
# These can be of the form of function decorators or class decorators

