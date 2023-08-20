# so firstly we have to write the source code of the application, this is then compiled into machine level binary code
# this is then loaded into memory

# The Python source code goes through the following to generate an executable code
#
# Step 1: The Python compiler reads a Python source code or instruction in the code editor. In this first stage, the execution of the code starts.
# Step 2: After writing Python code it is then saved as a .py file in our system. In this, there are instructions written by a Python script for the system.
# Step 3: In this the compilation stage comes in which source code is converted into a byte code. Python compiler also checks the syntax error in this step and generates a .pyc file.
# Step 4: Byte code that is .pyc file is then sent to the Python Virtual Machine(PVM) which is the Python interpreter. PVM converts the Python byte code into machine-executable code and in this interpreter reads and executes the given file line by line. If an error occurs during this interpretation then the conversion is halted with an error message.
# Step 5: Within the PVM the bytecode is converted into machine code that is the binary language consisting of 0’s and 1’s. This binary language is only understandable by the CPU of the system as it is highly optimized for the machine code.
# Step 6: In the last step, the final execution occurs where the CPU executes the machine code and the final desired output will come as according to your program.

# our application actually uses memory from regions called the stack and heap
# stack memory is a special region in RAM
# stack is also a special data type but it's the memory region that stores local variables and method calls
# because method calls are on the stack, the programme knows where to return to after finishing execution of a given method
# the stack is small in size but fast to access
# if the stack has too many frames on it and exceeds capacity, this is a stack overflow error

# heap memory is another special region in RAM where dynamic memory allocation takes place
# the size of the heap is much larger than the size of the stack
# objects are stored on the heap
# references to these heap objects are stored on the stack
# the heap is large in size but slow to access
# the python virtual machine keeps track of these objects allocated on the heap and deletes them when they no longer have an active reference, unlike C++ where this is manual

# stack memory works in frames
# so a function called on the stack will have a frame on the stack containing all the local variables created within the function
# remember that objects in python are on the heap by default, so the reference to the object will be on its own stack from on the stack
# while the object and its data members will be on the heap
# class and instance variables are both on the heap
# house_ref = House(),  house_ref is on the stack while the House object is on the heap
# when a function finishes executing, it is removed from the stack, and execution control returns to the point where the function was called

# in python, we do not have to bother with objects on the heap memory
# the garbage collection will remove unused objects
# when there are no active references from the stack memory to an object on the heap, it becomes eligible for garbage collection
# python uses reference counting to handle this
# every variable in python is a reference to an object
# a single object may have several references, there may be several variables pointing to it

a = ['Asad', 25, 100]  #  a list object on the heap referred to by the stack reference a
b = a  #  stack reference b now points to the same heap object that a does
#  there are 2 references to the same list object
#  every object in python has an extra field - the reference counter that is increased (decreased) when a reference to the object is created (removed)
#  if the reference counter reaches zero, it means that the garbage collector can safely remove that object form the heap memory
#  the garbage collection is the process that removes unused and unreferenced objects from the heap
#  the del keyword decrements the reference counter

#  we can use the is_instance() function to check if a variable is an object
print(isinstance(a, object))  # is a referring to an object

#  there is a crucial difference between call-by-reference and call-by-value
#  call by value : just a copy of the original variable is passed so the original variable will not be altered
#  call by reference : the variable itself is passed so the original variable will be altered
#  python does something different: pass by object reference, it depends on whether or not the variable is mutable or immutable
#  python will not change the value of immutable objects passed to functions
#  it will change mutable objects however

with open('test.txt', 'r') as test:
    print(test.read())

#  there are two main types of errors: syntax errors and exceptions
#  syntax errors are parsing errors which occur when code has a type or invalid commands
#  exceptions are errors detected during execution
#  exceptions should be handled to make sure the application does not crash

#  we can handle exceptions with try-except-finally blocks
#  if there are no exceptions, the except block is never called (it is skipped)
#  if an exception occurs during the execution of the try block, the except block will be called and then the execution continues after the try-except statement
#  there may be several except clauses (we can catch multiple exceptions)

#  we can force a specified exception to occur with the help of the raise keyword
#  we can define our own exception, we just have to use exception as the parent class

try:
    a = 10
    b = 0
    a/b
except ZeroDivisionError:  # we have to pass an exception
    print('not possible to divide by zero')
finally:  # the following code gets executed whether there is an error or not
    print("finally block")

print('code didnt crash! we got here')

age = 10

try:
    if age < 18:
        raise Exception('You are underage')  # raise the exception

except Exception as exception: # except block for the exception object we just created
    print(exception.args)  # print the exception message

# to create our own exception, we have to create an exception object that inherits from the exception superclass

