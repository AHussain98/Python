import collections
import numpy
import pandas

# Python lists are ordered collections of elements and, in Python, are implemented as
# resizable arrays. An array is a basic data structure that consists of a series of contiguous
# memory locations, and each location contains a reference to a Python object.

# Lists shine in accessing, modifying, and appending elements. Accessing or modifying an
# element involves fetching the object reference from the appropriate position of the
# underlying array and has complexity O(1). Appending an element is also very fast. When
# an empty list is created, an array of fixed size is allocated and, as we insert elements, the
# slots in the array are gradually filled up. Once all the slots are occupied, the list needs to
# increase the size of its underlying array, thus triggering a memory reallocation that can take
# O(N) time. Nevertheless, those memory allocations are infrequent, and the time complexity
# for the append operation is referred to as amortized O(1) time.

# The list operations that may have efficiency problems are those that add or
# remove elements at the beginning (or somewhere in the middle) of the list. When an item is
# inserted, or removed, from the beginning of a list, all the subsequent elements of the array
# need to be shifted by a position, thus taking O(N) time.

dq = collections.deque()
dq.append(1)  # append and appendleft, pop and popleft is O(1)
dq.appendleft(2)

#  Python provides a data structure with those
# properties in the collections.deque class. The word deque stands for double-ended
# queue because this data structure is designed to efficiently put and remove elements at the
# beginning and at the end of the collection, as it is in the case of queues. In Python, deques
# are implemented as doubly-linked lists.
# accessing an element in the middle of a deque is O(N)! Dont use deque over list in most cases

# Searching for an item in a list is generally a O(N) operation and is performed using the
# list.index method. A simple way to speed up searches in lists is to keep the array sorted
# and perform a binary search using the bisect module.
# The bisect module allows fast searches on sorted arrays. The bisect.bisect function
# can be used on a sorted list to find the index to place an element while maintaining the
# array in sorted order. In the following example, we can see that if we want to insert the 3
# element in the array while keeping collection in sorted order, we should put 3 in the
# third position (which corresponds to index 2):
#  insert bisect
#  collection = [1, 2, 4, 5, 6]
#  bisect.bisect(collection, 3)
#  # Result: 2

# This function uses the binary search algorithm that has O(log(N)) running time. Such a
# running time is exceptionally fast, and basically means that your running time will increase
# by a constant amount every time you double your input size.

# Dictionaries are implemented as hash maps and are very good at element insertion,
# deletion, and access; all these operations have an average O(1) time complexity
# dictionaries are capable of maintaining their elements by order of insertion

# A hash map is a data structure that associates a set of key-value pairs. The principle behind
# hash maps is to assign a specific index to each key so that its associated value can be stored
# in an array. The index can be obtained through the use of a hash function; Python
# implements hash functions for several data types. As a demonstration, the generic function
# to obtain hash codes is hash.
# In the following example, we show you how to obtain the
# hash code given the "hello" string:
#  hash("hello")
#  # Result: -1182655621190490452
#  # To restrict the number to be a certain range you can use
#  # the modulo (%) operator
#  hash("hello") % 10
#  # Result: 8
# Hash maps can be tricky to implement because they need to handle collisions that happen
# when two different objects have the same hash code. However, all the complexity is
# elegantly hidden behind the implementation and the default collision resolution works well
# in most real-world scenarios.
# Access, insertion, and removal of an item in a dictionary scales as O(1) with the size of the
# dictionary. However, note that the computation of the hash function still needs to happen
# and, for strings, the computation scales with the length of the string. As string keys are
# usually relatively small, this doesn't constitute a problem in practice

# Sets are unordered collections of elements, with the additional restriction that the elements
# must be unique. The main use-cases where sets are a good choice are membership tests
# (testing if an element is present in the collection) and, unsurprisingly, set operations such as
# union, difference, and intersection.
# In Python, sets are implemented using a hash-based algorithm just like dictionaries;
# therefore, the time complexities for addition, deletion, and test for membership scale as O(1)
# with the size of the collection.
# Sets contain only unique elements. An immediate use case of sets is the removal of
# duplicates from a collection, which can be accomplished by simply passing the collection
# through the set constructor, as follows:
#  # create a list that contains duplicates
#  x = list(range(1000)) + list(range(500))
#  # the set *x_unique* will contain only
#  # the unique elements in x
#  x_unique = set(x)
# The time complexity for removing duplicates is O(N), as it requires to read the input and
# put each element in the set

# priority queue (heap) exist in the  queue.PriorityQueue class that, as a bonus, is thread
# and process-safe. The PriorityQueue class can be filled up with elements using
# the PriorityQueue.put method, while PriorityQueue.get can be used to extract the
# minimum value in the collection:
#  from queue import PriorityQueue
#  queue = PriorityQueue()
#  for element in collection:
#  queue.put(element)
#  queue.get()
#  # Returns: 3
# If the maximum element is required, a simple trick is to multiply each element of the list
# by -1. In this way, the order of the elements will be inverted.

