# lambda expressions are expressions that create an anonymous function
# we can use these like we do in C++, to modify the behaviour of built in or library functions

countries = ['Argentina', 'Chile', 'Zanzibar', 'Brazil', 'Uruguay', 'Fiji']

# a lambda created an anonymous function, if you were then going to give it a name by binding a variable to it, then there's no point using a lambda
# when you define a regular fucntion, the function has a name
# functions created via lambdas do not have a name
# a lambda is an expression, which means we can use it anywhere that an expression can appear.
# a lambda expression evaluates to a fucntion, and that function is then used as the value of the expression
# lambdas can only contain a single expression. a normal function can contain many lines of code and many code blocks, a lambda cannot
# the function created by the lambda expression returns the result of evaluating the expression contained in the lambda expression

#  a lambda expression starts with the word lambda
#  then a comma seperated list of parameters
#  then a colon
#  the lambda expression then follows, this will be the returned value

#  we can also use conditional expressions in lambda functions
# remember that conditional expressions in python must have an else clause
# c++ lets us do the same thing with the ternary operator ?

age = 25
message = "you are old enough to vote" if age > 18 else "nope!"  # conditional
print(message)

# The eval() method parses the expression passed to this method and runs python expression (code) within the program.

x = 1
print(eval('x + 1'))  # returns 2

#  In Python, functions behave like any other object, such as an int or a list.
#  That means that you can use functions as arguments to other functions, store functions as dictionary values, or return a function from another function.

# *args allows a function to take a variable number of arguments
# args is a tuple, *args allows us to unpack the tuple

def average(*args):
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)

print(average(1,2,3,4,5))   # these input params are treated as a tuple

# if anything is to follow *args, it has to be set of named keyword parameters

# there is also the **kwarg param, this is keyword parameters
# * unpacks a tuple or a list
# ** unpacks a dictionary in the same way

def print_backwards(*args, **kwargs):  # variable number of standard args and variable number of keyword args
    print(kwargs)
    for word in args[::-1]:
        print(word, **kwargs)

print_backwards("hello", 'I\'m', 'sid', end=' ')  # here end is our kwarg
