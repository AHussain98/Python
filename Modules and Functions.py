# it is possible to produce python code which is not intended to be executed directly
# instead it provides functions and classes

from time import *  # unsafe import, this brings in all objects
# from time into your namespace, so you dont use the time. operator to access

# import turtle # catchall import
# from turtle import forward,right,left # selective import
# import time  # import these two modules, safer to import this way and use .
#
# forward(150)  # now we dont need to do turtle.forward(), we can just use forward()
# right(90)
# forward(100)
# left(180)
# forward(200)
#
# time.sleep(3)  # sleep for 3 seconds
import webbrowser

print(dir())  # anything starting with 2 underscores is not intended to be changed
# webbrowser.open("https://www.futhead.com/23/players/81/riyad-mahrez/")
# epoc is number of seconds since start date, this is generally jan 1st 1970 on linux
#
# import time
# from datetime import datetime  # import the class from the module
#
# print(time.gmtime())  # UTC, named tuple
# print(time.localtime())  # named tuple
# print(time.time())  # number of seconds since epoc, 1st jan 1970
#
# time_here = time.localtime(time.perf_counter())  # capture the tuple
# print(time.strftime("%c", time_here))
#
# print(f"the epoch of this system stats at {time.strftime('%c', time.gmtime(0))}")
#
# if time.daylight != 0:
#     print("daylight saving time is in effect")
#     print(f"the local timezone is {time.tzname[1]}")
#
# # some time functionality is platform specific, be wary of this
#
# print(datetime.today())  # first one is module, second is class
# print(datetime.now())
#
# import pytz  # another timezone package
#
# for x in pytz.all_timezones:
#     print(x)
#
# for x in pytz.country_names:  # dictionary
#     print(pytz.country_names[x])
#
# print(type(pytz.country_names))
# print(pytz.timezone('GB'))
#

# now onto functions

# create a function
def python_food():
    print("chicken and rice")


# now call the function
python_food()
# all python functions return a result, if you don't tell it what to return, it returns None
print(python_food())  # see what it returns, the function is called and its returned value is printed


# def centre_text(*args, sep = ' ', file = None):  # modify for multiple args, create a default seperator
#     text = ""
#     for arg in args:
#         text += str(arg) + sep # concatenate the arguments and add them to the string
#     left_margin = (80 - len(text))
#     print(" " * left_margin, text, file = file) # write the output to the optional file argument
#
#
# centre_text("Asad")
# centre_text("Asad Ali Hussain", 25, "London", sep=':')

# parameter is the variable defined in the function definition itself
# argument is what you pass in when you call the function
# two functions that take the same parameters are said to have the same signature

# lets try opening a file

# with open("centered.txt", mode='w') as centred_file:
#     centre_text("Asad Ali Hussain", 25, "London", sep=':', file = centred_file) # sent to a file correctly

# lets create a version that returns
# def returns_centre_text(*args, sep = ' '):  # modify for multiple args, create a default seperator
#     text = ""
#     for arg in args:
#         text += str(arg) + sep # concatenate the arguments and add them to the string
#     left_margin = (80 - len(text))
#     return " " * left_margin + text # plus instead of comma
#
# print(returns_centre_text("Yo yo", "Yo", 123, sep='!'))  # now we can just send the returned value of the function to prin

# we can also assign the returned result of functions to a variable

# s1 = returns_centre_text("Yo yo", "Yo", 123, sep='!')
# print(s1)
#
# # parabola function
#
# def parabola(int: x):
#     return x*x
#
# for x in range(-100,100):
#     print(parabola(x))

# print(type(s1)) # data type of the object
# print(repr(s1)) # printable representation of an object as a string
# print(locals()) # prints all the local objects, can be used within functions

# what you define within a function is local only to that function, as with C++ global variable, defined in the
# global space local space is within class or function, if you change the value of a global variable within a local
# space, python will create a copy of the variable for use within the local space, the global variant is unchanged
# and you no longer refer to the global variable within your scope

# this is unless you use the global keyword

# name='Asad'  # global variable
# print(name) # global
# def change_name():
#    # name = 'Hussain'
#    global name  # this just tells python to use the global version of the variable from this point on
#    # if we've used the global keyword, then changes made in local scope will carry over
#    name = 'Hussain'
#    print(name)  # will be the local version if we've changed the global, but since we used the global keyword,
#    # the change carries over to global scope
#
# change_name()
# print(name)  # global version has changed due to above

