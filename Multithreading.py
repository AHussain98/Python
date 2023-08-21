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

def count_operation(x=100):
    for i in range(x):
        print(threading.current_thread().name + ' ' + str(i))
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

print('Main thread will still print this in between tc and tc2!')  # gets printed in main threads next time slice, not after the above 2 are finished

# remember that the main thread creates the other threads
# but the main thread keeps on executing in a sequential manner, it will get its own time slices as well as the threads it created
# using the join() function, we can wait for threads to finish execution
# so we can block the main thread until the other threads are finished
t1.start()
# t1.join()  # join function forces main thread to wait for given thread to complete execution

t2.start()
t1.join()  # join function forces main thread to wait for given thread to complete execution

t2.join()
print('Main thread will now execute this after the above 2 are done!')
# join function blocks the calling threads execution (main thread in this case) until completion of the joined thread

# we can also pass parameters to the thread object by adding args=

t3 = threading.Thread(target=count_operation, name='Thread #3', args=(10,))  # remember to add the brackets and comma because we're passing a tuple
# args=10 would process 10 as a string

t3.start()

### In the theoretical section, we have considered processes and threads. Threads are light-weight processes running within a given process. So multiple threads may belong to the same process.

# By the way this is why synchronization is needed because these threads are using the same resources of the same process - such as memory.
#
# Let's create 5 threads and then let's see the process which they belong to. This is why we need to import os (stands for operating system) module to be able to get the PID (Process ID) associated with the threads.
#
# from threading import Thread
# import os
#
#
# class Counter(Thread):
#
#     def __init__(self, name):
#         Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         for i in range(10):
#             print('%s is running and belongs to process with ID  %s' % (self.name, str(os.getpid())))
#
#
# t1 = Counter('Thread #1')
# t2 = Counter('Thread #2')
# t3 = Counter('Thread #3')
# t4 = Counter('Thread #4')
# t5 = Counter('Thread #5')
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# And the result is that all the threads share the same process. Which means that all of these threads have the same Process ID (PID).
#
# Thread #1 is running and belongs to process with ID  1788
# Thread #1 is running and belongs to process with ID  1788
# Thread #1 is running and belongs to process with ID  1788
# Thread #1 is running and belongs to process with ID  1788
# Thread #1 is running and belongs to process with ID  1788
# Thread #1 is running and belongs to process with ID  1788
# Thread #1 is running and belongs to process with ID  1788
# Thread #1 is running and belongs to process with ID  1788
# Thread #1 is running and belongs to process with ID  1788
# Thread #1 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #2 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #3 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #4 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788
# Thread #5 is running and belongs to process with ID  1788

# a thread in python can be either a daemon thread or a standard worker thread
# when a python program starts then one thread begins running immediately (main thread)
# we can create child threads from the main thread. The main thread is the last thread to
# finish execution because it performs various shutdown operations
# daemon threads are intended as helper threads ( for example garbage collection)

# so when we run an application, the virtual machine starts the main thread (which we can use to create child treads) and kicks off daemon threads to run in the background

# we are able to create daemon threads directly aswell
# daemon threads are low priority threads that run in the background to perform tasks like garbage collection
# usually we create daemon threads for i/o operations or connecting to other applications, downloading data etc...
# daemon threads are terminated by the pvm when all other worker threads are terminated (finish execution)
# this is the main difference, worker threads are not terminated by the pvm while deamon threads are

def daemon_operation():

    while True:
        print('this is a daemon thread!')

dt = threading.Thread(target=daemon_operation, name='dt', daemon=True) # create a daemon thread

dt.start()  # even though the daemon thread is running an infinite loop, the pvm will terminate it when there are no more normal threads running

print(' this is printed by the main thread')

# threads (of the same process) run in shared memory space while processes run in seperate memory spaces
# every thread has its own stack memory but all threads share the heap memory
# the main purpose of synchronization is the sharing of resources without interference using mutual exclusion
# we talk about locking because we need to manage the fact that the treads share the heap memory
