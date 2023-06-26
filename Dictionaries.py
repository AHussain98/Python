# lists and tuples are sequence types, we can use indexes to access individual items in them
# dictionaries and sets are not sequences, they are mappings,
# dictionaries store key/value pairs, each va,ue has a unique key which is used to refer to it
# a set is an unordered collection of things
# use a dictionary to store keys and values seperated by a colon

vehicles = {"Audi":"DA65MPY", "Clio":"ND12WPT"} # curly brackets used to create dictionary
my_car = vehicles["Audi"] # value accessed using key
print(my_car)
my_old_car = vehicles["Clio"]
print(my_old_car)

# we can also pass the key to the get method

first_car = vehicles.get("Clio")
print(first_car)

# we can add values like so:
vehicles["A7"] = "Next up"
# dictionaries do not have an append method, we assign values to the dictionary by using its key
# dictionaries prserve the insertion order, if your python is 3.6 or newer

# keys must match exactly when we try to use them
# if a key doesn't exist, .get() will return None, whereas indexing will crash the programme
# the get method may be useful when we don't know if the key exists or not
# however indexing is faster

# we can iterate through a dictionary via a for loop
for key in vehicles:
    print(key, vehicles[key], sep=" : ")

# however, we can do the above more efficiently

for key, value in vehicles.items():
    print(key,value, sep = " : " )

# in python, remember to use enumerate when iterating over dequences and .items() when iterating over dictionaries
# enumerate() is faster when you want to repeatedly access the list/iterable items at their index. When you just want a list of indices, it is faster to use len() and range().

# we change values in the dictionary by just assigning a new item to that key
vehicles["Clio"] = "Sold!"
# the insertion order is still preserved even though we've changed the value
