# python is interpreted, so code is interpered and processed at run-time, there is no need for compiling the program
# python is object oriented and easy to use with all the major databases

# print function prints to the console
print("Hello")  # exit code 0 means no issues
# triple quotes for multi-line comments

# variables are reserved memory locations, these are created as soon as we assign to it
# boolean values are binary values of 1 and 0, True and False
result = 3 < 1
print(result)  # is False
print(type(result))  # class bool

name = 'Asad'  # string created, string are one dimensional arrays
# there are no char data types in python, chars are strings with a single letter in python
char = 'A'  # this is still a string
# we can access specific letters at particular indexes
print(name[0])  # print first char in name
# or negative index from the end
print(name[-1])  # last letter
small_name = name[1:3]  # substring including 2nd and 3rd letter
print(small_name)

# we are able to concatenate strings using the + operator
last_name = ' Hussain'
print(name + last_name)

# we cannot concatenate strings with numbers
# we can use the .format method (inbuilt for strings) to get around this however

# under the hood, python uses a 1d array to store the string as a sequence of chars
# this is why we can slice and index them
string = "Hi, this is for demonstration"
print(string[::-1])  # reversed string

# python is a general purpose language, can be used object oriented way
# python defines data types with classes
# remember that everything in python is an object
# python allows type casting

a = int(23)  # type cast to integer
print(type(a))  # class int
a = str(a)  # make a into a string
print(type(a))  # this is now a string
print(type(13.5))  # float

# arithmetic operators: +, -, *, /, ??, **, %
print(10 / 3)  # normal division, results in a float
print(10 // 3)  # integer division, results in an int

# comparison operators <, >, ==

# assignment operator =, +=, -=, *=, /=
# logical operators, and, or, not

# you can use else with loops as well
for letter in name:
    print(letter, end='')
else:  # this operation is run after finishing the for loop
    print(" all gone!")  # this is printed at the end

# remember that python has the enumerate function for dealing with indices
for value in enumerate(range(5)):  # we can then unpack this tuple
    print(value)

animals = ['cat', 'dog', 'rabbit']
for index, animal in enumerate(animals):
    print(str(index) + ' ' + animal)  # index is integer by default so cast to string to concatenate

# break keyword breaks a loop and returns control to after loop
# continue skips the current iteration of loop at the point the keyword is called

# in python, a function cannot be empty, if we need to keep the body of a function empty, we can use the pass keyword

# **kwargs works as a dictionary, keys are the dictionary, values are the passed args

def show_names(*args, **kwargs):  # args as a tuple
    for arg in args:
        print(arg)  # this is smarter than using indexing to access the elements, as we don't know at compile time how many elements there are
    print(kwargs["name"])  # get the value from the key called age
    print(kwargs["age"])

show_names("Asad", "Hussain", 25, name="Ahus", age=25)

# remember we can return values

def add(num1, num2):
    return (num1 + num2)

print(add(10,5))

# you can actually return multiple values in a tuple

def ret(num):
    return num, 5  # return a tuple

a,b = ret(10)  # unpack the tuple
print(a,b)

#  return sends a specific value back to its caller and ends the function
#  yield produces a sequence of values and can resume execution

def producer():
    for num in range(0,12):
        if num % 2 == 0:
            yield num

print(producer())  # execution stops when we hit the yield statement

for num in producer():  # using yield, we can iterate through a given function result
    print(num)


prod = producer()  # assign the generator to an object
print(next(prod))

# local variables cannot be used outside the scope of the given function
# global variables are defined in the global namespace, these can be used anywhere in the program

# using range() does not return a generator, it is an immutable object
# Iterating over such a generator object is pretty slow on CPython. This is mainly due to the increment of pure-Python integers and their comparisons for each loop iteration.
# Pure-Python integers are quite expensive because they can be bigger than native integers (CPython needs to consider the case where the range can be very large although it never happens in practice).
# Managing pure-Python objects also introduce an additional overhead too (allocation, deallocation, reference counting, indirections, etc.)
# The advantage of the range type over a regular list or tuple is that a range object will always take the same (small) amount of memory,
# no matter the size of the range it represents (as it only stores the start, stop and step values, calculating individual items and subranges as needed).

# using pow() is far more efficient that using double asterisk

# we can tell python we are modifying the global variable within the local scope by using the global keyword

# in other programming languages, the main function is the starting point of the application
# but python is an interpereted language, there is no entry point, the script is being executed line by line
# there is no entry poing
# there are implicit variables such as __name__
# the __name__ is a special built-in variable which evaluates to the name of the current module
# however if a module is being run directly then this __name__ gets the value __main__

# the code we see under the __name__ == '__main__' condition only executes if that module is run directly
# if we import from another module then this code in that module will not run
