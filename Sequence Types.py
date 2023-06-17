# strings are technically sequences, but the main basic sequence types are lists, tuples and ranges
# a sequence is an ordered collection of items, we can refer to items via their index position
# in python, anything you can iterate over, such as a string, is an iterable. All sequence types can be iterables

# the following is a list
computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
# square brackets are used for indexing, slicing and for creating lists

# because this list is a squence type, we can iterate over it in a for loop

for part in computer_parts:
    print(part)

print()  # empty line
print(computer_parts[2])
print(computer_parts[0:3])  # print the first three items in the list
# slicing a list produces another list

# in python, strings are immutable, however lists are mutable, we can change the contents of a list

#immutable types in python: int, flot, bool, str, tuple, frozenset, bytes

# the id() fucntion will give the unique identifaction number for an object across the lifetime of the program, this may or may not be the objects address, depending on your python implemntation

result = True  # bool true has capital T
another_result = result

print(id(result))
print((id(another_result)))   # these are the same, they're both names bound to the same object

result = False
# bind the named variable result to a new value
print(id(result)) # result now has a new id
# because bools are immutable, the True and False objects havent changed, the names have
# This is not the case for mutable objects

# python has mutable objects built in: List, Dict, Set, bytearray

another_computer = computer_parts
print(id(computer_parts))
print(id(another_computer))  # same id for the list object at the moment
computer_parts += ["Alienware"]  # put in square brakcets otherwise it will add one char at a time
print(computer_parts)
print(id(computer_parts))  # notice we have the same id, we've edited the same object, this is becasue lists are mutable, we havent created another list object
# another_computer will also reflect this change, that name has been bound to the same list object as computer_parts
# we can bind multiple names to a list object
a = b = c = d = f = computer_parts

a += ["Aisha"]
print(c)  # change reflected using this name



