# high performance programming can be thought of as the act of minimizing these operations either by reducing the overhead 
# (i.e., writing more efficient code) or by changing the way that we do these operations to make each one more meaningful (i.e., finding a more suitable algorithm).

# the bottleneck in any parallel calculation is always the smaller serial tasks that are being spread out.

#  major hurdle with utilizing multiple cores in Python is Python’s use of a global interpreter lock (GIL). The GIL makes sure that a Python process can run
# only one instruction at a time, regardless of the number of cores it is currently using. 
# This means that even though some Python code has access to multiple cores at a time, only one core is running a Python instruction at any given time. 
# While this may seem like quite a hurdle, especially if the current trend in computing is to have multiple computing units rather than having faster ones, this problem can be avoided
# by using other standard library tools, like multiprocessing (Chapter 9), technologies like numpy or numexpr, Cython, or distributed models of computing.

# The frontside bus, for example, is the connection between the RAM and the L1/L2 cache. It moves data that is ready to be transformed by the processor into the staging
# ground to get ready for calculation, and it moves finished calculations out. There are other buses, too, such as the external bus that acts as the main route from hardware
# devices (such as hard drives and networking cards) to the CPU and system memory. This external bus is generally slower than the frontside bus.
# In fact, many of the benefits of the L1/L2 cache are attributable to the faster bus. Being able to queue up data necessary for computation in large chunks on a slow bus
# (from RAM to cache) and then having it available at very fast speeds from the cache lines (from cache to CPU) enables the CPU to do more calculations without waiting such a long time

# This theme of keeping data where it is needed and moving it as little as possible is very important when it comes to optimization.
#The concept of “heavy data” refers to the time and effort required to move data around, which is something we would like to avoid.

#try to take advantage of a CPU’s ability to vectorize a calculation, or run one instruction on multiple data in one clock cycle.
# This concept of vectorization is illustrated by the following code:
import math

def check_prime(number):
    sqrt_number = math.sqrt(number)
    numbers = range(2, int(sqrt_number)+1)
    for i in range(0, len(numbers), 5):
         # the following line is not valid Python code
         result = (number / numbers[i:(i + 5)]).is_integer()
         if any(result):
             return False
    return True

# Here, we set up the processing such that the division and the checking for integers are done on a set of five values of i at a time.
#  If properly vectorized, the CPU can do this line in one step as opposed to doing a separate calculation for every i. 


# before optimising, profile first!
# By profiling first, you can quickly identify the bottlenecks that need to be solved, and then you can solve just enough of these to achieve
# the performance you need. If you avoid profiling and jump to optimization, you’ll quite likely do more work in the long run. Always be driven by the results of profiling

# Robert Kern’s line_profiler is the strongest tool for identifying the cause of CPU-bound problems in Python code. It works by profiling individual
# functions on a line-by-line basis, so you should start with cProfile and use the highlevel view to guide which functions to profile with line_profiler.

# If you haven’t thought about the complexity of Python’s dynamic machinery before,
# do think about what happens in that n += 1 operation. Python has to check that the n
# object has an __add__ function (and if it didn’t, it’d walk up any inherited classes to
# see if they provided this functionality), and then the other object (1 in this case) is
# passed in so that the __add__ function can decide how to handle the operation.
# Remember that the second argument might be a float or other object that may or
# may not be compatible. This all happens dynamically.

# Just as Robert Kern’s line_profiler package measures CPU usage, the memory_profiler module by Fabian Pedregosa and Philippe Gervais measures memory usage on a line-by-line basis. 

def fn_expressive(upper=1_000_000):
    total = 0
    for n in range(upper):
       total += n
    return total

def fn_terse(upper=1_000_000):  # this version is twice as fast!
    return sum(range(upper))

assert fn_expressive() == fn_terse(), "Expect identical results from both functions"
# Both functions calculate the sum of a range of integers. 
# A simple rule of thumb (but one you must back up using profiling!) is that more lines of bytecode will execute more slowly than fewer equivalent lines of bytecode that use built-in functions. 
# The difference between the two code blocks is striking. Inside fn_expressive(), we maintain two local variables and iterate over a list using a for statement. The for
# loop will be checking to see if a StopIteration exception has been raised on each loop. Each iteration applies the total.__add__ function, which will check the type of 
# the second variable (n) on each iteration. These checks all add a little expense. Inside fn_terse(), we call out to an optimized C list comprehension function that
# knows how to generate the final result without creating intermediate Python objects. This is much faster, although each iteration must still check for the types of the
# objects that are being added together (in Chapter 4, we look at ways of fixing the type so we don’t need to check it on each iteration).
# As noted previously, you must profile your code—if you just rely on this heuristic, you will inevitably write slower code at some point. It is definitely worth learning
# whether a shorter and still readable way to solve your problem is built into Python. If so, it is more likely to be easily readable by another programmer, and it will probably run faster

