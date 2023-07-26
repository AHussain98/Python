# it is possible to produce python code which is not intended to be executed directly
# instead it provides functions and classes

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

import time
from datetime import datetime  # import the class from the module

print(time.gmtime())  # UTC, named tuple
print(time.localtime())  # named tuple
print(time.time())  # number of seconds since epoc, 1st jan 1970

time_here = time.localtime(time.perf_counter())  # capture the tuple
print(time.strftime("%c", time_here))

print(f"the epoch of this system stats at {time.strftime('%c', time.gmtime(0))}")

if time.daylight != 0:
    print("daylight saving time is in effect")
    print(f"the local timezone is {time.tzname[1]}")

# some time functionality is platform specific, be wary of this

print(datetime.today())  # first one is module, second is class
print(datetime.now())

import pytz  # another timezone package

for x in pytz.all_timezones:
    print(x)

for x in pytz.country_names:  # dictionary
    print(pytz.country_names[x])

print(type(pytz.country_names))
print(pytz.timezone('GB'))


# now onto functions

# create a function
def python_food():
    print("chicken and rice")


# now call the function
python_food()
# all python functions return a result, if you don't tell it what to return, it returns None
print(python_food())  # see what it returns, the function is called and its returned value is printed


def centre_text(*args):  # modify for multiple args
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text))
    print(" " * left_margin, text)


centre_text("Asad")
centre_text("Asad Ali Hussain", 25, "London")

# parameter is the variable defined in the function definition itself
# argument is what you pass in when you call the function
# two functions that take the same parameters are said to have the same signature
