# str is the only datatype that stores text and is immutable
# strings are sequences that can only store unicode text
# strings can be converted into binary data, and the opposite way around

# Python strings are immutable. This is also true for byte sequences. This is an important fact,
# because it has both advantages and disadvantages. It also affects the way strings should be
# handled in Python efficiently. Thanks to immutability, strings can be used as dictionary
# keys or set collection elements because, once initialized, they will never change their
# value. On the other hand, whenever a modified string is required (even with only tiny
# modification), a completely new instance needs to be created. Fortunately, bytearray, as a
# mutable version of bytes, does not have such an issue. Byte arrays can be modified inplace (without creating new objects) through item assignments and can be dynamically
# resized, exactly like lists – using appends, pops, inserts, and so on

# concatenating immutable sequences results in the creation of a new sequence object

# Consider that a new string is
# built by repeated concatenation of multiple strings, as follows:
# substrings = ["These ", "are ", "strings ", "to ", "concatenate."]
# s = ""
# for substring in substrings:
#  s += substring

# This will result in quadratic runtime costs in the total string length. In other words, it is
# highly inefficient. For handling such situations, the str.join() method is available. It
# accepts iterables of strings as the argument and returns joined strings. The call to join() of
# the str type can be done in two forms:
# # using empty literal
# s = "".join(substrings)
# # using "unbound" method call
# str.join("", substrings)
# The first form of the join() call is the most common idiom. The string that provides this
# method will be used as a separator between concatenated substrings

# CPython uses various techniques to optimize your code. The first optimization takes place
# as soon as source code is transformed into the form of the abstract syntax tree, just before it
# is compiled into byte code. CPython can recognize specific patterns in the abstract syntax
# tree and make direct modifications to it. The other kind of optimizations are handled by the
# peephole optimizer. It implements a number of common optimizations directly on Python's
# byte code. As we mentioned earlier, constant folding is one such feature. It allows the
# interpreter to convert complex literal expressions (such as "one" + " " + "thing", " "
# * 79, or 60 * 1000) into a single literal that does not require any additional operations
# (concatenation or multiplication) at runtime

# lists and tuples both represent sequences of objects, lists are dynamic and tuples are immutable
# tuple is immutable and hashable

# Many programmers easily confuse Python's list type with the concept of linked lists
# which are found often in standard libraries of other languages, such as C, C++, or Java. In
# fact, CPython lists are not lists at all. In CPython, lists are implemented as variable length
# arrays. This should be also true for other implementations, such as Jython and IronPython,
# although such implementation details are often not documented in these projects. The
# reasons for such confusion is clear. This datatype is named list and also has an interface
# that could be expected from any linked list implementation.

# Lists in Python are contiguous arrays of references to other objects. The pointer to this array
# and the length is stored in the list's head structure. This means that every time an item is
# added or removed, the array of references needs to be resized (reallocated). Fortunately, in
# Python, these arrays are created with exponential over allocation, so not every operation
# requires an actual resize of the underlying array. This is how the amortized cost of
# appending and popping elements can be low in terms of complexity. Unfortunately, some
# other operations that are considered cheap in ordinary linked lists have relatively high
# computational complexity in Python:
# Inserting an item at an arbitrary place using the list.insert method has
# complexity O(n)
# Deleting an item using list.delete or using the del operator har has
# complexity O(n)
# At least retrieving or setting an element using an index is an operation where cost is
# independent of the list's size, and the complexity of these operations is always O(1).

# For situations where a real linked list or doubly linked list is required, Python provides
# a deque type in the collections built-in module. This is a data structure that allows us to
# append and pop elements at each side with O(1) complexity. This is a generalization of
# stacks and queues, and should work fine anywhere where a doubly linked list is required.

# As you probably know, writing a piece of code such as this can be tedious:
# >>> evens = []
# >>> for i in range(10):
# ... if i % 2 == 0:
# ... evens.append(i)
# ...
# >>> evens
# [0, 2, 4, 6, 8]
# This may work for C, but it actually makes things slower for Python for the following
# reasons:
# It makes the interpreter work on each loop to determine what part of the
# sequence has to be changed
# It makes you keep a counter to track what element has to be processed
# It requires additional function lookups to be performed at every iteration
# because append() is a list's method
# A list comprehension is a better pattern for these kind of situations. It allows us to define a
# list by using a single line of code:
# >>> [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]
# This form of writing is much shorter and involves fewer elements. In a bigger program, this
# means less bugs and code that is easier to understand. This is the reason why many
# experienced Python programmers will consider such forms as being more readable.