import bisect
# python has two types of arrays, lists and tuples
# lists are dynamic and tuples are static
# lists can store any type of data because they store references to objects rather than objects themselves, as opposed to numpy arrays
# arrays store elements in order, thereby accessing an element by index is O(1)

arr = list(range(100))
print(arr[50])  # O(1)

# linear search in an array is O(N)
# binary search is log(N), but requires a sorted list

# bisect provides very efficient searching
i = bisect.bisect_left(arr,5)  # returns the first element larger than the one passed in
print(i)

# lists are dynamic arrays, they are mutable and allow for resizing
# tuples are static arrays, they are immutable and cannot be changed after creation
# tuples are cached by the Python runtime, which means we don't need to allocate memory to reserve memory every time we use one

# tuples are for
# describing multiple properties of one unchanging thing, and lists can be used to store
# collections of data about completely disparate objects. For example, the parts of a
# telephone number are perfect for a tuple: they won’t change, and if they do, they rep‐
# resent a new object or a different phone number. Similarly, the coefficients of a poly‐
# nomial fit a tuple, since different coefficients represent a different polynomial. On the
# other hand, the names of the people currently reading this book are better suited for a
# list: the data is constantly changing both in content and in size but is still always rep‐
# resenting the same idea.


# lists and tuples can store mixed types, but it removes overhead to only use one data type
# generic code is much slower than code specifically designed to solve a particular problem

# In addition, the immutability of a tuple as opposed to a list, which can be resized and
# changed, makes it a lightweight data structure. This means that there isn’t much
# overhead in memory when storing tuples, and operations with them are quite
# straightforward. With lists, as you will learn, their mutability comes at the price of
# extra memory needed to store them and extra computations needed when using
# them.

# changing list elements is O(1) because we can find the data immediately via index

#  When a list of size N is first appended to, Python must create a
# new list that is big enough to hold the original N items in addition to the extra one
# that is being appended. However, instead of allocating N + 1 items, M items are
# actually allocated, where M > N, in order to provide extra headroom for future
# appends. Then the data from the old list is copied to the new list, and the old list is
# destroyed.

# appending to the end of a list is O(1)
# when the list is full and copied over, this operation is O(N)

# adding two tuples is always O(N) because  we must allo‐
# cate and copy the tuple every time something is added to it, as opposed to only when
# our extra headroom ran out for lists. As a result of this, there is no in-place appendlike operation; adding two tuples always returns a new tuple that is in a new location
# in memory

# Furthermore, even if we create a list without append (and thus we don’t have the extra
#  headroom introduced by an append operation), it will still be larger in memory than a
# tuple with the same data. This is because lists have to keep track of more information
# about their current state in order to efficiently resize. While this extra information is
# quite small (the equivalent of one extra element), it can add up if several million lists
# are in use.
# Another benefit of the static nature of tuples is something Python does in the
#  background: resource caching. Python is garbage collected, which means that when a
# variable isn’t used anymore, Python frees the memory used by that variable, giving it
# back to the operating system for use in other applications (or for other variables). For
#  tuples of sizes 1–20, however, when they are no longer in use, the space isn’t immedi‐
# ately given back to the system: up to 20,000 of each size are saved for future use. This
# means that when a new tuple of that size is needed in the future, we don’t need to
# communicate with the operating system to find a region in memory to put the data
# into, since we have a reserve of free memory already. However, this also means that
#  the Python process will have some extra memory overhead.
# While this may seem like a small benefit, it is one of the fantastic things about tuples:
# they can be created easily and quickly since they can avoid communications with the
# operating system, which can cost your program quite a bit of time.

# sets and dictionaries are ideal when data has no intrinsic order but does have a unique hashable object that can ve used to reference it

# dictionaries and sets give O(1) lookup if we know the key or index and have O(1) insertion time

# Also, although the complexity for insertions/lookups is
# O(1), the actual speed depends greatly on the hashing function that is in use. If the
# hash function is slow to evaluate, any operations on dictionaries or sets will be simi‐
# larly slow

# remember that a set is just a collection of unique keys
# again, adding an item to the set is O(1), if you try to add an item that already exists in the set it just won't be added

# Dictionaries and sets use hash tables to achieve their O(1) lookups and insertions.
# This efficiency is the result of a very clever usage of a hash function to turn an arbi‐
# trary key (i.e., a string or object) into an index for a list. The hash function and list
# can later be used to determine where any particular piece of data is right away,
# without a search. By turning the data’s key into something that can be used like a list
# index, we can get the same performance as with a list. In addition, instead of having
# to refer to data by a numerical index, which itself implies some ordering to the data,
# we can refer to it by this arbitrary key

