import sys

# lets find out how much memory objects take up in python
big_range = range(10000)
print("big_range is {} bytes ".format(sys.getsizeof(big_range)))



# there's a huge difference in the amount of memory thats used to store the same set of numbers
# both the range and list are iterators
# big_range is a special type of iterator called a generator
# we can create a generator object via a function:


def my_range(n: int):
    print("my range starts")
    start = 0
    while start < n:
        print(f"start is currently {start}")
        yield start  # The yield statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value.
        start += 1

big_range = my_range(5)  # nothing is printed at this stage, the function is not executed at this point
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
# when we use yield, the function returns the yielded value and then goes into a suspended state, keeping track of its exxecution position and variable values
# when it gets called again, it repeats the process
# a generator works like an iterator
