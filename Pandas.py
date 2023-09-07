# pandas is a library for the python programming language for data manipulation and analysis
# pandas relies heavily on numpy and c
# pandas is extremely fast with data manipulation (multidimensional arrays or matrixes)
# pandas is used for reading and writing data, reshaping, data set merging and joining and data filtration
# pandas and numpy are extremely fast because of vectorization - and elimination of slow loops

# pandas uses c with cython under the hood to speed up time critical operations
# pandas uses extremely optimised loops and features multiple iterators
import pandas as pd

# first create a dictionary
my_dict = {'name' : ['Asad', 'Aisha', 'Misha'],
           'ages': [25, 26, 10]}

print(my_dict)

# now transform the dictionary into a pandas dataframe
df = pd.DataFrame(my_dict)
print(df)  # produces a matrix from a dictionary

# a series is like a single column of a data frame
series = pd.Series([10,20,30,40,50])  # create a series by passing in a list
print(series) # every item in the series is identified by a single index
print(series/2) # we can handle the entire series as if its a single variable
# we can still get access to each element at each index via []

# we can update an item at a given index by referencing its index
series[0] = 60
print(series)  # updated
# we can specify what the indexes should be
series2 = pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])  # indexes for series2 will be chars
print(series2)

# there are min and max functions for data frames
print(series.max())
# remember that a series is how we can handle a 1d array of items efficiently

# you can transfordm any kind of structure into a data frame, such as lists, dicts, numpy arrays, other data frames etc...