
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

# we can delete from a dictionary using the del keyword
del vehicles["Clio"]
# accessing a dictionary with a key that doesnt exist will crash your program
# this is why its safer to use the dictionary functions to add and delete itema,s as this won't crash if it fails
# lists and dictionaries have a pop method
vehicles.pop("Brexit", None) # None is the default value
# the pop method removes the value associated with the key you pass
# if the value does not exit, it returns the default value you pass in the second parameter
# thats why the above pop method doesnt cause a crash
result = vehicles.pop("Brexit", None)
print(result)

# lets create a menu for buying a computer using a dictionary

available_parts = {"1" : "computer",
                   "2" : "monitor",
                   "3" : "keyboard",
                   "4" : "mouse",
                   "5" : "hdmi cable"
                   }
current_choice = None # create this variable and initialise it
print(available_parts) # printing a dictionary like this prints the keys and values
computer_parts = [] # empty list, its very common to cmobine lists and dictionaries
while current_choice != "0":
    if current_choice in available_parts:  # when you use the in keyword in a dictionary, we're only checking the keys
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            print("removing {}".format(chosen_part))
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part} ") # f string, more compact than .format method
            computer_parts.append(chosen_part)
    else:
        print("Not in the menu, please select:")
      #  for i in available_parts:
       #     print(i, " : ", available_parts[i])
        # its more efficient to use the .items() function
        for key, value in available_parts.items():
            print(key, ":", value)

    current_choice = input("Whats your choice? ")
