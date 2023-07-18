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
"""

# the bytes data type is an array of bytes, array not list
# its a sequence that can store values in the range 0 to 255

equation = bytes((207, 128, 0, 255, 190)) # pass a tuple to the function
print(equation)
print(type(equation)) # bytes class
print(len(equation)) # this confirms we do have an array of bytes
print(equation[0])

"""In this second half of this section, we explored binary files:



Computers work in binary (base 2) with numbers stored as a sequence of zeros and ones (on or off).

Computers store everything, including text files, as binary.

When working with binary files, you need to know what the file contains. There should be documentation – a specification – describing the contents of the file. Without a specification, it will be difficult to work out what the sequence of bytes actually represents.

The corollary to that is, you should create your own documentation if you write your own binary data.



We used the Python bytes-like objects – bytes and bytearray – when reading binary data. bytearray is a mutable version of the bytes type. bytes is immutable – just like strings.

In fact, the bytes type provides many of the same methods as strings. We used the split and startswith methods, for example, in our code.



bytes and bytearray are arrays, and each value must be a byte: a number between 0 and 255.

Unlike lists, all items in an array must be of the same type. Bytes-like objects are arrays of bytes.



Python 2 strings were the equivalent of Python 3 bytes. In Python 3, strings are sequences of Unicode characters.

If a bytes or bytearray object contains Unicode data, you can decode it to produce the corresponding string. It's important to use the correct codec when decoding a bytes-like object to a string.



We used a bitmap file as a practical example of reading and writing binary data.

Common binary file formats, such as bitmaps or mp3 files, are well documented. Other files may contain data in a proprietary format – for example, Microsoft didn't document the format of the files produced by Microsoft Word (.doc files) until 2008. Or, more accurately, they didn't release the .doc file specification until that year. They would have had a specification for use by their own programmers.



Binary file formats can be complex. There may be sections that are optional, or variable length. We followed the specifications for 2 different binary file formats – .bmp and .mp3 – to make sense of the data they contain. Our code didn't handle every possible case that was documented, but we were able to use the specs to produce some useful results.



You can use slicing to get bytes from the byte array, or use the available methods to convert a sequence of bytes into one of the numeric types.

We used the from_bytes method of the int class, to produce an integer from a sequence of bytes.

When doing that, it's essential to know whether the bytes are stored in big-endian or little-endian format.



Little endian – the least significant byte appears first.

Big endian – the most significant byte appears first. This is also be referred to as network order.



If you need to convert a bytes or bytearray to a floating point value, check out the struct module. We haven't covered struct. Reading floating point data is quite advanced, and if you find that you need to do that you'll be advanced enough to work it all out from the documentation.



When reading the tags from an MP3 file, we covered a few more important concepts:

We saw how to check that we've reached the end of the file (or, in our case, that we hadn't reached the end of the file).

Sometimes, string data is stored as null-terminated strings, also known as c-strings. They're terminated by at least 1 zero byte.

You can check a specific bit in a byte by using the bitwise & operator. If a bit is zero, the result will be zero, or False in a boolean expression. If the bit is set, the result will be non-zero (or True).

To avoid a UnicodeDecodeError, avoid decoding bytes unless you're certain they contain valid Unicode.

Comparing a bytes object to a string will always be False. Compare to a bytes object or bytes literal instead.



Reading and writing binary data follows the same basic steps as reading and writing text:

The file is opened for reading, writing, or both.

The file's read method is used to read a number of bytes. If you don't specify how many bytes to read, you'll get all the data from your current position to the end of the file.

Data is written using the file's write method. You provide a bytes or bytearray object (or a bytes literal).

When working with a binary file, the seek method allows you to seek relative to the start or end of the file, or relative to your current position in the file. It's possible to use negative values, to seek backwards as well as forwards.



We finished by checking the hash of a file. We open the file (for reading, in binary mode), then pass the bytes that we read to one of the hash functions. In the next section, we'll expand on this program, to allow the filename to be provided on the command line.
"""