# The basic rules for global keyword in Python are:
#
# When we create a variable inside a function, it is local by default.
# When we define a variable outside of a function, it is global by default. You don't have to use the global keyword.
# We use the global keyword to read and write a global variable inside a function.
# Use of the global keyword outside a function has no effect.

# when you import a python module, its code is loaded into memory and then executed
# if you import a script, it will run immediately as soon as its imported

# importing a module sorts out namespaces as well as executing code
# when modules are imported, an attribute of the module called __name__ is set to the name of the module, without path or extention
# when a python module is executed as a script, the __name__ attribute is set to __main__

print(__name__)  # shows main

# preventing code from being executed when its imported is simply a case of checking if __name__ == '__main__'
# this is checked in the code we're importing, if this is false then we make it so that it wont execute
# this is done by indenting all of the executable code within the above if statement

# if __name__ == '__main__':  # this is not executed if we import the code, this check should contain the executable
# #     # code and should be at the very bottom of the imported module
# #     change_name()
# #     print(name)

# in python, there is no concept of access control, such as private or protected variables
# so in theory, you could access and change code in modules you've imported that you shouldn't be able to change
# modules and varibales that start with an underscore should not be changed outside of the module they belong to, they're classed as protected
# there's nothing preventing us from changing this like in C++ but its a sign for the programmer to not change it

# when you use import *, python will not import any functions that begin with _ or with __
# when you import normally, you can access these by using the name of the module with teh . operator

# using double underscore infront of a class or variable invokes python name mangling
# _foo: Only a convention. A way for the programmer to indicate that the variable is private (whatever that means in Python).
#
# __foo: This has real meaning. The interpreter replaces this name with _classname__foo as a way to ensure that the name will not overlap with a similar name in another class.
#
# __foo__: Only a convention. A way for the Python system to use names that won't conflict with user names. Don't change these

# anything that starts and ends with 2 underscores generally shouldnt be changed

# import Dictionaries
#
# print(Dictionaries.vehicles)

# python allows functions to be nested in another function
# useful for recursion
# remember that recursive solutions shouldn't be a go-to, there could be an iterative solution which is faster and preferred

# recursion can be useful for dealing with directories
# os module provides access to files and directories

import os
print(os.name)

# listing = os.walk('.') # returns a list of tuples
# for root, directories, files in listing:
#     print(root, directories, files)

#print(listing)

print(os.listdir())

# The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
#
# Use the keyword nonlocal to declare that the variable is not local.
# this is similar to our global example with names above, but is useful for functions where we don't want to change the global variable
# and we just want to change the closest variable, in the outer function

def myfunc1():
  x = "John"
  def myfunc2():
    x = "hello"
  myfunc2()
  return x

print(myfunc1())  # john is returned and printed

def myfunc1_2():
  x = "John"
  def myfunc2_2():
    nonlocal x  # declare the x below to be non-local, python uses the one above
    x = "hello"
  myfunc2_2()
  return x

print(myfunc1_2())  #  now hello is printed

# global keyword tells python to look for a variable in the global scope
# nonlocal tells python to looks for the variable closest to the keyword and use that

# only access global and nonlocal variables when absolutely necessary
# python searches for things in order of LEGB -> local, enclosing, global, builtins

# also if we dont change or redefine the variables in a nested function, we can access them

def myfunc1_3():
  x = "Asad"
  def myfunc2_3():
    y = "hello " + x  # we can access x and we get a local copy, we haven't changed it
    print(y)
    print(locals())  # these are the local variables in the nested function, we can see x in here
    # this is a python optimisation so it doesn't have to go looking for what x is and where its defined
  myfunc2_3()

myfunc1_3()  # accessed the variable in enclosing scope without using non-local

# if you assign a value to a name inside a function, then that name will have a local Python scope. 
# In contrast, if you assign a value to a name outside of all functions—say, at the top level of a module—then that name will have a global Python scope.
# 
# Python Scope vs Namespace
# In Python, the concept of scope is closely related to the concept of the namespace. 
# As you’ve learned so far, a Python scope determines where in your program a name is visible.
# Python scopes are implemented as dictionaries that map names to objects. These dictionaries are commonly called namespaces.
# These are the concrete mechanisms that Python uses to store names. They’re stored in a special attribute called .__dict__.


# If and else scopes do not count as anew scope, as anything you define or use within them will be accessible in the outer scope that the if/else statement exists in
# same for for loops
