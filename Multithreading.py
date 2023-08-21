# by default, programming languages are sequential: they execute the statements and commands line by line
# in single threaded applications, methods are called one by one, we have to wait for them to finish one by one
# in this scenario, time consuming operations may freeze the application and the users may not know what's happening

# the most relevant reason for multithreading is to seperate multiple tasks: one or more which is time critical
# and may be subject to interference by the execution of other tasks

# multithreading is the ability of the cpu to execute multiple processes or threads concurrently
# both processes and threads are independent sequences of execution

# a process is an instance of program execution -> when you open a software or web browser, these are distinct processes
# the OS assigns distinct registers, stack memory and heap memory to every single process

# a thread is a lightweight process
# a thread is a unit of execution within a given process ( a process may have multiple threads)
# each thread in a process shares the memory and resources and this is why programmers must know concurrent and multithreaded techniques

# processing time for a single core is shared among processes and threads, this is called time slicing
# e.g. a single processor core may use thread 1 for a time slice, then thread 2 for a time slice and so on

# there is a difference between multi-threading and parallel computing
# for parallel computing, every processor core will have just a single thread which means they can run threads continously without time slicing

# advantages of multithreading:
# we can design more responsive applications, we can do several operations concurrently
# we can achieve better resource utilization ( make the most of the cpu's you have)
# we can improve performance

# disadvantages of multithreading:
# multithreading is not always better
# threads manipulate data located on the same memory area because they belong to the same process and we have to deal with this fact (synchronisation)
# its not easy to design multithreaded applications (easy to make bugs)
# expensive: switching between threads is expensive, cpu has to save local data, application pointer etc...
# of the current thread and load the data of the other thread aswell
# its very expensive to switch between threads, so using multiple threads for small problems is not always performant

import threading

print(threading.current_thread().name)  # main thread

# so the main thread runs all these commands sequentially
# all other threads are created by the main thread (also known as the application thread)

def count_operation():
    for i in range(100):
        print(threading.current_thread().name + str(i))
# sequential execution
count_operation() # main thread executes these sequentially
count_operation()  # this method call is executed as soon as the above one is finished

# lets create another thread and try doing this concurrently
t1 = threading.Thread(target=count_operation,name='t1') # thread class intantiation
# target is the callable object that the thread should execute
# name is the name of the thread
t2 = threading.Thread(target=count_operation,name='t2')

# so now these thread objects have been instantiated, we can now start them with the start method
# t1.start()  # main function will then kick off this thread and while it executes, moves onto the next line
# t2.start()  # main then kicks off this thread while the first one is running
# because of time slicing, the OS will execute the threads at the same time

# Multithreading is a technique where multiple threads are spawned by a process to do different tasks, at about the same time, just one after the other.
# This gives you the illusion that the threads are running in parallel, but they are actually run in a concurrent manner.
# In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.

class Counter(threading.Thread):  # this is how we can inherit from the thread class

    def __init__(self):
        threading.Thread.__init__(self)

    # when you start a thread, this run function is called
    def run(self):
        for i in range(100):
            print(f"{self.name} thread is running: {str(i)}") # this name is automatically assigned in the Thread class

# now lets instantiate this counter
tc = Counter()
tc2 = Counter()

tc.start()  # inherits the start function
tc2.start()  # we have achieved inherited multithreading
# both threads will run concurrently with the help of timeslicing
# python will run the first thread for a short amount of time, then the 2nd, then the first again etc...
# pythons GIL prevents more than one thread executing bytecode at one time
