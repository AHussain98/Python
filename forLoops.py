#python ways to repeat a block of code: for loops, while loops, list comprehensions and generator expressions
#the set of values in the for loop comes from a sequence, or some other iterable object
#iterable object is anything that can be iterated over

# parrot = "Norwegian Blue"
# for character in parrot: #python for loops use the for and in keywords
#     print(character)
#
# number = "9,223;372:036 854,775;807"
# seperators = number[1::4] #slice the number string
#
# seperatorsMyTurn = "" #make my seperators variable an empty string, we need to create the variable first and assign it a value before we can use it
# count = 0
# for char in number:
#     if not char.isnumeric():
#        seperatorsMyTurn = seperatorsMyTurn + char  #seperatorsMyTurn[count] = char does not work in python, as strings are immutable
#        # count += 1 #python doesnt have ++ or --
#        # in python, you have to contaenate and create a new string, you cant edit a string like in c++
# print(seperatorsMyTurn)
#
# #lets try the above with user input
#
# numbers = input("Please enter a series of numbers, using any seperators you like")
# for char in numbers:
#     if not char.isnumeric():
#         seperatorsMyTurn = seperatorsMyTurn + char #this is how we do it in python
#
#     print(seperatorsMyTurn)
#
#     values = "".join(char if char not in seperatorsMyTurn else " " for char in numbers).split()
#     print(values)
#     print(sum(int(val) for val in values)) #remember to sum it, they need to be ints

# for i in range(1,20):  #range starts at 1 and then ends at 19, the last value in the range is not included
#     print("i is now {}".format(i))
# #in ranges, if you dont provide a start value, it will default at 0
# for i in range(10):
#     print(i)
# #we can also add a step value to our ranges
# for i in range(0,10,2):
#     print(i)
#
# for i in range(1,13): #nested forloops, very useful
#     for j in range(1,13):
#         print("{0} times {1} = {2}".format(i,j,i*j))
#     print("------------------------") #this line is in the outer loop but the inner loop has completed


# a list in python is an ordered sequence of values enclosed in square brackets

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item != "spam": #imagine we didnt like spam
#       print("Buy " + item)
#
# #lets try another approach using continue
#
# for item in shopping_list:
#     if item == "spam": #continue skips the current loop iteration if it is true
#         continue #continue must be indented, as it runs when the if condition is true
#     print("Buy " + item) #continue causes all remaining code in the block to be skipped, loop reruns
# #c++ also has a continue statement
#
# for item in shopping_list:
#     if item == "spam":
#         break #break keyword breaks the loop entirely
#     print("Buy " + item)

item_to_find = "siuuuu"
found_at = None #this variable is initalised as None, this si roughly equivalent to NULL in c++
#Now lets loop over the index positions of the loop rather than the list itself
#we have to initialise found_at, otherwise if the item to find wasnt in the list, wed get an error, as were trying to assign fount_at to an item that doesnt exist in the loop
#for index in range(6):
for index in range(len(shopping_list)): #len to use length of shopping list array
    if shopping_list[index] == item_to_find:
        found_at = index
        #when we find what we're searching for, there's no need for the loop to continue to run, so include a break if this condition is reached
        break #this is more efficient
if found_at is not None:
     print("Item found at index position {}".format(found_at))
else:
    print("{} is not in the loop".format(item_to_find))

#we can do the above in an even smarter way using python specific tools:

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find) #the index function returns the index of the value its passed for a sequence