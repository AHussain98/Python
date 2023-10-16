import requests
import sys
import os
import hashlib
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# In Python, using a variable before it has been assigned a value is always an error—
# otherwise, if names were filled in with defaults, some errors might go undetected. This
# means you must initial counters to zero before you can add to them, must initial lists
# before extending them, and so on; you don’t declare variables, but they must be assigned before you can fetch their values

# To save programs permanently, you need to write your code in files, which are usually
# known as modules. Modules are simply text files containing Python statements. Once
# they are coded, you can ask the Python interpreter to execute the statements in such a
# file any number of times, and in a variety of ways—by system command lines, by file
# icon clicks, by options in the IDLE user interface, and more. Regardless of how it is
# run, Python executes all the code in a module file from top to bottom each time you
# run the file

print(sys.platform)  # page 107

# Python programs are composed of multiple module files linked together
# by import statements, and each module file is a package of variables—that is, a namespace. Just as importantly, each module is a self-contained namespace: one module file
# cannot see the names defined in another file unless it explicitly imports that other file.
# Because of this, modules serve to minimize name collisions in your code—because each
# file is a self-contained namespace, the names in one file cannot clash with those in
# another, even if they are spelled the same way.

# Frozen binary executables are packages that combine your
# program’s byte code and the Python interpreter into a single executable program. This
# approach enables Python programs to be launched in the same ways that you would
# launch any other executable program (icon clicks, command lines, etc.). While this
# option works well for delivery of products, it is not really intended for use during program development; you normally freeze just before shipping (after development is finished).

# 1. Programs are composed of modules.
# 2. Modules contain statements.
# 3. Statements contain expressions.
# 4. Expressions create and process objects.

# Data types:
# Numbers 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
# Strings 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
# Lists [1, [2, 'three'], 4.5], list(range(10))
# Dictionaries {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
# Tuples (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
# Files open('eggs.txt'), open(r'C:\ham.bin', 'wb')
# Sets set('abc'), {'a', 'b', 'c'}
# Other core types Booleans, types, None
# Program unit types Functions, modules, classes
# Implementation-related types Compiled code, stack tracebacks

# Every object in Python is classified as either immutable (unchangeable) or not. In terms
# of the core types, numbers, strings, and tuples are immutable; lists, dictionaries, and
# sets are not—they can be changed in place freely, as can most new objects you’ll code
# with classes

# The Python list object is the most general sequence provided by the language. Lists are
# positionally ordered collections of arbitrarily typed objects, and they have no fixed size.
# They are also mutable—unlike strings, lists can be modified in place by assignment to
# offsets as well as a variety of list method calls.

# In a nutshell, an object is iterable if it is either a physically stored sequence in memory,
# or an object that generates one item at a time in the context of an iteration operation
# —a sort of “virtual” sequence. More formally, both types of objects are considered
# iterable because they support the iteration protocol—they respond to the iter call with
# an object that advances in response to next calls and raises an exception when finished
# producing values.

# The tuple object (pronounced “toople” or “tuhple,” depending on whom you ask) is
# roughly like a list that cannot be changed—tuples are sequences, like lists, but they are
# immutable, like strings. Functionally, they’re used to represent fixed collections of
# items: the components of a specific calendar date, for instance. Syntactically, they are
# normally coded in parentheses instead of square brackets

# Variables are simply names—created by you or Python—that are used to keep track of
# information in your program. We’ll say more about this in the next chapter, but in
# Python:
# • Variables are created when they are first assigned values.
# • Variables are replaced with their values when used in expressions.
# • Variables must be assigned before they can be used in expressions.
# • Variables refer to objects and are never declared ahead of time.

# X / Y
# Classic and true division. In Python 2.X, this operator performs classic division,
# truncating results for integers, and keeping remainders (i.e., fractional parts) for
# floating-point numbers. In Python 3.X, it performs true division, always keeping
# remainders in floating-point results, regardless of types.
# X // Y
# Floor division. Added in Python 2.2 and available in both Python 2.X and 3.X, this
# operator always truncates fractional remainders down to their floor, regardless of
# types. Its result type depends on the types of its operands.

#In Python, types are determined automatically at runtime, not
#in response to declarations in your code. This means that you never declare variables
#ahead of time (a concept that is perhaps simpler to grasp if you keep in mind that it all
#boils down to variables, objects, and the links between them)