# As more items are inserted into the hash table, the table itself must be resized to
# accommodate them. It can be shown that a table that is no more than two-thirds full
# will have optimal space savings while still having a good bound on the number of col‐
# lisions to expect. Thus, when a table reaches this critical point, it is grown. To do this,
# a larger table is allocated (i.e., more buckets in memory are reserved), the mask is
# adjusted to fit the new table, and all elements of the old table are reinserted into the
# new one. This requires recomputing indices, since the changed mask will change the
# resulting index. As a result, resizing large hash tables can be quite expensive! How‐
# ever, since we do this resizing operation only when the table is too small, as opposed
# to doing it on every insert, the amortized cost of an insert is still O(1).
#
# By default, the smallest size of a dictionary or set is 8 (that is, if you are storing only
# three values, Python will still allocate eight elements), and it will resize by 3× if the
# How Do Dictionaries and Sets Work? | 87
# 6 More information about this can be found at https://oreil.ly/g4I5-.
# dictionary is more than two-thirds full. So once the sixth item is being inserted into
# the originally empty dictionary, it will be resized to hold 18 elements. At this point,
# once the 13th element is inserted into the object, it will be resized to 39, then 81, and
# so on, always increasing the size by 3×

# Objects in Python are generally hashable, since they already have built-in __hash__
# and __cmp__ functions associated with them. For numerical types (int and float),
# the hash is based simply on the bit value of the number they represent. Tuples and
# strings have a hash value that is based on their contents. Lists, on the other hand, do
# not support hashing because their values can change. Since a list’s values can change,
# so could the hash that represents the list, which would change the relative placement
# of that key in the hash table.6
# User-defined classes also have default hash and comparison functions. The default
# __hash__ function simply returns the object’s placement in memory as given by the
# built-in id function. Similarly, the __cmp__ operator compares the numerical value of
# the object’s placement in memory.

# Doing a lookup on a dictionary is fast; however, doing it unnecessarily will slow
# down your code, just as any extraneous lines will. One area where this surfaces is in
# Python’s namespace management, which heavily uses dictionaries to do its lookups.
# Whenever a variable, function, or module is invoked in Python, there is a hierarchy
# that determines where it looks for these objects. First, Python looks inside the
# locals() array, which has entries for all local variables. Python works hard to make
# local variable lookups fast, and this is the only part of the chain that doesn’t require a
# dictionary lookup. If it doesn’t exist there, the globals() dictionary is searched.
# Finally, if the object isn’t found there, the __builtin__ object is searched. It is impor‐
# tant to note that while locals() and globals() are explicitly dictionaries and __buil
# tin__ is technically a module object, when searching __builtin__ for a given
# property, we are just doing a dictionary lookup inside its locals() map (this is the
# case for all module objects and class objects!).

# finding local functions is always fact for this reason

def fibonacci_list(num_items):
     numbers = []
     a, b = 0, 1
     while len(numbers) < num_items:
         numbers.append(a)
         a, b = b, a+b
         return numbers

def fibonacci_gen(num_items):
     a, b = 0, 1
     while num_items:
         yield a
         a, b = b, a+b
         num_items -= 1

# This function will yield many values instead of returning one value. This turns
# this regular-looking function into a generator that can be polled repeatedly for
# the next available value.
# The first thing to note is that the fibonacci_list implementation must create and
# store the list of all the relevant Fibonacci numbers. So if we want to have 10,000 num‐
# bers of the sequence, the function will do 10,000 appends to the numbers list (which,
# as we discussed in Chapter 3, has overhead associated with it) and then return it.
# On the other hand, the generator is able to “return” many values. Every time the code
# gets to the yield, the function emits its value, and when another value is requested,
# the function resumes running (maintaining its previous state) and emits the new
# value. When the function reaches its end, a StopIteration exception is thrown, indi‐
# cating that the given generator has no more values. As a result, even though both
# functions must, in the end, do the same number of calculations, the fibonacci_list
# version of the preceding loop uses 10,000× more memory (or num_items times more memory).

# In Python, for loops require that the
# object we are looping over supports iteration. This means that we must be able to cre‐
# ate an iterator out of the object we want to loop over. To create an iterator from
# almost any object, we can use Python’s built-in iter function. This function, for lists,
# tuples, dictionaries, and sets, returns an iterator over the items or keys in the object.
# For more complex objects, iter returns the result of the __iter__ property of the
# object.

# itertools module allows us to chain together multiple generators, add conditions to them and make finite generators

# The array module efficiently stores primitive types like integers, floats, and charac‐
# ters, but not complex numbers or classes. It creates a contiguous block of RAM to
# hold the underlying data.

# expert python programming, chapter 3,4,5,14,15,16
