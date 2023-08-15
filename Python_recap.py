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