# use enumerate when you need to get an index from elements in a sequence

# If you need to aggregate elements of multiple lists (or any other iterables) in the one-by-one
# fashion, you can use the built-in zip(). This is a very common pattern for uniform iteration
# over two same-sized iterables:
# >>> for items in zip([1, 2, 3], [4, 5, 6]):
# ... print(items)
# ...
# (1, 4)
# (2, 5)
# (3, 6)

# dictionaries can also be created using comprehensions, with the same benefits

# CPython uses hash tables with pseudo-random probing as an underlying data structure for
# dictionaries. It seems like a very deep implementation detail, but it is very unlikely to
# change in the near future, so it is also a very interesting fact for the Python programmer.
# Due to this implementation detail, only objects that are hashable can be used as a
# dictionary key. An object is hashable if it has a hash value that never changes during its
# lifetime, and can be compared to different objects. Every Python built-in type that is
# immutable is also hashable. Mutable types, such as list, dictionaries, and sets, are not
# hashable, and so they cannot be used as dictionary keys. Protocol that defines if a type is
# hashable consists of two methods:
# __hash__: This provides the hash value (as an integer) that is needed by the
# internal dict implementation. For objects that are instances of user-defined
# classes, it is derived from their id().
# __eq__: This compares if two objects have the same value. All objects that are
# instances of user-defined classes compare as unequal by default, except for
# themselves.
# Two objects that are compared as equal must have the same hash value. The reverse does
# not need to be true. This means that collisions of hashes are possible – two objects with the
# same hash may not be equal. It is allowed, and every Python implementation must be able
# to resolve hash collisions CPython uses open addressing to resolve such collisions. The
# probability of collisions greatly affects dictionary performance, and, if it is high, the
# dictionary will not benefit from its internal optimizations.

# While three basic operations, adding, getting, and deleting an item, have an average time
# complexity equal to O(1), their amortized worst case complexities are a lot higher. It is O(n),
# where n is the current dictionary size. Additionally, if user-defined class objects are used as
# dictionary keys and they are hashed improperly (with a high risk of collisions), this will
# have a huge negative impact on the dictionary's performance.

# Sets are a very robust data structure that are mostly useful in situations where the order of
# elements is not as important as their uniqueness. They are also useful if you need to
# efficiently check efficiency if the element is contained in a collection. Sets in Python are
# generalizations of mathematic sets, and are provided as built-in types in two flavors:
# set(): This is a mutable, non-ordered, finite collection of unique, immutable
# (hashable) objects
# frozenset(): This is an immutable, hashable, non-ordered collection of unique,
# immutable (hashable) object

# Sets in CPython are very similar to dictionaries. As a matter of fact, they are implemented
# like dictionaries with dummy values, where only keys are actual collection elements. Sets
# also exploit this lack of values in mapping for additional optimizations.
# Thanks to this, sets allow very fast additions, deletions, and checks for element existence
# with the average time complexity equal to O(1). Still, since the implementation of sets in
# CPython relies on a similar hash table structure, the worst case complexity for these
# operations is still O(n), where n is the current size of a set.
# Other implementation details also apply. The item to be included in a set must be hashable,
# and, if instances of user-defined classes in the set are hashed poorly, this will have a
# negative impact on their performance.
# Despite their conceptual similarity to dictionaries, sets in Python 3.7 do not preserve the
# order of elements in specification, or as a detail of CPython implementation.

# dictionaries preserve the order of element entry, sets do not

# python also has an enum module
# Enum definition is
# immutable and global. It should be used whenever there is a closed set of possible values
# that can't change dynamically during program runtime, and especially if that set should be
# defined only once and globally. Dictionaries and named tuples are data containers. You can
# create as many instances of them as you like

