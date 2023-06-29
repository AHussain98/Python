import copy

# create a simple dictionary
animals = {"lion" : "Asad",
           "elephant" : ["Big","Fluffy"],
           "teddy" : "Dudu"
           }

# now lets make a refrence to a mutable object
things = animals
print(id(things) == id(animals)) # returns true, things is a reference to the same object as animals
# this is the default behaviour when we make an assignment to a mutable object
# there is only one dictionary, we have two names for it, but fundamentally only one object


# what about immutable objects?
name = "asad","ali","hussain"
print(type(name)) # confirm it is a tuple
more_names = name
print(id(more_names) == id(name)) # still pointing to the same object, because this doesn't really  matter for immutable types
# if we can't mutate a value, then it doesnt really matter if its shallow or deep copied

# we can use the copy function to create our own objects that are identical copies
things = animals.copy()
print(id(things) == id(animals))  # now returns false, things is now bound to a different dictionary object
# so now there are two dictionaries
# however, copy() does a shallow copy, if there are still mutable objects that have been copied over within the animals object,
# then things will still be pointing to those shared objects
# with immutable values, it makes no difference if a copy is shallow or deep
# these copy paradigms matter when values are mutable
# for example, a change to the value with key "elephant" above will carry across between both animals and things
# the reference to the list which is a value in animals is copied over to things, they're both pointing to the same list
print(animals["elephant"])
print(things["elephant"]) # these are the same, even though we've made a copy of the dictionary, its still pointing to the same list
# and if we try appending, the change will carry over into the otehr dictionary
animals["elephant"].append("Cute")
print(animals["elephant"])
print(things["elephant"]) # carried over

# this is what happens when you perform a shallow copy of a container that contains mutable objects
# a shallow copy copies references, it does not make copies of things that are referenced

# this is where deep copy comes in
# to create a deep copy, we can use the copy module performing a deep copy will
# create copies of lists, dictionaries and other mutable objects that are contained in whatever youre copying
# first import the copy module
unique_dict = copy.deepcopy(animals)
animals["elephant"].append("pisstake")
print()

# lets confirm the lists are not the same
print(id(animals["elephant"]) == id(things["elephant"]))
print(id(animals["elephant"]) == id(unique_dict["elephant"])) # returns false, these list objecst are not the same
# unique_dict has its own dict object

print()

print(animals["elephant"])
print(things["elephant"]) # carried over
print(unique_dict["elephant"]) # not carried over
# deep copy gives every reference contained in the container its own unique version in memory
# it does this by copying recursively

# remember that objects we use as keys must be hashable ( it has a hash value that doesn't change over its lifetime)
# dictionary under the hood uses hash table to quickly convert keys into addresses and search there for values two or
# more keys can produce the same hash-code, this is a collision and it will take longer to resolve and retrieve the
# value when this happens