# These links from variables to objects are called references in Python—that is, a reference
# is a kind of association, implemented as a pointer in memory.1 Whenever the variables
# are later used (i.e., referenced), Python automatically follows the variable-to-object
# links. This is all simpler than the terminology may imply. In concrete terms:
# • Variables are entries in a system table, with spaces for links to objects.
# • Objects are pieces of allocated memory, with enough space to represent the values
# for which they stand.
# • References are automatically followed pointers from variables to objects.
# At least conceptually, each time you generate a new value in your script by running an
# expression, Python creates a new object (i.e., a chunk of memory) to represent that
# value. As an optimization, Python internally caches and reuses certain kinds of unchangeable objects, such as small integers and strings (each 0 is not really a new piece
# of memory—more on this caching behavior later). But from a logical perspective, it
# works as though each expression’s result value is a distinct object and each object is a
# distinct piece of memory.

# Now let’s introduce another variable into our interaction and watch what happens to
# its names and objects:
# >>> a = 3
# >>> b = a
# The second
# command causes Python to create the variable b; the variable a is being used and not
# assigned here, so it is replaced with the object it references (3), and b is made to reference
# that object. The net effect is that the variables a and b wind up referencing the same
# object (that is, pointing to the same chunk of memory).

# One way to think of this is that, unlike in some languages, in Python variables are always
# pointers to objects, not labels of changeable memory areas: setting a variable to a new
# value does not alter the original object, but rather causes the variable to reference an
# entirely different object. The net effect is that assignment to a variable itself can impact
# only the single variable being assigned. When mutable objects and in-place changes
# enter the equation, though, the picture changes somewhat;

# f we change this statement’s syntax slightly, however, it has a radically different effect:
# >>> L1 = [2, 3, 4] # A mutable object
# >>> L2 = L1 # Make a reference to the same object
# >>> L1[0] = 24 # An in-place change
# >>> L1 # L1 is different
# [24, 3, 4]
# >>> L2 # But so is L2!
# [24, 3, 4]
# Really, we haven’t changed L1 itself here; we’ve changed a component of the object that
# L1 references. This sort of change overwrites part of the list object’s value in place.
# Because the list object is shared by (referenced from) other variables, though, an inplace change like this doesn’t affect only L1—that is, you must be aware that when you
# make such changes, they can impact other parts of your program. In this example, the
# effect shows up in L2 as well because it references the same object as L1. Again, we
# haven’t actually changed L2, either, but its value will appear different because it refers
# to an object that has been overwritten in place.
# This behavior only occurs for mutable objects that support in-place changes, and is
# usually what you want, but you should be aware of how it works, so that it’s expected.
# It’s also just the default: if you don’t want such behavior, you can request that Python
# copy objects instead of making references. There are a variety of ways to copy a list,
# including using the built-in list function and the standard library copy module.

# remember strings are immutable in Python

# The immutable classification is an important constraint to be aware of, yet it tends to
# trip up new users. If an object type is immutable, you cannot change its value in place;
# Python raises an error if you try. Instead, you must run code to make a new object
# containing the new value. The major core types in Python break down as follows:
# Immutables (numbers, strings, tuples, frozensets)
# None of the object types in the immutable category support in-place changes,
# though we can always run expressions to make new objects and assign their results
# to variables as needed.
# Mutables (lists, dictionaries, sets, bytearray)
# Conversely, the mutable types can always be changed in place with operations that
# do not create new objects. Although such objects can be copied, in-place changes
# support direct modification.
# Generally, immutable types give some degree of integrity by guaranteeing that an object
# won’t be changed by another part of a program.

# an example of an fstring, potentially superior to .format
name = 'Asad'
print(f"My name is {name}")

# Technically, Python lists contain zero or more references to other objects. Lists
# might remind you of arrays of pointers (addresses) if you have a background in
# some other languages. Fetching an item from a Python list is about as fast as indexing a C array;

# lists are mutable so they can be changed in place
L = [1,2,3,4,5]
L[2] = 20
print(L)

M = L.reverse()  # even though we've assigned it, L has still been reversed, M is none here as reverse returns None
M = reversed(L) # this won't leave L as the reversed version
print(L)

# As we saw earlier, because slice assignment is a deletion plus an insertion, you can also
# delete a section of a list by assigning an empty list to a slice (L[i:j]=[]); Python deletes
# Lists in Action | 249
# the slice named on the left, and then inserts nothing. Assigning an empty list to an
# index, on the other hand, just stores a reference to the empty list object in the specified
# slot, rather than deleting an item:
# >>> L = ['Already', 'got', 'one']
# >>> L[1:] = []
# >>> L
# ['Already']
# >>> L[0] = []
# >>> L
# [[]]

