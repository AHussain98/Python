# using enumerate is more efficient than using index lookups
# much more efficient to delete via slicing at teh start and end rather than deleting via index
# Lists are mutable, unlike strings, which is another sequence. The oontents of a list can be changed without creating references to the same object
# append() is a method that can only be used with a mutable sequence type
# we can nest lists
even = [2,4,6,8]
odd = [1,3,5,7,9]
numbers = [odd,even] # nested list
print(numbers)

# we can access these in a for loop
for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)

menu = [
        ["egg", "hash brown"],
        ["egg"],
        ["egg","muffin","hash brown"],
        ["cheese", "muffin"],
        ["muffin"],
        ["hash brown"]
        ]
for meal in menu:
    if "hash brown" not in meal:
        print(meal)

# now for each list in menu, remove the egg
# we can do this by working backwards in a nested loop

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "egg":
            del meal[index]
    print(meal)

# print function has some built in signatures we can make use of
# we can print multiple objects at once
name = "Asad"
surname = "Hussain"
print(name,surname)
# we can change the seperator
print(name,surname, sep=", ")
# end= allows us to change the normal newline we get after a print statement

# the join method can be used with any iterable
flowers = ["daffofil", "sunflower", "tiger lily", "iris"]
for flower in flowers:

    print(flowers)

    # the join method joins all items in the iterable, it uses the string you call it on as the seperator
seperator = " | "
output = seperator.join(flowers)
print(output) # each string in flowers is piped
# join is a method of the str class
# all the items in the iterable must be strings if e wish to join them

# split() string method can be used to split out a string and returns a list
panagram = "the quick brown fox jumps over the lazy dog"
words = panagram.split()
print(words) # split the string into a list of strings
# split splits the string on whitespaces by default

numbers2 = "9,122,32,5,766"
numbers2_list = numbers2.split(',') # split on commas
print(numbers2_list)

for index,num in enumerate(numbers2_list):
      numbers2_list[index] = int(num)  # converted the strings to ints
# enumerate is faster when you want to repeatedly access the iterable items at their index
# if you just want a list of indices, it is faster to use range(len())
print(type(numbers2_list[0])) # should be an int
print(numbers2_list)

# a tuple is a mathematical name for an ordered set of data
# being ordered is a requirement for a python sequence

# tuples are another sequence type, along with strings, lists and ranges
print(*range(10)) # * to unpack the sequence, range is its own built in data type
# range only works with ints

# tuples differ from lists because they are immutable, they cannot be changed after they have been created, just like strings
t = ("a","b","c") # tuples don't actually need these parethesis
print(t) # output is in parenthesis rather than square brackets, so we know its a tuple

# parenthesis must be used if we pass a tuple literal as an argument to a function
# example with print:
print(("a",12,'8')) # using parenthesis makes teh print fucntion interperet the input as a tuple

transfer = "Hussain","PSG",50000000
print(transfer) # printed in parenthesis because its a tuple
print(transfer[2]) # tuples can be referred to by index aswell

# tuples use lest memory than lists because they don't have to deal with methods that change them
# tuples are used when data must not be changed
# there is a tuple() function just like with list()





