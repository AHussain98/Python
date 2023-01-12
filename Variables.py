#when a program runs, everything the program uses is stored in the computers memory
#program code and the data it uses are stored in different areas of memory
#a variable is a name for a specific area of memory where we've stored useful data
#python sets up variable data types for us automatically, based on the data we store in the variable, so we dont need to delcare string etc... variables
#variables are created when attached to a value using =

age = 24
print(age)
name = "Asad"
print(type(age)) #function for finding out the data type of a variable
print(type(name))

#in python, we can bind and unbind variables to data types as we wish, the age variable is currently mapped to an int
#but we can change this to map to a string:

age = "Twenty-Four"
print(age) #this reassignment works in python, not in c++, but its not good practice

#python 3 has 3 numerical data types, int, float and complex
#int - whole number
#float - real number, decimal point
#theres no limit to the size of an int you can store in python
#python has 5 sequence types built in: strings, lists, tuples, ranges and byte/bytearray
computer_parts = ["monitor", "keyboard", "mouse"]
print(computer_parts[0])
print(computer_parts[0][1])



