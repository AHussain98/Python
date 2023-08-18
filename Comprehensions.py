from collections import namedtuple

numbers = [1,2,3,4,5,6]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

squares_comp = [num ** 2 for num in numbers]  # this is a list comprehension, produces a list
# does the same thing as the above but is more concise
set_comp = {num ** 2 for num in numbers}  # this is a set comprehension, produces a set
print(squares_comp)
print(set_comp)

#  comprehensions can be comprised of an expression and then an iteration
#  list comprehensions produce a list by evaluating each item in the iterable
#  we can create these by iterating over a list, string, range, or any other iterable
#  List comprehensions are often faster than loops because they use a more optimized internal mechanism for iterating over the collection.
#  Additionally, list comprehensions allow you to perform transformations and filtering in a single statement, which can lead to more efficient code.

text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)
words = [words.upper() for words in text.split(' ')]  # do the same thing to a list of strings made up of the text variable
print(words)
words = (words.upper() for words in text.split(' '))  # this is not a list comprehension, rather it is a generator expression

#  List comprehensions return the entire list, and the generator expression returns only the generator object.
#  The values will be the same as those in the list, but they will be accessed one at a time by using the next() function.
#  This is what makes list comprehensions faster than generator expressions

# number = int(input("input the number you want squared: "))
# index_pos = numbers.index(number)
# print(squares[index_pos])

#  you wont replace the value of variables you use in a list comprehension if a variable of the same name exists
#  this is unlike with a for loop

#  its also very common to have an if clause within a comprehension
evens = [num for num in numbers if num % 2 == 0]  # now we have a list of evens
# this is an expression, followed by an iterable, and then a condition
# you can actually chain the conditions together by using the and keyword
evens_more = [num for num in numbers if num % 2 == 0 and num % 3 == 0] # chained condition
# you cant have an else clause in a comprehension
# we only have a filter

print(evens)
print(evens_more)

# there also exist conditional expressions
x = 12
expression = "Twelve" if x == 12 else "Unknown"  # this is a conditional expression
# there must be an else as otherwise if the condition was false, python wouldn't know what to do
print(expression)

# if you're going to iterate over a list and will not use it again, consider using a generator expression instead

# you can also nest comprehensions
burgers = ['beef', 'chicken']
toppings = ['onion', 'lettuce', 'cheese', 'chilli sauce']

for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:  # nested list, a comprehension that iterates over each of the burgers for all of the toppings
    print(nested_meals)

for nested_meals in [(burger, topping) for topping in toppings for burger in burgers]:  # not nested, all burgers with all toppings
    print(nested_meals)

# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
map_capitals = list(map(str.upper, text.split(' ')))  # remember that when you pass a function as an argument, you don't include the parenthesis, so it's just upper here
# when you use parenthesis, you pass the result of calling the function, but we want to pass the function itself
# passing the name of the function without parenthesis is called passing a reference to the function
print(map_capitals)  # str.upper called on every item in text.split(), and we've turned this into a list
# comprehensions are preferred to maps as they're easier to read, and faster in some cases

# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
# filters are again slower than comprehensions due to overhead caused by function calls

# reduce() takes a function and a sequence and reduces the sequence to a single value by repeatedly calling the function
# this is in the functools module

# the timeit module lets us test how long certain functions take to execute by passing a reference to the function and a number of times to execute to the timeit object

# every comprehension can be rewritten as a loop, but the reverse is not true
# you can't replace the reduce function with a comprehension, for example

# any and all are functions that take in an iterable and return true or false depending on the truthyness of the values in the iterable

entries = [1,2,3,4,5]
entries_with_zero = [0,1,2,3,4,5]
print(all(entries))  # returns true
print(all(entries_with_zero))  # false, as there's a zero which evaluates as false
print(any(entries_with_zero))  # will be true

# empty data structres and types set to 0 will also be evaluated as false, e.g. empty string, empty list, set etc...
# all will return true with an empty object however, so be wary of that
# you can combine any and all with comprehensions, so have comprehensions within the any/all functions

print(any(num for num in entries if num % 2 == 0))  # returns true as some are even

# you can also create named tuples, which are a subclass of tuples used to create tuples with a name as a skeleton
Plant = namedtuple('Plant', ['name', 'type', 'origin'])     # so the tuple is called Plant, and the returned object we get is the first field, which is Plant
andromeda = Plant('andromeda', 'pretty', 'Europe')  # a created named tuple
japanese_knotweed = Plant('japanese_knotweed', 'not good', 'Japan')

print(japanese_knotweed.type)  # now we don't need to remember the index for particular fields, we can refer to them by name

print(type(andromeda))  # Plant type
