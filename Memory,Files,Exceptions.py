
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

a = ['Asad', 25, 100]  # a list object on the heap referred to by the stack reference a
b = a  # stack reference b now points to the same heap object that a does
# there are 2 references to the same list object
# every object in python has an extra field - the reference counter that is increased (decreased) when a reference to the object is created (removed)
# if teh reference counter reaches zero, it means that the garbage collector can safely remove that object form the heap memory
# the garbage collection is the process that removes unused and unreferenced objects from the heap
# the del keyword decrements the reference counter

# we can use the is_instance() function to check if a variable is an object
print(isinstance(a, object))  # is a referring to an object

# there is a crucial difference between call-by-reference and call-by-value
# call by value : just a copy of the original variable is passed so the original variable will not be altered
# call by reference : the variable itself is passed so the original variable will be altered
# python does something different: pass by object reference, it depends on whether or not the variable is mutable or immutable
# python will not change the value of immutable objects passed to functions
# it will change mutable objects however
