print("Today is a good day to learn Python")
print('python is fun')
#works with both single and double quotes
print("we can even include 'quotes' in strings!") #provided they are different types
print("hello" + " world") #concatenation

greeting = "Hello"
#name = input("Please enter your name:") #take an input and store in the variable name, input function executes first
#print(greeting + " " + name)

splitString = "This string has been \nsplit over \nseveral \nlines" #\n used to move to a new line
print(splitString)

tabbedString = "1\t2\t3\t4\t5" #/t to create tabs
print(tabbedString)

print()

print("The owner said \"he's resting at the minute.\"") #to use quotes inside a string, we can escape them
print("""The owner said "he's resting at the minute." """) #or we can use triple quotes

anotherSplitString = """This
string
has 
been 
split
over 
several
lines"""

print(anotherSplitString) #also when using triple quotes, each string on a line is printed on a single line

print("Number 1\tThe Larch\nNumber 2\tThe Horse Chestnut")

print("you can include \\ in strings by using two \\ in a row") #you can include \ in your printed text by escaping it with another backslash

parrot = "Norwegian Blue" #binding the variable parrot to this string
print(parrot) #print the whole thing
print(parrot[3]) #pring only the char at index 3
#python, same as c++, starts with index 0

#you can also index backwards by using a negative number
print(parrot[-1]) #prints the last char
#we can get the negative index values by subtracting the positive index values from the string length

#list slicing done by using 3 values seperated by colon
print(parrot[0:6]) #start at index 0 and go upto index 6 (not including position 6)
print(parrot[0:14:2]) #from 0 to 14, print every 2nd index
print(parrot[:9]) #from start to index 9, empty start field defaults to start
print(parrot[10:]) #from 10 to end
#square brackets are used for indexing and slicing

print(parrot[-4:-2]) #counting from end of string
print(parrot[-4:12]) #prints same as above
print(parrot[0:6:2]) #starts at index 0, extends upto but not inlcuding index 6  in steps of s

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators) #prints everything from every 4th index above, starting from 1

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1] #stop value defaults to the start of the string due to the -1 step
print(backwards)
backwards = letters[::-1]#goes from z to a automatically, due to the negative step
print(backwards)
print(letters[:17:-1]) #print last 8 characters in reverse order
print(letters[-1:]) #just z
print(letters[:1]) #just a
print(letters[:-1:])

#numbers cant be concatenated to strings in python
#division of two ints is a float
#python is case sensitive

#we have operators we can use on sequences:
string1 = "he's "
string2 = "probably "
string3 = "hungry "
string4 = "for the "
string5 = "cake"
print(string1 + string2 + string3 + string4 + string5)
#the pluses arent necessary when printing string literals in python
print("he's " "probably " "hungry" )
#strings in python can also be multipled
print("Hello" *5) #HelloHelloHelloHelloHello

#we can also check if one string appears in another
today = "Friday"
print("day" in today) #true
print("Thur" in today) #false
#in operator evaluates to true if the first element appears in the string

#in python, every datatype can be coerced into a string representation using the str function

age = 24
print("My age is " + str(age)) #str function has converted my int age value into a string
#we can also do this with the .format method, the numbered replacement fields are replaced with the values given after the .format
print("my age is {0}".format(age)) #the variable appears in the {0} space
#replacement fields dont need to be used in order
print("my favourite month is {2}, I was born on the {0}rd day of {2} and I {1} it, and {0} is my lucky number!".format(23,"love","March"))


print("Splitting an input like "
      "this is "
      "fine")

for i in range(1,13):
    print("{0} squared is {1} and cubed is {2}".format(i,i**2,i**3))
#you can raise one number to the power of another using **

print() #blank line

#but these dont quite line up when we print them, so we can actually specify width by doing this:
for i in range(1,13):
    print("{0:2} squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))
    #so the above means use the first value in the format, and make the column a width of 2, then for the second and third input, make it a width of 3 and 4
    #we've also used < after the colon to align the values to the left
    #^ means centred

print("Pi is approximately {0:12}".format(22/7)) #field width of 12
print("Pi is approximately {0:12f}".format(22/7)) #f means floating point value, defaults to 6 digits
print("Pi is approximately {0:12.50f}".format(22/7)) #f for floating point, width of 12 but now precision of 50

for i in range(1,13):
    print("{} squared is {} and cubed is {}".format(i,i**2,i**3)) #replacement field numbers are necessary, if not provided then they'll just print in order
    #we can print ints within a string is we use replacement fields

#string interpolation, not used in python 3
age = 24
print("My age is %d years" %age) #to insert a float, its %f, and a string is %s
