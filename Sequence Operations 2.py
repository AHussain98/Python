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

