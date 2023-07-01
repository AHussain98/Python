# a set is an unordered collection with no duplicate entries
# the keys to a dictionary are very similar to a set, the main difference is that dictionary keys are ordered
# sets have no ordering, which is why you cant access individual elements of a set

# you can combine sets via the union method, this still ensures that all entries only appear once in the combined set
# however items that appear in both sets are said to be in the intersection of the sets you can also subtract one set
# from another

# sets are created using curly braces

farm_animals = {'cow', 'sheep', 'horse', 'chicken', 'goat'}  # items may not appear in the same order that we type them
# this is because sets are unordered
print(farm_animals)

# iterating over a set:
for animal in farm_animals:
    print(animal)  # unordered, different every time

# sets use hashes to store items, so anything we want to put into a set must be hashable
# same for dictionary keys, cannot be mutable

# you cant index into a set, as its unordered, data is not sequential this also means we cannot slice a set. Python
# considers two sets to be equal if they contain the same items. Ordering is unimportant, it's the items in the set
# that count

# you can use the set function to create a new set, passing any iterable into it
numbers = set("12345")  # this creates a set out of the string literal
print(numbers)
even_numbers = set(range(0, 10, 2))  # a set of even numbers generated via a range
print(even_numbers)

# we test set membership by using the in keyword, as we do with lists, strings and other data structures
if "2" in numbers:
    print("Yay!")
# doing the above with a set is faster than with a list because sets use hashcodes, which search with O(1). If we're
# checking that something is in a list, python will start with the first item and run through the list item by item
# using a set literal instead of the set function is even faster than using the set function

# {} refers to an empty dict by default
# you can create an empty set by doing the following:

empty_set = {*""}
print(type(empty_set))
# can also be written as {*{}}
# can also create an empty set using the set function
numbers = set()
numbers.add(1) # integer value 1 is added to the set
print(numbers)
numbers.add("one") # add won't work if the item is not unique
print(numbers)

data = [5,5,3,1,2,1,2,2,3,4,4,4,5]
unique_data = set(data) # unique values made using set function
print(unique_data) # sets have no ordering, this will appear in a different order each time

# remember that dictionary keys are unique and ordered, so we can use them when we to keep a unique list of items in
# the order that they appear

unique_sorted_data = list(dict.fromkeys(data))
# the from keys method creates a dictionary with the keys we pass to it
# when a new value appears in the data, it replaces the existing value in the dictionary but the insertion order is preserved
print(unique_sorted_data)
# the clear() method clears all items from a set or a dictionary
# to remove an individual item, use the remove() or discard() methods
# remove will raise an exception if the item isnt present
unique_data.discard(5)
print(unique_data)

# sets also have a pop() method
# pop() when used with a set takes no arguments, it removes and returns an arbitrary item from the set

while unique_data:  #this means while there is data in this data structure
    item = unique_data.pop()
    print(item)

# unique_data now empty

farm_animals = {'cow', 'sheep', 'horse', 'chicken', 'goat'}
wild_animals = {"panther", 'fox','horse','goat','bear'}
# two sets with some overlap, some items are the same
# frozenset is an immutable version of set

#union used to create a new set from two sets
all_animals_1 = farm_animals.union(wild_animals) # the animals that appear in both sets, unique
print(all_animals_1)

# union, intersection and difference all return a new set
# we can use the update method to add elements to a set via union without creating a whole new set
# there are also operators for the above methods, but methods are clearer and more flexible, we can pass multiple sets to them on the same line for example

evens = set(range(0,50,2))
odd = set(range(1,50,2))
# the above sets don't have any elements in common

farm_animals.update(wild_animals) # now farm animals has been updated, no new set
print(farm_animals)

farm_animals2 = {'cow', 'sheep', 'horse', 'chicken', 'goat'}
wild_animals2 = {"panther", 'fox','horse','goat','bear'}
print(farm_animals2.intersection(wild_animals2)) # print just values that appear in both sets

# set difference is the set of all items that are in one set and not in the other
print(farm_animals2.difference(wild_animals2))  # so just whats in farm animals 2 but not in wild animals 2
# remember hthat intersection and difference methods have _update versions to just update the original set, and not make any copies
# we can actually pass any iterable to these functions, including lists