# an iterator is a container object that implements the iterator protocol
# This protocol consists of two methods:
# __next__: This returns the next item of the container
# __iter__: This returns the iterator itself
# Iterators can be created from a sequence using the iter built-in function

i = iter('abc')
print(next(i))
print((next(i)))
print(next(i))
#print(next(i))  # throws

# When the sequence is exhausted, a StopIteration exception is raised. It makes iterators
# compatible with loops, since they catch this exception as a signal to end the iteration. If you
# create a custom iterator, you need to provide objects with the implementation of __next__,
# which iterates the state of the object, and the __iter__ method, which returns the iterable.

# Generators provide an elegant way to write simple and efficient code for functions that
# return a sequence of elements. Based on the yield statement, they allow you to pause a
# function and return an intermediate result. The function saves its execution context and can
# be resumed later, if necessary.
# For instance, the function that returns consecutive numbers of the Fibonacci sequence can
# be written using a generator syntax. The following code is an example that was taken
# from the PEP 255 (Simple Generators) document:

# def fibonacci():
#  a, b = 0, 1
#  while True:
#    yield b
#    a, b = b, a + b

# You can retrieve new values from generators as if they were iterators, so using
# the next() function or for loops:
# >>> fib = fibonacci()
# >>> next(fib)
# 1
# >>> next(fib)
# 1
# >>> next(fib)
# 2
# >>> [next(fib) for i in range(10)]

# [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
# Our fibonacci() function returns a generator object, a special iterator, which knows
# how to save the execution context. It can be called indefinitely, yielding the next element of
# the sequence each time. The syntax is concise, and the infinite nature of the algorithm does
# not disturb the readability of the code. It does not have to provide a way to make the
# function stoppable. In fact, it looks similar to how the sequence generating function would
# be designed in pseudocode.

# In many cases, the resources required to process one element are less than the resources
# required to store whole sequences. Therefore, they can be kept low, making the program
# more efficient. For instance, the Fibonacci sequence is infinite, and yet the generator that
# generates it does not require an infinite amount of memory to provide the values one by
# one and, theoretically, could work ad infinitum. A common use case is to stream data
# buffers with generators (for example, from files). They can be paused, resumed, and
# stopped whenever necessary at any stage of the data processing pipeline without any need
# to load whole datasets into the program's memory.

# generators let us interact with code thats called with next(), the yield becomes an expression

def greeting():
    print('How are you?')
    while True:  # generators work in loops
        answer = (yield)  # yield statement is an expression
        if 'good' in answer:
            print('Thats great!')
        elif 'bad' in answer:
            print("aw shame!")

free = greeting()  # generator object captured
next(free)
free.send('Im good thanks')  # send function sends your response to the yield expression

# The send() method acts similarly to the next() function, but makes
# the yield statement return the value passed to it inside of the function definition. The
# function can, therefore, change its behavior depending on the client code. Two other
# methods are available to complete this behavior: throw() and close(). They allow us to
# inject exceptions into the generator:
# throw(): This allows the client code to send any kind of exception to be raised.
# close(): This acts in the same way, but raises a specific
# exception, GeneratorExit. In this case, the generator function must
# raise GeneratorExit again, or StopIteration.


# a decorator is any function that recieves a function and returns an enhanced one, just a wrapper

# The decorator is generally a named callable object (lambda expressions are not allowed)
# that accepts a single argument when called (it will be the decorated function) and returns
# another callable object. Callable is used here instead of a function with premeditation.
# While decorators are often discussed in the scope of methods and functions, they are not
# limited to them. In fact, anything that is callable (any object that implements
# the __call__ method is considered callable) can be used as a decorator, and, often, objects
# returned by them are not simple functions but are instances of more complex classes that
# are implementing their own __call__ method.

# The decorator syntax is simply a syntactic sugar. Consider the following decorator usage:
# @some_decorator
# def decorated_function():
#  pass
# This can always be replaced by an explicit decorator call and function reassignment:
# def decorated_function():
#  pass
# decorated_function = some_decorator(decorated_function)
# However, the latter is less readable and also very hard to understand if multiple decorators
# are used on a single function.

def repeat(number = 3):  # parameterised decorator
    # cause decorated function to be called a number of times
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs) # call the function
        return wrapper  # call the wrapper function
    return actual_decorator  # call the actual decorator function