# keys in a dictionary can only be immutable types

# ike strings and lists, tuples are sequences; they support many of the same operations. However, like strings, tuples are immutable; they don’t support any of the
# in-place change operations applied to lists.

# t data read from a file always comes back to your script as
# a string, so you’ll have to convert it to a different type of Python object if a string
# is not what you need. Similarly, unlike with the print operation, Python does not
# add any formatting and does not convert objects to strings automatically when you
# write data to a file—you must send an already formatted string

# • The == operator tests value equivalence. Python performs an equivalence test,
# comparing all nested objects recursively.
# • The is operator tests object identity. Python tests whether the two are really the
# same object (i.e., live at the same address in memory).

#  if a collection object contains
# a reference to itself, it’s called a cyclic object. Python prints a [...] whenever it detects
# a cycle in the object, rather than getting stuck in an infinite loop (as it once did long ago):
# >>> L = ['grail'] # Append reference to same object
# >>> L.append(L) # Generates cycle in object: [...]
# >>> L
# ['grail', [...]]

# Python assignments store references to objects in names or data structure components. They
# always create references to objects instead of copying the objects. Because of that,
# Python variables are more like pointers than data storage areas

# The concept of “iterable objects” is relatively recent in Python, but it has come to
# permeate the language’s design. It’s essentially a generalization of the notion of sequences—an object is considered iterable if it is either a physically stored sequence, or
# an object that produces one result at a time in the context of an iteration tool like a
# for loop. In a sense, iterable objects include both physical sequences and virtual sequences computed on demand

# #the bestway to read a text file line by line today is to not read it at all—instead, allow the for
# #loop to automatically call __next__ to advance to the next line on each iteration. The
# #file object’s iterator will do the work of automatically loading lines as you go. The
# #following, for example, reads a file line by line, printing the uppercase version of each
# #line along the way, without ever explicitly reading from the file at all:
# #>>> for line in open('script2.py'): # Use file iterators to read by lines
# #... print(line.upper(), end='') # Calls __next__, catches StopIteration
# #...
# #IMPORT SYS
# #PRINT(SYS.PATH)
# #X = 2
# #PRINT(X ** 32)
# #Notice that the print uses end='' here to suppress adding a \n, because line strings
# #already have one (without this, our output would be double-spaced; in 2.X, a trailing
# #comma works the same as the end). This is considered the best way to read text files
# #line by line today, for three reasons: it’s the simplest to code, might be the quickest to
# #run, and is the best in terms of memory usage. The older, original way to achieve the
# #same effect with a for loop is to call the file readlines method to load the file’s content
# #into memory as a list of line strings
#
# # for loops are faster than while loops, iterator-based for loop version, because iterators run at C language speed inside Python, whereas the while loop version runs Python
# # byte code through the Python virtual machine. Anytime we trade Python code for C
# # 418 | Chapter 14: Iterations and Comprehensions
# # code, speed tends to increase. This is not an absolute truth, though,

# To simplify manual iteration code, Python 3.X also provides a built-in function, next,
# that automatically calls an object’s __next__ method. Per the preceding note, this call
# also is supported on Python 2.X for portability. Given an iterator object X, the call
# next(X) is the same as X.__next__() on 3.X (and X.next() on 2.X), but is noticeably
# simpler and more version-neutral. With files, for instance, either form may be used:
# >>> f = open('script2.py')
# >>> f.__next__() # Call iteration method directly
# 'import sys\n'
# >>> f.__next__()
# 'print(sys.path)\n'
# >>> f = open('script2.py')
# >>> next(f) # The next(f) built-in calls f.__next__() in 3.X
# 'import sys\n'
# >>> next(f) # next(f) => [3.X: f.__next__()], [2.X: f.next()

# Technically, there is one more piece to the iteration protocol alluded to earlier. When
# the for loop begins, it first obtains an iterator from the iterable object by passing it to
# the iter built-in function; the object returned by iter in turn has the required next
# method. The iter function internally runs the __iter__ method, much like next and
# __next__.

# list comprehensions are usually faster than for loops, prefer these whenever possible

