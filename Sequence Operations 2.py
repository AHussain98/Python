current_choice = '-'
computer_parts = ["mouse", "keyboard","monitor","pc","chair","mouse pad"]
customer_basket = []

# while current_choice != '0':  # remember that input is string by default
#     if current_choice in "123456":
#         print("Adding {}".format(current_choice))
#         chosen_part = computer_parts[int(current_choice) - 1]
#         if chosen_part in customer_basket:
#             # its already in, so remove it
#             customer_basket.remove(chosen_part) # list has remove method
#         else:
#             customer_basket.append(computer_parts[int(current_choice) - 1])
#         print("your current basket is: {}".format(customer_basket))
#     else:
#         print("Please select from the following choices: ")
#         for number, part in enumerate(computer_parts): # if a sequence contains more than one value, we can include these extra values in our for loop decleration
#             print("{0} : {1}".format(number,part))
#     current_choice = input()
# enumerate returns pairs of values, the first is the index position and the second is the item
# print("Your basket is: {0}".format(customer_basket))

# if you try to remove an item which isnt present in a list, you get an error

# lets move onto sorting a list
even = [2,4,6,8]
odd = [1,3,5,7,9]
even.extend(odd)  # extend adds onto the end of a list
print(even)
even.sort() # lists have a sort function
print(even)
even.reverse() # reverse function
print(even)
even.sort(reverse=True)  # this is how to sort in reverse
print(even)
# all of the above are sorting the list in place, no copies are made
print(max(even))
print(any(even))

pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram) # sorted function takes any iterable and returns a list in sorted order
print(letters)
# sorted returns a new list

numbers = [1.4,7.8,1.2,3.4,2.2]
sorted_numbers = sorted(numbers)  # this is a new list!
# unlike with a sort, using the sorted method returns a new list. sort just sorts the list in place, no new list
print(sorted_numbers)
print(numbers) # unchanged

# anywhere we use a variable, we can pass a literal
# so we can pass a literal to sorted
print(sorted("Brexit"))

# # case insensitive sort
# example = "The quick brown fox jumped over the lazy dog"
# lower_case = sorted(example, key=str.casefold) # this second argument is how we can sort without caring about caps
# # don't use the parenthesis because that will call the fucntion
# print(lower_case)
# # casefold returns a string where all the characters are lowercase
# print(example.casefold()) # lowercase
#
# names = ["Asad", "Misha", "Alayna","Idris","Mustafa","Aisha"]
# names.sort(key=str.casefold)
# print(names)
#
# empty_list = [] # creates an empty list
# # names is also a list, we created that and initialised it at once
# # you can create a list by concatenating lists
# empty_list.append( "Humaira")
# new_list = names + empty_list # this adds the values in empty_list onto the end of new_list
# print(new_list)
#
# # you can also create a list by using a function that returns one, like sorted()
# # there's also a list function which creates a list from any iterable
#
# numbers = "12345"
# digits = list(numbers) # list function, this is one way to copy a list, so digits is its own object, not just another name for the list object as would be the case if we did =
# more_numbers = list(digits)
# print(numbers is more_numbers) # is keyword can be used to check if two names refer to the same object
# print(digits)
#
# # you can also create a list using a slice
# more_numbers = numbers[:2]
# print(more_numbers is numbers) # another object, but only because we've sliced
#
# more_numbers = numbers.copy()
# print(more_numbers is numbers) # false, so we have another list

computer_parts = ["mouse", "keyboard","monitor","pc","chair","mouse pad"]
computer_parts[3] = "trackball" # we've made a change to the list via index
# this cant be done with strings because they're immutable
print(computer_parts)
computer_parts[3:] = ["Aisha"]  # replaced via slice, if you make it equal to an iterable
print(computer_parts)

# you can delete from a list using the del keyword
del computer_parts[:2]  # delete the first two entries in the list
print(computer_parts)
# you can also delete by index

numbers = [1,2,3,4,5,6,7,8,9,10] # be very careful when iterating over a list and deleting items as you do so, you could  be referring to an index which is no longer used
# to do this safely in python, lets see how to do this in a sorted list
min_value = 4 # imagine we want to remove anything below 4
stop = 0 # variable to store the index we'll stop at
for index,value in enumerate(numbers):  # use enumerate because we want indexes aswell
    if value >= min_value:
        stop = index
        break  # break out of the loop
# so its important we dont change any values within the loop itself, as we can't edit the index value in python because index is reset everytime the loop reruns
del numbers[:stop]
print(numbers)

# now imagine we want to remove the high values in the list
# we can work backwards
start = 0
max_value = 7
for index in range(len(numbers) - 1,-1,-1): # start at the end, remember that the last value diesnt get printed, so put -1 there, and we want to go backwards so make the step -1
    if numbers[index] <= max_value:
        start = index + 1
        break
del numbers[start:]  # cleaner to add one to start, we do this because the start value will also be deleted
print(numbers)

# when we remove an item from a list, all the later items are shuffled down, to fill in the gap
# this messes up the index numbers as we work forwards through the list
# iterating backwards is useful and avoids this issue, this allows the sequence to be changed without causing an issue

data = [104,101,4,105,308,200,212,323,9,45,900,102,99]
min_valid = 100
max_valid = 200

# lets try removing all invalid values by iterating backwards through the list

for i in range(len(data) - 1,-1,-1):
    # start at the end, finish at 0 and move backwards by 1 each step
    if data[i] < min_valid or data[i] > max_valid:
        del data[i]; # delete the invalid values as we come to them, starting from the end

print(data) # valid
