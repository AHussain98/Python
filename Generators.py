import sys
import os

# lets find out how much memory objects take up in python
big_range = range(10000)
print("big_range is {} bytes ".format(sys.getsizeof(big_range)))



# there's a huge difference in the amount of memory thats used to store the same set of numbers
# both the range and list are iterators
# big_range is a special type of iterator called a generator
# Generator functions (available since 2.3) are coded as normal def statements, but use yield statements to return results one at a time, suspending and resuming their state between each.
# we can create a generator object via a function:


def my_range(n: int):
    print("my range starts")
    start = 0
    while start < n:
        print(f"start is currently {start}")
        yield start  # The yield statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value.
        start += 1


big_range = my_range(5)   # nothing is printed at this stage, the function is not executed at this point
print(next(big_range))  # prints zero, as that is what is the next value immediately after the iterators creation

print("big_range is {} bytes ".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []
for val in big_range:  # the function is actually called here, and runs for each value yielded by the generator
    # remember that the generator works like an iterator
    big_list.append(val)

print("big list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range) # prints a generator object
print(big_list)

# a normal function finishes after returning a result
# the my_range object (when used as a generator and using the yield keyword) actually takes up more memory than if it was just a normal function with a return statement
# when we use yield, the function returns the yielded value and then goes into a suspended state, keeping track of its execution position and variable values
# when it gets called again, it repeats the process
# a generator works like an iterator

# you can use the next function to return the value that will be yielded next by the generator
# a for loop is just calling next for us
# but we cannot use a generator object in a for loop if we have assigned to it, we cna use the generator function directly

for i in big_range:  # doesn't do anything, we cant use the variable assigned to a generator function in a for loop
    print(i)
for i in my_range(5):  # this executes as we would expect
    print(i)

# however we can also use ranges in for loops
for i in range(5):  # works, the range class behaves like an iterable, its reset every time its used,
    # which isnt the case when we use a variable assigned to the generator function
    print(i)

# easy way to swap values between variables by unpacking a tuple
a = 5
b = 10
a, b = b, a  # rhs gets evaluated first in an assignment, so this is a, b = 10, 5
print(a,b)  # swapped

# create a fibonacci function using a generator

def fibo():
    current, previous = 0, 1
    while True:  # infinite generator
        yield current
        current, previous = current + previous, current

fib = fibo()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# for i in fib:
#     print(i)

# os.walk() is a generator, it doesnt build up a huge list of files and directories, it just returns them as needed
root = "music"

for path, directories, files in os.walk(root, topdown=True):
    print(path)
    for f in files:
        print("\t{}".format(f))