# Caching is a great technique used to improve the performance of a wide range of
# applications. The idea behind caching is to store expensive results in a temporary location,
# called cache, that can be located in memory, on-disk, or in a remote location.
# Web applications make extensive use of caching. In a web application, it often happens that
# users request a certain page at the same time. In this case, instead of recomputing the page
# for each user, the web application can compute it once and serve the user the already
# rendered page. Ideally, caching also needs a mechanism for invalidation so that if the page
# needs to be updated, we can recompute it before serving it again. Intelligent caching allows
# web applications to handle increasing number of users with less resources. Caching can also
# be done preemptively, such as the later sections of the video get buffered when watching a
# video online.
# Caching is also used to improve the performance of certain algorithms. A great example is
# computing the Fibonacci sequence. Since computing the next number in the Fibonacci
# sequence requires the previous number in the sequence, one can store and reuse previous
# results, dramatically improving the running time. Storing and reusing the results of the
# previous function calls in an application is usually termed as memoization, and is one of
# the forms of caching. Several other algorithms can take advantage of memoization to gain
# impressive performance improvements, and this programming technique is commonly
# referred to as dynamic programming.
# The benefits of caching, however, do not come for free. What we are actually doing is
# sacrificing some space to improve the speed of the application. Additionally, if the cache is
# stored in a location on the network, we may incur transfer costs and general time needed
# for communication. One should evaluate when it is convenient to use a cache and how
# much space we are willing to trade for an increase in speed.

# numpy arrays are collections of elements of the same data type
a = numpy.array([0,1,2,3])
print(a.dtype)  # 32 bit int

a2 = numpy.array([[1,2,3],[4,5,6]])  # 2d array
print(a2)
print(a2.shape) # 2,3 by default

#a2.reshape(1,6)  # change to single long array

# numpy array interface is similar to lists

for a in a2:
    for ab in a:
        print(ab)

# access specific element with comma
print(a2[(0,1)])  # we are actually indexing using a tuple!
a2[0,1] = 55  # indexing and slicing numpy arrays is very fast because unlike core python, it doesnt produce a copy
a2[0:2, 0:2] = [[10,20], [30,40]]  # change the array itself using indexing

a2.flags.writeable = False  # prevents accidental mutation of the array or any of its views

# NumPy allows you to index an array using another NumPy array made of either integer or
# Boolean values--a feature called fancy indexing.
# If you index an array (say, a) with another array of integers (say, idx), NumPy will
# interpret the integers as indexes and will return an array containing their corresponding
# values. If we index an array containing 10 elements with np.array([0, 2, 3]), we
# obtain an array of shape (3,) containing the elements at positions 0, 2, and 3. The
# following code gives us an illustration of this concept:
#  a = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
#  idx = np.array([0, 2, 3])
#  a[idx]
#  # Result:
#  # array([9, 7, 6])

# you can use normal list as index arrays, but not tuples

# Indexing in NumPy is a reasonably fast operation. Anyway, when speed is critical, you can
# use the slightly faster numpy.take and numpy.compress functions to squeeze out a little
# more performance.

# Numpy is used for fast mathematic operations
# numpy avoids stepping into the python interpreter by performing element-wise calculation using optimised C code
# Broadcasting is a clever set of rules that enables fast array calculations for arrays of similar (but not equal) shape

# Whenever you do an arithmetic operation on two arrays (like a product), if the two
# operands have the same shape, the operation will be applied in an element-wise fashion.
# For example, upon multiplying two shape (2,2) arrays, the operation will be done
# between pairs of corresponding elements, producing another (2, 2) array, as shown in the
# following code:
#  A = np.array([[1, 2], [3, 4]])
#  B = np.array([[5, 6], [7, 8]])
#  A * B
#  # Output:
#  # array([[ 5, 12],
#  # [21, 32]])

# If the shapes of the operands don't match, NumPy will attempt to match them using
# broadcasting rules. If one of the operands is a scalar (for example, a number), it will be
# applied to every element of the array, as the following code illustrates:
#  A * 2
#  # Output:
#  # array([[2, 4],
#  # [6, 8]])

# When handling complex expressions, NumPy stores intermediate results in memory. David
# M. Cooke wrote a package called numexpr, which optimizes and compiles array
# expressions on the fly. It works by optimizing the usage of the CPU cache and by taking
# advantage of multiple processors.
# Its usage is generally straightforward and is based on a single function--
# numexpr.evaluate. The function takes a string containing an array expression as its first
# argument. The syntax is basically identical to that of NumPy. For example, we can calculate
# a simple a + b * c expression in the following way:
#  a = np.random.rand(10000)
#  b = np.random.rand(10000)
#  c = np.random.rand(10000)
#  d = ne.evaluate('a + b * c')
# The numexpr package increases the performances in almost all cases, but to get a substantial
# advantage, you should use it with large arrays

# pandas is used to analyse datasets in a performant way
# pandas deals with arrays, pandas main data structure is data frames

# The main difference between a pd.Series object and an np.array is that a pd.Series
# object associates a specific key to each element of an array. Let’s see how this works in
# practice with an example.







