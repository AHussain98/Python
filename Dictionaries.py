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

# there are restrictions on what you can use a s akey, but values can be any python object
pantry = {"chicken" : 500, "chillis" : 10, "paprika" : 5, "coriander" : 20, "salt" : 5}
recipes = {"spiced chicken": ["chicken", 'chillis','paprika','coriander','salt','rice']}

#print({str(index + 1): meal for index,meal in enumerate(recipes)})  # this is a dictionary comprehension, smarter way to do the below
# lets create a dictionary to show the meals we can cook
display_dict = {}
for index,value in enumerate(recipes): # enumerates can be used with any iterable, such as dictionaries
    print(index + 1, value) # with a dictionary, enumerate generates an index for each value in the dictionary
    display_dict[str(index+1)] = value  # stringify the index and make that the key for each recipe
while True:
    print("Please choose your recipe:")
    for key, value in display_dict.items():
        print(key, " : ",value)
    choice = input(": ")
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"you have selected {selected_item}")
        print("checking ingredients")
        ingredients = recipes[selected_item]
        print(ingredients)
        # lets check these iteams are available in the pantry
        # for item, required_quantity in ingredients.items():
        #     quantity_in_pantry = pantry.get(item,0) # get function returns the item you pass into it, else it returns the default value you pass as the second parameter
        #     if required_quantity <= quantity_in_pantry:
        #         print(f" {item} is available")
        #     else:
        #         quantity_to_buy = required_quantity = quantity_in_pantry
        #         print(f" {item} is not available, you need {quantity_to_buy} more")
print(vehicles.items())
print(vehicles.get("A7")) # returns the value for a specific key if it exists
print(vehicles.get("clio","Nope")) # or the default value you pass as the second parameter if it doesnt
vehicles.setdefault("Clio", "Back again!") # set default returns the value of a key if the key exists, if not then it creates the pair and assigns the default value you pass in
print(vehicles.get("Clio"))
# the difference is that setdefulat will actually create the key value pair in the dictionary, whereas get only
# checks and returns a value

# dictionary keys must be hashable values
# mutable types may not be used as keys, you can use an int or string or tuple as a key

d = {0 : "Zero",
     1 : "One",
     2 : "Two",
     3 : "Three"
     }

# the python dictionary type is called dict
# dict is also the dictionary class

new_dict = dict.fromkeys(d,0) # the keys for this new dictionary come from the iterable called d which we passed to
# the dict object with the fromkeys() method, we have made all the values 0
print(new_dict)
# we can also print just the keys, or just the values
print(d.keys())
# remember that an iterable is an object capable of returning its members one at a time, e.g. when running through a
# for loop. Examples of iterables include all sequence types (such as list, str, and tuple) Also some non-sequence
# types like dict, file objects, and objects of any classes you define with an __iter__() method or with a
# __getitem__() method that implements sequence semantics are iterables.

# remember that dictionary keys are unique, the same dictionary key cannot appear more than once in a dictionary
b = {4 : "Four",
     5 : "Five",
     6 : "Six"
     }
d.update(b) # update one dictionary to include the key/value pairs from the other one
# this will also update any old keys with new values if we have changed them
print(d)
# the objects returned by dict.keys(), values() and items() are view objects, they provide a dynamic view on
# the dictionaries entries. When the dictionary changes, these views also change
d[10] = "Ten"
v = d.values()
print(v)
print("Four" in v) # checking if a value exists in the dictionary by using the value view

# a smart way to loop through a dictionary
for key, value in d.items():
    print(f"{key} is mapped to {value}")
# the above can also be useful when we're looking for keys or values, as we don#t need to make copies of the keys or values
# which would be inefficient for large dictionaries
