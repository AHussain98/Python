# numpy is numerical python, a library used for handling arrays
# there is no real array data structure in python because almost everything is an object
# we can achieve 50x faster running times with numpy, an important library for numerical methods when speed and memory are crucial
# implemented in python but under the hood runs c and c++

# everything is an object in python, remember that lists store references to integer objects
# every reference is 8 bytes in size, this is why storing a lot of items in lists has a huge memory complexity
# numpy arrays are stored in a contiguous block of memory, items are right next to each other
import numpy as np

python_list = [1,2,3,4,5]   # a standard python list, objects
numpy_array = np.array(python_list)  # construct a numpy array, contigous elements

print(type(numpy_array))  # array is still an object
# we can store different types in a list in python, but not in a numpy array
a = np.array([1,1.5,True])  # these will be stored as strings
print(a)

# we can still update values with indices
a[1] = 10
a[2] = 20
print(a)

# we can insert by defining the array, the index and the item we want to insert, insert returns an array
new_a = np.insert(a,2,100)
print(new_a)

print(new_a.ndim)  # number of dimensions
print(new_a.shape) # how many elements are in each dimension, rows and columns

nums = np.array([[1,2,3],[4,5,6]]) # 2d array
print(nums.shape)

for index,row in enumerate(nums):
    print(index,row)  # row and then the elements
_3d_nums = np.array([1,2,3], ndmin=3)  # ndmin is min number of dimensions, we have specified that this array has 3 dimensions
print(_3d_nums.shape)

# as with standard python lists, we can use negative indices which start from the last item
print(a[-1])
# we can use slicing with the : operator, the same rules apply as with a list
print(a[0:2])

# we can define what the data type of the array should be
floating_array = np.array([1.1,2.2,3.3,4.4,5.5], dtype='f')
print(floating_array.dtype)  # floats on 32 bits

# the reshape function changes the shape of a given array
# the shape is the number of items in each dimension

nums = nums.reshape(6) # change the 2d array into a single dimensional array, of 6 elements
print(nums)
# the reshape function will work as long as we have enough elements to reshape into the shape we want
# use -1 as one of the args in reshape to allow python to calculate the value of the unknown dimension

# we can also stack and merge these numpy arrays

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = np.vstack((arr1,arr2))
print(result)  # vertically stack the numpy arrays, output is a 2d array

result2 = np.hstack((arr1,arr2))  # merge the arrays

# filtering in numpy

num_arr = np.array([1,2,3,4,5])
bool_arr = np.array([True,True,False,False,True])
result3 = num_arr[bool_arr]  # result is where each of these is equivalent
print(result3) # 1,2 and 5 evaluate as True

result4 = num_arr < 3
print(result4)  # prints where this is true, array of bools