@repeat(2)
def print_my_call():
    print("print my call!")

print_my_call()  # will now be called twice

# the with statement is used as a context manager
# Any object that implements the context manager protocol can be used as a context
# manager. This protocol consists of two special methods:
# __enter__(self): This allows you to define what should happen before
# executing the code that is wrapped with context manager and returns context
# variable
# __exit__(self, exc_type, exc_value, traceback): This allows you to
# perform additional cleanup operations after executing the code wrapped with
# context manager, and captures all exceptions that were raised in the process
# In short, the execution of the with statement proceeds as follows:
# 1. The __enter__ method is invoked. Any return value is bound to target the
# specified as clause.
# 2. The inner block of code is executed.
# 3. The __exit__ method is invoked.
# __exit__ receives three arguments that are filled when an error occurs within the code
# block. If no error occurs, all three arguments are set to None. When an error occurs,
# the __exit__() method should not re-raise it, as this is the responsibility of the caller. It
# can prevent the exception being raised, though, by returning True. This is provided to
# allow for some specific use cases, such as the contextmanager decorator, which we will
# see in the next section. But, for most use cases, the right behavior for this method is to do
# some cleanup, as would be done by the finally clause. Usually, no matter what happens
# in the block, it does not return anything

# Functions in Python are first-class objects, so whenever you use a function name,
# you're actually using a variable that is a reference to the function object. As with any other
# function, lambda functions are first-class citizens, so they can also be assigned to a new
# variable. Once assigned to a variable, they are seemingly undistinguishable from other
# functions, except for some metadata attributes.

# >>> def circle_area(radius):
# ... return math.pi * radius ** 2
# ...
# >>> circle_area(42)
# 5541.769440932395
# >>> circle_area
# <function circle_area at 0x10ea39048>
# >>> circle_area.class
# <class 'function'>
# >>> circle_area.name
# 'circle_area'
# >>> circle_area = lambda radius: math.pi * radius ** 2
# >>> circle_area(42)
# 5541.769440932395
# >>> circle_area
# <function <lambda> at 0x10ea39488>
# >>> circle_area.__class__
# <class 'function'>
# >>> circle_area.__name__
# '<lambda>'

# The map(), filter(), and reduce() functions are three built-in functions that are most
# often used in conjunction with lambda functions. They are commonly used in functional
# style Python programming because they allow us to declare data transformations of any
# complexity, while simultaneously avoiding side-effects.

# map(fun, iterable, ...) applies the func function argument to every item of
# iterable. You can pass more iterables to the map() function. If you do so, map() will
# consume elements from each iterable simultaneously. The func function will receive as
# many items as there is iterables on every map step. If iterables are of different sizes, map()
# will stop until the shortest one is exhausted. It is worth remembering that map() does not
# evaluate the whole result at once, but returns an iterator so that every result item can be
# evaluated only when it is necessary.

# The following is an example of map() being used to calculate the squares of the first 10
# positive integers, including 0:
# >>> map(lambda x: x**2, range(10))
# <map object at 0x10ea09cf8>
# >>> list(map(lambda x: x**2, range(10)))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# filter(function, iterable) works similarly to map() by evaluating input elements
# one by one. Unlike map(), the filter() function does not transform input elements into
# new values, but allows us to filter out those input values that meet the predicate defined by
# the function argument. The following are examples of the filter() functions usage:
# >>> evens = filter(lambda number: number % 2 == 0, range(10))
# >>> odds = filter(lambda number: number % 2 == 1, range(10))
# >>> print(f"Even numbers in range from 0 to 9 are: {list(evens)}")
# Even numbers in range from 0 to 9 are: [0, 2, 4, 6, 8]
# >>> print(f"Odd numbers in range from 0 to 9 are: {list(odds)}")
# Odd numbers in range from 0 to 9 are: [1, 3, 5, 7, 9]

