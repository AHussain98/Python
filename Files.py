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

# we can also create a writer csv object which writes what we pass to it
# there is a csv DictReader method that reads lines as dictionaries
# a with block can be used to open several files at the same time
# seek() sends the file pointer to the particular offset
# tell() returns the current stream position

""" We started the section with a look at files and directories.

Directories – or folders – can contain files, as well as other directories.

As a programmer, it's important to understand file paths. You'll often need to provide paths to your program's data files, for example.

It's also very useful to be able to use the command line (or CLI - Command Line Interface). For the basics, at least, there isn't a huge difference between the Windows command prompt and the *nix terminal. There are minor differences, such as ls vs dir to list the files in the directories.

Another difference is in the character used to separate the various parts of a path. Windows uses the backslash (\), whereas Linux and OSX use the slash (/). In Python, specify your paths using a slash - that avoids the need to escape the backslash characters in strings, and means your relative paths will be valid on all 3 operating systems.



We then looked at opening text files for reading, and writing.

When you open a file, you must close afterwards. Use with is safer, as your file will be closed automatically, when the with block terminates.



You can open a file for reading, writing, or both.

If you want to open a file for both reading and writing, make sure you understand the difference between the behaviour of 'r+' and 'w+'.



With text files, the following methods are used to read from a file:

readline() reads a single line from the file and returns a string. This is the same behaviour as when we did for line in jabber:, the file is read one line at a time. For large files, this is the recommended approach as it does not read the entire file into memory.

readlines() reads the entire file and returns a list of strings, so the entire file is read into memory (which can cause problems with very large files).

read() as we used it, reads the entire file and (if it's a text file) returns a string containing the contents of the file. read() can also take an optional parameter specifying how much data to read (as we'll see later).



The corresponding methods, when writing, are:



writelines() writes each of the items in a list, to the output file. Lines separators are not included. When working with text files, it can be more convenient to use print (with the file= keyword argument) instead of write or writelines.

write() writes a single item to the output file. No string conversion is performed – so you'd get an error if you tried to write an integer. Once again, you can use print if you want the automatic string conversion of integers.



Line feeds are represented by the '\n' character. You'll often want to strip line feeds from the ends of the strings you read, and the strip method can be used to do this.



We also looked at reading (and writing) data from some common file formats. We covered:

Parsing data from a text file.

Splitting fields on various separators.

JSON.

Various CSV formats.



Make sure you use the correct encoding, when reading and writing text files. Be explicit about the encoding you expect, when reading, and the encoding you're going to use, when writing.

If you read Unicode text with the wrong file encoding, you'll get garbage or errors (more often, errors).

 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
"""

