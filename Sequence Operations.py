even = [2,4,6,8,10]
odd = [1,3,5,7,9]

print(min(even))
print(max(odd))  # min and max functions can be used with sequences

print(len(odd)) # number of items in the sequence
# the count function tells you how many times a value appears in a sequence, lets use a string to demonstrate this
name = "Asad Hussain"
print("a appears in my name {0} times".format( name.count('a'))) # the number of times a appears in my name

# method is the same as a function, except its bound to an object
# len() is a fucntion, append() is a method

even.append("brexit")
print(even)

computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]
current_choice = '-' # declare a variable
customer_basket = []  #empty list

while current_choice != '0':  # remember that input is string by default
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        customer_basket.append(computer_parts[int(current_choice) - 1])
    else:
        print("Please select from the following choices: ")
        #for i in computer_parts:
        #    print("{0}: {1}".format(computer_parts.index(i) + 1, i)) # index method allows us to print the index that an object appears in the list
            # the above lines are not very efficent as everytime the loop runs, the list is searched for from the begenning for the index that the part appears in
            # to do this more efficiently, use the enumerate function which returns each item with its index position:
        for number, part in enumerate(computer_parts): # if a sequence contains more than one value, we can include these extra values in our for loop decleration
            print("{0} : {1}".format(number,part))
    current_choice = input()
# enumerate returns pairs of values, the first is the index position and the second is the item
print("Your basket is: {0}".format(customer_basket))

for index,char in enumerate("123456"):
    print(index,char)

# the final value when using a range() is not included
print(*range(1,10))  # only goes up to 9, * unpacks the sequence

# int() changes input into an integer
# str() changes target into a string
# input() is a string by default
