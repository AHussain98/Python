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
