# all the information you save in your computer is stored in files
# files are stored in containers called directories
# each python project has its own __pychache__ folder, which stores the compiled python code for the project

# test = open('test.txt', 'r') # open the file in read only mode
# # open returns an object we can interact with
# # for i in test:
# #     print(i)
#
# test.close() # we must close the file when we're finished with it

# file descriptors are used by the OS to keep track of the files that ahve been opened
# every available file descriptor is shared system wide
# if you dont close every file you open, you may lose data
# open files with the with keyword will help avoid resource leaks

with open('test.txt', 'r') as test:
    lines = test.readlines() # as soon as we leave the with block, the file will be closed automatically

print(lines) # stores each line as a object in a list

with open('test.txt', 'r') as test:
    lines = test.read()

print(lines) # stored the whole file as a single string

# the default file mode, if you don't specify one is to open the file for reading strip method will strip from both
# ends of the string strip checks each character at the ends of the strings in turn and removes them if they match
# the string you pass in. it stops when it reaches a character that does not match lstrip does this for just the left
# side, rstrip for just the right

string = "This is my string"
outer_dict = {}
new_string = string.strip("This ") # this will remove This and is, as they're both contained in the strip argument
print(new_string)

# removeprefix and removesuffix methods were added in Python 3.9
print(string.removesuffix(" string"))  # remove this from the end

# its good practice to store the filename as a variable, so we can safely reuse it
input_filename = 'test.txt'
with open('test.txt', 'r') as test:
    for row in test:
        data = row.strip('\n').split(',')
        string, number, char_num = data  # unpack the data into these variables for each row
      #  print(data) # this will have the newline char at the end of each list, so strip it for that first
        dict_data = {  # push the values into the data dictionary
            'string' : string,
            'number' : number,
            'char_num' : char_num
        }
        outer_dict[string.casefold()] = dict_data # push this data into the outer dictionary
print(outer_dict)
# one dictionary value can have multiple keys pointing to it, the keys must be unique
