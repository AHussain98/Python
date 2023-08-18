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