#  in Python, your code is not supposed to care about
# specific data types. If it does, it will be limited to working on just the types you anticipated when you wrote it, and it will not support other compatible object types that
# may be coded in the future. Although it is possible to test for types with tools like the
# type built-in function, doing so breaks your code’s flexibility. By and large, we code to
# object interfaces in Python, not data types.

# With a
# def statement:
# • Name assignments create or change local names by default.
# • Name references search at most four scopes: local, then enclosing functions (if any),
# then global, then built-in.
# • Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes, respectively.

# Python’s name-resolution scheme is sometimes called the LEGB rule, after the scope
# names:
# • When you use an unqualified name inside a function, Python searches up to four
# scopes—the local (L) scope, then the local scopes of any enclosing (E) defs and
# lambdas, then the global (G) scope, and then the built-in (B) scope—and stops at
# the first place the name is found. If the name is not found during this search, Python
# reports an error.
# • When you assign a name in a function (instead of just referring to it in an expression), Python always creates or changes the name in the local scope, unless it’s
# declared to be global or nonlocal in that function.
# • When you assign a name outside any function (i.e., at the top level of a module
# file, or at the interactive prompt), the local scope is the same as the global scope—
# the module’s namespace.
Z = 10 # global variable
def func(Y):
    X = Y + Z  # X and Y are local to the function, Z is just a reference to the global Z value

# Python’s pass-by-assignment scheme isn’t quite the same as C++’s reference parameters option, but it turns out to be very similar to the argument-passing model of the C
# language (and others) in practice:
# • Immutable arguments are effectively passed “by value.” Objects such as integers and strings are passed by object reference instead of by copying, but because
# you can’t change immutable objects in place anyhow, the effect is much like making
# a copy.
# • Mutable arguments are effectively passed “by pointer.” Objects such as lists
# and dictionaries are also passed by object reference, which is similar to the way C
# passes arrays as pointers—mutable objects can be changed in place in the function,
# much like C arrays.

# prefer list comprehensions wherever possible over for loops, they're faster
res = [x for x in range(-5,5) if x > 0]
print(res)

# list comprehensions return new lists so cant be used to make unplace changes to lists, as they produce a new one

#  map calls can be twice as fast
# as equivalent for loops, and list comprehensions are often faster than map calls. This
# speed difference can vary per usage pattern and Python, but is generally due to the fact
# that map and list comprehensions run at C language speed inside the interpreter, which
# is often much faster than stepping through Python for loop bytecode within the PVM.

# • Generator functions (available since 2.3) are coded as normal def statements, but
# use yield statements to return results one at a time, suspending and resuming their
# state between each.
# • Generator expressions (available since 2.4) are similar to the list comprehensions
# of the prior section, but they return an object that produces results on demand
# instead of building a result list.

# Because neither constructs a result list all at once, they save memory space and allow
# computation time to be split across result requests. As we’ll see, both of these ultimately
# perform their delayed-results magic by implementing the iteration protocol

# The chief code difference between generator and normal functions is that a generator
# yields a value, rather than returning one—the yield statement suspends the function
# and sends a value back to the caller, but retains enough state to enable the function to
# resume from where it left off.

def genSquares(N: int):
    for i in range(N):
        yield i*i

x = genSquares(5)   # create a generator object
print(next(x))   #  call the next function, move generator object on
print(next(x))
print(next(x))
print(next(x))
print(next(x))

G = (x**2 for x in range(4))  # Generator expression
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(G)  # generator object

# generators are iterator objects that support the iterator protocol automatically
# this is why the next function works with them

# generators can still return a value after the function is called

# in Python, imports are not just textual insertions
# of one file into another. They are really runtime operations that perform three distinct
# steps the first time a program imports a given file:
# 1. Find the module’s file.
# 2. Compile it to byte code (if needed).
# 3. Run the module’s code to build the objects it defines.

# : when we use a * instead of specific
# names, we get copies of all names assigned at the top level of the referenced module.

#The only time you really must use import instead of from is when you must use the same name defined in two different modules.

# As we’ve seen, a module’s code is run only once per process by default. To force a
# module’s code to be reloaded and rerun, you need to ask Python to do so explicitly by
# calling the reload built-in function

# As a special case, you can prefix names with a single underscore (e.g., _X) to prevent
# them from being copied out when a client imports a module’s names with a from *
# statement. This really is intended only to minimize namespace pollution; because from
# * copies out all names, the importer may get more than it’s bargained for (including
# names that overwrite names in the importer). Underscores aren’t “private” declarations: you can still see and change such names with other import forms, such as the
# import statement

