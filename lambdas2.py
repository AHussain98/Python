# define a function that increments the argument by 10
def increment_normal(x):
    return x + 10

# lets apply a lambda expression
increment_lambda = lambda x: x + 10 #  x here is the bound variable
# the lambda expression returns the value in the body of the expression

print(increment_lambda(50))
# sometimes it is convieninet to use lambda expressions
# they allow a fucntion to be created and passed around in one line of code
# simply a special syntax for making fucntions
# they only have one statement and they return the result automatically
# we can provide lambdas as a parameter of another function

# we can define a lambda with multiple parameters
addition = lambda x,y : x + y

print(addition(10,20))
# we can again create lambda functions with default values, or assign values during the function call to change their positions in the caller
# we can also use *args for multiple arguments and **kwargs for multiple keyword arguments

lambda_func = lambda **kwargs : sum(kwargs.values())
print(lambda_func(one=1,two=2,three=3))

# lambda functions are also known as anonymous functions
# lambda functions are still objects in python like regular functions but the interpreter knows nothing about them, so a traceback for an exception in a lambda function will show lambda

# standard functions cannot be called immediately, they need to be defined first
# lambda expressions can be called immediately
print((lambda x: x *10)(10))  # lambda expression invoked immediately

# passing lambdas into a function

def int_mulitply(x):
    return lambda c: x * c
saved_num = int_mulitply(5)
print(saved_num(10))  # prints 50

# filter fucntion is used to select some particular elements from a given sequence of items, we can use lambdas to help us do this
nums = [1,2,3,4,5]
evens = list(filter(lambda x: x % 2 == 0, nums))  # filter for the elements where this lambda is true
print(evens)

# map applies the passed operation to every single element in the sequence