# The reduce(function, iterable) works completely opposite to map(). Instead of
# taking items of iterable and mapping them to the function return values in a one-byone fashion, it cumulatively performs operations specified by function to
# all iterable items. Let's consider following the example of reduce() calls being used to
# sum values of elements contained in various iterable objects:
# >>> from functools import reduce
# >>> reduce(lambda a, b: a + b, [2, 2])
# 4
# >>> reduce(lambda a, b: a + b, [2, 2, 2])
# 6
# >>> reduce(lambda a, b: a + b, range(100))
# 4950

## The Python data model specifies a lot of specially named methods that can be overridden in
# your custom classes to provide them with additional syntax capabilities. You can recognize
# these methods by their specific naming conventions that wrap the method name with
# double underscores. Because of this, they are sometimes referred to as dunder. It is simply
# a speech shorthand for double underscores.

# Callable protocol __call__() Allows objects to be called with the parentheses syntax:
# instance()

# Descriptor protocols __set__(), __get__(), and __del__() Allows us to manipulate the attribute access pattern of classes (see the Descriptors section)

# Container protocol __contains__() Allows us to test whether or not an object contains some value using the in keyword:
# value in instance

# Iterable protocol __iter__()
# Allows objects to be iterated over using the for
# keyword:
# for value in instance:
# ...

# Sequence protocol
# __len__(),
# __getitem__()
# Allows objects to be indexed with square
# bracket syntax and queried for length using a
# built-in function:
# item = instance[index]
# length = len(instance)


# The same dunder convention is also used for specific attributes of custom user functions
# and is used to store various metadata about Python objects. These attributes are as follows:
# __doc__: A writable attribute that holds the function's documentation. It is, by
# default, populated by the docstring function.
# __name__: A writable attribute that holds the function's name.
# __qualname__: A writable attribute that holds the function's qualified name.
# The qualified name is a full dotted path to the object (with class names) in the
# global scope of the module where the object is defined.
# __module__: A writable attribute that holds the name of the module that
# function belongs to.
# __defaults__: A writable attribute that holds the default argument values if the
# function has any.
# __code__: A writable attribute that holds the function's compile code object.
# __globals__: A read-only attribute that holds the reference to the dictionary of
# global variables for that function's scope. The global scope for a function is the
# namespace of the module where this function is defined
# __dict__: A writable attribute that holds a dictionary of function attributes.
# Functions in Python are first-class objects, so they can have any arbitrary
# arguments defined, just like any other object.
# __closure__: A read-only attribute that holds a tuple of cells with the function's
# free variables. Closure cells allow you to create parametrized function decorators.
# __annotations__: A writable attribute that holds the function's argument and
# return annotations.
# __kwdefaults__: A writable attribute that holds the default argument values
# for keyword-only arguments if the function has any.

# A built-in type,
# called object is a common ancestor for all built-in types, as well as for all user-defined
# classes that have no explicit parent class specified. Thanks to this, every time you need to
# implement a class that behaves almost like one of the built-in types, the best practice is to
# subtype it.

# When you are about to create a new class that acts like a sequence or a
# mapping, think about its features and look over the existing built-in types.
# The collections module extends basic lists of built-in types with many
# useful containers. You will often end up using one of them without
# needing to create your custom subclasses.

# super is a built-in class that can be used to access an attribute belonging to an object's
# superclass

class Mama:
    def says(self):
        print("clean your room")

class Sister(Mama):
    def says(self):
        super().says()  # super refers to the base class
        print("and be quiet")


s = Sister()
s.says()

# when you
# face a multiple inheritance schema, it becomes hard to use super. Before explaining these
# problems, you need to first understand when super should be avoided and how
# the Method Resolution Order (MRO) works in Python.

# super accesses base classes based on the order they appear in the MRO, so if not every class is using super in the __init__() member functions, this causes problems
# all in all, diamond inheritance, super, and multiple inheritance should be avoided

# if you call a class member function that is defined in a parent class, the function is found via MRO
# Python Merge Resolution Order, C3 does a recursive depth lookup on each parent to get a sequence of lists.
# Then, it computes a left-to-right rule to merge all lists with a hierarchy disambiguation,
# when a class is involved in several lists.
# e.g. a class that inherits from base1 and base 2, both of ehich inherit from commonbase, which inherits from object:
# >>> L(MyClass)
# ['MyClass', 'Base1', 'Base2', 'CommonBase', 'object']
# The __mro__ attribute of a class (which is read-only) stores the result of
# the linearization computation. Computation is done when the class
# definition is loaded.
# You can also call MyClass.mro() to compute and get the result.

