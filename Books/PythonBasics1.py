import sys

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





