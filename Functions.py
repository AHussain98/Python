import colorama

# a function that is bound to a class is called a method
# python function definitions are defined by the keyword def

def multiply(x=7, y=9):  # function with two parameters, 7 and 9 are default values
   # we don't put spaces after and before the equals sign when adding default values to our parameters
    result = x * y
    return result  # return keyword just like c++


# result only exists inside multiply()

print(multiply(10, 20))  # call the function
# parenthesis are required even if there are no parameters
# variables that are defined in the function are not accessible outside of that function
# functions can use and return variables that are declared globally

# when a function is called, execution jumps to the function body wherever it is defined nd executes it
# execution then returns to the function caller, with any returned variables

answer = multiply(2, 3)  # store the returned value in the answer variable
print(answer)

print(multiply())  # using default values

# python arguments are passed by assignment, similar to passing by reference when passing a mutable object for
# immutable objects, this is similar to passing by value When you pass function arguments by reference,
# those arguments are only references to existing values. In contrast, when you pass arguments by value,
# those arguments become independent copies of the original values. Python utilizes a system, which is known as “Call
# by Object Reference” or “Call by assignment”. In the event that you pass arguments like whole numbers, strings or
# tuples to a function, the passing is like call-by-value because you can not change the value of the immutable
# objects being passed to the function. Whereas passing mutable objects can be considered as call by reference
# because when their values are changed inside the function, then it will also be reflected outside the function. we
# can get around the above rules by taking advantages of assignments with the code, and assigning the return values
# of functions to variables when we call functions
test_string = "HanNaH"


def is_palindrome(test):
    if test.casefold() == test.casefold()[::-1]:
        print("This is a palindrome")
    else:
        print("Not a palindrome")


is_palindrome(test_string)
is_palindrome("Asad")

# of course, we can call functions within fucntions like in c++
# all python functions have a return value, either explicit or implicit
# pass keyword is used when we dont want code to do anything for now, but still to e interpreted as syntatically correct
# we can use return without passing in an object to be returned to just end the function

prompt = "Please enter an even number"


def get_even_int(prompt):
    """
    docstrings go inside the function in python, just before the code
    they are an attribute of the function object

    """
    while True:
        temp = int(input(prompt))  # remember python input is string by default
        if temp % 2 == 0:
            print("Correct")
            return  # without this, the while loop would continue indefinitely
        else:
            raise ValueError("{} is not an even integer".format(temp))  # raise keyword used to throw exceptions
            #  print("Try again")


# get_even_int(prompt)

# functions that do not explicitly return anything return None

# we can force functions to crash under specific circumstances by raising an exception

# there are also keyword arguments we can pass in, so we can explicitly define what a varialbe should be in the function
print(multiply(y=27))  # y is passed in as a keyword argument


# we typically pass in paratemers positionally, but we can also use default or keywords like the above

# lets try creating a function to return the fibonacci number of a value passed in

def fibo(n: int = 5) -> int: # annotate the function to show it accepts an integer and returns an integer
    # so the default value of the fibo function is 5 and its function annotation shows it should be passed an int and returns an int
    # adding default values within a function annotation requires us to put spaces before and after the equals sign
    # remember that when we just want default values, we do not put spaces before or after the quals sign
    """
    return the nth fibonacci number for positive n
    :param n:
    :return: The fibonacci number
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    fib = [0, 1]  # a list with the first two numbers of the fibonacci sequence
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[-1]  # return the last element
# function annotations make it clearer what kind of values your functions can accept and what they return

print(fibo(5))
print(fibo(15))
CYAN = '\u001b[36m'


colorama.init()
print(CYAN, "this is in cyan")
print("and so is this")
colorama.deinit()


