import json
import csv

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

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filename = 'flowers_print.txt'  # this file will be created and opened in the write state when we run the programme
with open(plants_filename, "w") as plants:
    for plant in data:
        print(plant, file = plants)  # file keyword tells print where it should print the data to

# now lets try reading from the file

new_list = []
with open(plants_filename) as plants: # read mode as default
    for plant in plants:
        new_list.append(plant.rstrip())  # rstrip method gets rid of newline character

print(new_list)

plants_write_filename = 'plants.write.txt'

with open(plants_write_filename, "w") as plants:
    for plant in data:
        plants.write(plant)  # file objects also have write methods, we cna use this or the print method to write to a file
# the write method sends exactly what you specify to the file
# the print method includes things like line breaks and seperators, and performs other conversions
# the print function calls a special method that all objects have, before printing the object
# the method is called __str__, this returns a string representation of the object
# so somethings won't work with write(), such as pushing numerical values into a txt file, these files only accept strings so this wont work

# each time you open the file with w, it will wipe the file first
# use 'a' to append to the file

# Technical debt -> whe you're facing a problem now because of design decisions made earlier
# This also describes problems we're creating for the future, if we choose limited solutions now

# ASCII and Unicode are encodings used to standardise character sets
# in python3, all strings are unicode
# An encoding standard is a numbering scheme that assigns each text character in a character set to a numeric value.
# Unicode is the universal character encoding used to process, store and facilitate the interchange of
# text data in any language while ASCII is used for the representation of text such as symbols, letters, digits, etc.

with open('test.json', 'w', encoding='utf-8') as testfile:  # create a json file with a specific encoding
    json.dump(data,testfile)

csv_filename = 'OlympicMedals_2020.csv.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',') # readline returns one line from the file, first line in this case
    print(f"column headers: {headers}")
    csv_file.seek(0) # return the file pointer to the start of the file
    sample = csv_file.read() # read the whole file
    csv_file.seek(0) # return the file pointer to the start of the file
    file_dialect = csv.Sniffer().sniff(sample) # sniffer works out what the delimiter should be, we can then pass this object as teh dialect to teh reader
    reader = csv.reader(csv_file, dialect=file_dialect) # reader iterates over the file object

    for row in reader:
        print(row)

# repr() function used to check what a string actually contains

