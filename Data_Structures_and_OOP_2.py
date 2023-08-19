#  algorithm running time complexity
#  O(1) -> constant running time complexity, irrespective of size of input
#  O(N) -> linear running time complexity, algorithms time complexity scales with size of input
#  O(log N) -> logarithmic time complexity, running time scales logarithmically with the size of input (binary search)
#  log n is faster than n

#  arrays are not available in pure python
#  arrays give O(1) random access via indexing, the memory addresses are contiguous which is why indexing is available
#  more complex data structures rely heavily on arrays because of random indexing (such as stacks, queues and dictionaries

#  in python, we have lists which act as arrays, this is a one dimensional array of reference to objects
#  remember that in python, everything is an object, lists store references to other objects, not the objects themselves
#  every reference is 8 bytes in size, independent of the data type. This is why we can store any data in a python list
#  this is why storing lots of items in a list has huge memory complexity and should be avoided
#  numpy arrays are stored in a contigous block in memory, items are right next to each other, no references

#  typically when an array becomes full, we have to allocate a larger chunk of memory for a bigger array and then copy elements over
#  this resize and copy operation takes O(N) time, and we want to avoid it wherever possible
#  so if you start with a small array, you dont waste memory but introduce bottlenecks by constantly resizing
#  if you start with a huge array, you potentially waste memory but do not lose time due to resizing
#  typically to make an algorithm faster, you may need to use more memory

#  arrays also allow us to insert elements at arbitrary locations. This is O(N) time complexity because all other items must be shifted down
#  same consideration made when deleting
#  removing and inserting at the end of an array is always O(1)

my_list = [1,2,3,4,5]  # this is a list in python, arrays are used in numpy
l1 = list((1,2.0,3))  # another way to create a list

# del operator removes a given item in a list
# lists can also be sliced and iterated through in a loop

my_list.append("Asad")  # appending an item at the end of the list is O(1)

# because lists are indexed, there may be multiple items with the same value

print(my_list[-1])  # print the last item, negative indices used to access the list form the end
print(my_list)

# strings are basically one dimensional arrays in python

# we can also concatenate lists
list3 = my_list + l1  # can do the same with the extend function
my_list.extend(l1)
print(list3)

# list has some built in functions
result = my_list.copy()  # copy returns a copy of a list
result.remove("Asad")  # remove an item from a list
print(result)
last = result.pop()  # return the last item we have inserted, O(1)
print(last)
print(result)  # last item is removed
# lists can also be reversed with .reverse()
result.reverse()
print(result)
# inbuilt sort function
result.sort()
print(result)

# list comprehension -> create a new list based on the existing values of another list

# tuples are very similar to lists, the items cannot be changed, tuples are immutable

my_tuple = ('Asad', 'Idris', 'Misha', 'Alayna')  # we can store different data types as with lists
# you can't change or add any new elements to tuples
# we can still loop through them

# string = 'Asad'  # this is a string object
# string_tuple = ('Asad',)  # this is a tuple object with only one member

print(type(my_tuple))

# mutable objects allow modification after creation, these are lists, sets, dicts and custom objects like classes
# immutable objects cannot be changed after creation, such as int, float, bools and tuples
# the memory location of mutable objects do not change when some of the values change, this is not true with immutable objects

x = 5  # immutable object
print(id(5))  # memory address of x
x += 1
print(id(x))  # memory location has changed
# python stores x in a new memory location after incrementing the value
# this is because integers are a immutable data type, and x is just the variable assigned to the integer object
# 5 is it's own object, as is 6. They have separate memory locations, so x points to a different place when its incremented

# this is not the case for mutable objects like lists
print(id(my_list))
my_list.append("test")
print(id(my_list))  # still the same, we have updated the original list

# linked list is a dta structure, the aim is to be able to store items efficiently (insertion and removal operations)
# changing items in the middle of an array leads to costly shifting of elements, linked lists do not have this problem
# if we have the head node, we can access every subsequent element by following the next pointer
# every node stores data and a reference to the next node, this is why linked lists use more memory than arrays
# linked lists have no random indexing, finding an arbitrary element in a linked list is still O(N) running time
# inserting at the front of the list is O(1), as is deleting
# inserting at the end is O(N) as we have to iterate through it to get to the end, this is much slower than arrays
# linked lists are dynamic data structures, they can acquire new memory at runtime and can store different sized items, manipulating the first element is O(1)
# however linked lists have no random access, need more memory because of references, you can only iterate forwards (unless using a doubly linked list)
# doubly linked lists let us access forwards and backwards

# doubly linked list implementation is called a dequeue
from collections import deque

linked_list = deque([])  # initialse with an empty list
# append inserts items to the tail
linked_list.append(10)
linked_list.append("Hello")

print(linked_list)
# append_left inserts at the head
linked_list.appendleft("First!")
print(linked_list)

# pop() removes the rightmost item and returns it
# popleft() does the same for the front of the list
linked_list.pop()
linked_list.popleft()
print(linked_list)

# we can still use indexing for deque
print(linked_list[0])

# to search for arbitrary items faster than O(N), we can use hashing
# dictionaries are abstract data types and the underlying data structure is a 1d array
# composed of a collection of key value pairs, each key must be unique
# we can achieve O(1) time for insertion and removal
# we transform the keys into array indexes by running them thorugh a hash function
# we then search the array for the given value after converting the key into an index

my_dict = {'name':'Asad', 'age': 25}
print(my_dict)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
# remember that the value of a dictionary can be another dictionary

# a set is implemented with a one dimensional array with a hash function
# sets are unordered and un-indexed, we do not knoe the position of the items
# we are not able to store duplicates

my_set = {"my name is asad", 25, 100, True}
print(my_set) # unordered, so can print out in a different order every time
# the point of a set is that we can check in O(1) time that an item is present
# remember that pop will pop a random item when used by a set
# combine sets using the union function

# The main difference between sort and sorted in Python is that sort function returns nothing
# and makes changes to the original sequence, while the sorted () function creates a new sequence type containing a sorted version of the given sequence.
# the sorted fucntion has the key parameter, we can define the logic behind the sorting

nums = [1,7,3,5,2,9,8,7,11,34,4]
asc_nums = sorted(nums)
desc_nums = sorted(nums, reverse=True)
print(asc_nums)
print(desc_nums)

my_dict = sorted(my_dict, key=lambda myset: myset[0])
print(my_dict)  # now age comes before name