# Now, back to the super() call. If you deal with multiple inheritance hierarchy, it can
# become problematic. This is mainly due to the initialization of classes. In Python, the
# initialization methods (that is, the __init__() methods) of base classes are not implicitly
# called in ancestor classes if ancestor classes override __init__(). In such cases, you need
# to call superclass methods explicitly, and this can sometimes lead to initialization problems.
# To avoid such issues, super should be used in the whole class hierarchy

# A descriptor lets you customize what should be done when you refer to an attribute of an
# object.
# Descriptors are the base of a complex attribute access in Python. They are used internally to
# implement properties, methods, class methods, static methods, and the super type. They
# are classes that define how attributes of another class can be accessed. In other words, a
# class can delegate the management of an attribute to another one.
# The descriptor classes are based on three special methods that form the descriptor protocol:
# __set__(self, obj, value): This is called whenever the attribute is set. In
# the following examples, I will refer to this as a setter.
# __get__(self, obj, owner=None): This is called whenever the attribute is
# read (referred to as a getter).
# __delete__(self, obj): This is called when del is invoked on the attribute.
# A descriptor that implements __get__() and __set__() is called a data descriptor. If it
# just implements __get__(), then it is called a non-data descriptor

# Methods of this protocol are, in fact, called by the object's
# special __getattribute__() method (do not confuse it with __getattr__(), which has
# a different purpose) on every attribute lookup. Whenever such a lookup is performed,
# either by using a dotted notation in the form of instance.attribute, or by using
# the getattr(instance, 'attribute') function call, the __getattribute__() method
# is implicitly invoked and it looks for an attribute in the following order:
# 1. It verifies whether the attribute is a data descriptor on the class object of the
# instance.
# 2. If not, it looks to see whether the attribute can be found in
# the __dict__ lookup of the instance object.
# 3. Finally, it looks to see whether the attribute is a non-data descriptor on the class
# object of the instance.
# In other words, data descriptors take precedence over __dict__ lookup,
# and __dict__ lookup takes precedence over non-data descriptors.

# class RevealAccess(object):
#  """A data descriptor that sets and returns values
#  normally and prints a message logging their access.
#  """
#  def __init__(self, initval=None, name='var'):
#  self.val = initval
#  self.name = name
#  def __get__(self, obj, objtype):
#  print('Retrieving', self.name)
#  return self.val
#  def __set__(self, obj, val):
#  print('Updating', self.name)
#  self.val = val

# Metaclass is a type (class) that defines other types (classes)
# classes that define objects are objects too, and if they are object then they must have an associated class
# object instances are instances of a class, which is an instance of a type
# the bsic type of every class definition is simply the built-in type class

# In Python, it is possible to substitute the metaclass for a class object with our own type.
# Usually, the new metaclass is still the subclass of the type class

# Every class that's created with the class statement implicitly uses type as its metaclass. This
# default behavior can be changed by providing the metaclass keyword argument to the
# class statement,

class ClassWithMetaclass(metaclass=type):
    pass

# The value that's provided as a metaclass argument is usually another class object, but it
# can be any other callable that accepts the same arguments as the type class and is expected
# to return another class object. The call signature is type(name, bases, namespace) and
# the meaning of the arguments are as follows:
# name: This is the name of the class that will be stored in the __name__ attribute
# bases: This is the list of parent classes that will become the __bases__ attribute
# and will be used to construct the MRO of a newly created class
# namespace: This is a namespace (mapping) with definitions for the class body
# that will become the __dict__ attribute

# The Python syntax is converted into AST before it is compiled into byte code. This is a tree
# representation of the abstract syntactic structure of the source code. Processing of Python
# grammar is available thanks to the built-in ast module. Raw ASTs of Python code can be
# created using the compile() function with the ast.PyCF_ONLY_AST flag, or by using
# the ast.parse() helper. Direct translation in reverse is not that simple and there is no
# function provided in the standard library that can do so. Some projects, such as PyPy, do
# such things though

