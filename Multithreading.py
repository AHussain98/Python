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

# import threading
#
# print(threading.current_thread().name)  # main thread
#
# # so the main thread runs all these commands sequentially
# # all other threads are created by the main thread (also known as the application thread)
#
# def count_operation(x=100):
#     for i in range(x):
#         print(threading.current_thread().name + ' ' + str(i))
# # sequential execution
# count_operation() # main thread executes these sequentially
# count_operation()  # this method call is executed as soon as the above one is finished
#
# # lets create another thread and try doing this concurrently
# t1 = threading.Thread(target=count_operation,name='t1') # thread class intantiation
# # target is the callable object that the thread should execute
# # name is the name of the thread
# t2 = threading.Thread(target=count_operation,name='t2')

# so now these thread objects have been instantiated, we can now start them with the start method
# t1.start()  # main function will then kick off this thread and while it executes, moves onto the next line
# t2.start()  # main then kicks off this thread while the first one is running
# because of time slicing, the OS will execute the threads at the same time

# Multithreading is a technique where multiple threads are spawned by a process to do different tasks, at about the same time, just one after the other.
# This gives you the illusion that the threads are running in parallel, but they are actually run in a concurrent manner.
# In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.
#
# class Counter(threading.Thread):  # this is how we can inherit from the thread class
#
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     # when you start a thread, this run function is called
#     def run(self):
#         for i in range(100):
#             print(f"{self.name} thread is running: {str(i)}") # this name is automatically assigned in the Thread class
#
# # now lets instantiate this counter
# tc = Counter()
# tc2 = Counter()
#
# tc.start()  # inherits the start function
# tc2.start()  # we have achieved inherited multithreading
# # both threads will run concurrently with the help of timeslicing
# # python will run the first thread for a short amount of time, then the 2nd, then the first again etc...
# # pythons GIL prevents more than one thread executing bytecode at one time
#
# print('Main thread will still print this in between tc and tc2!')  # gets printed in main threads next time slice, not after the above 2 are finished

# remember that the main thread creates the other threads
# but the main thread keeps on executing in a sequential manner, it will get its own time slices as well as the threads it created
# using the join() function, we can wait for threads to finish execution
# so we can block the main thread until the other threads are finished
# t1.start()
# # t1.join()  # join function forces main thread to wait for given thread to complete execution
#
# t2.start()
# t1.join()  # join function forces main thread to wait for given thread to complete execution
#
# t2.join()
# print('Main thread will now execute this after the above 2 are done!')
# # join function blocks the calling threads execution (main thread in this case) until completion of the joined thread
#
# # we can also pass parameters to the thread object by adding args=
#
# t3 = threading.Thread(target=count_operation, name='Thread #3', args=(10,))  # remember to add the brackets and comma because we're passing a tuple
# # args=10 would process 10 as a string
#
# t3.start()

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
#
# def daemon_operation():
#
#     while True:
#         print('this is a daemon thread!')
#
# dt = threading.Thread(target=daemon_operation, name='dt', daemon=True) # create a daemon thread
#
# dt.start()  # even though the daemon thread is running an infinite loop, the pvm will terminate it when there are no more normal threads running
#
# print(' this is printed by the main thread')

# threads (of the same process) run in shared memory space while processes run in separate memory spaces
# every thread has its own stack memory but all threads share the heap memory
# the main purpose of synchronization is the sharing of resources without interference using mutual exclusion
# we talk about locking because we need to manage the fact that the treads share the heap memory
# import threading
#
# x = 0 # global variable
#
# def increment():
#     global x  # global variable
#
#     x = x + 1  # so increment the value of the x variable we defined in the global scope, this is the critical section
#
# def operation():
#     for _ in range(10000000):
#         increment()
#
# t4 = threading.Thread(target=operation, name='Thread #4')  # they both call this function to increment the heap object referenced by x
# t5 = threading.Thread(target=operation, name='Thread #5')
#
# t4.start()
# t5.start()
#
# t4.join()
# t5.join()
#
# print(' the value of x now is ' + str(x))  # the value of x is 2 million, but only sometimes
# this is because the threads are reading the value of x from heap memory, incrementing the value and writing the return value to heap memory
# these increment operations take time
# during an increment procedure, another thread may call the method with the original counter value, overwriting the value of x that was changed by the other thread

# A task performed by a computer is said to be atomic when it is not divisible anymore: it can't be broken into smaller steps.
# Atomicity is an important property of multithreaded operations: since they are indivisible, there is no way for a thread to slip through an atomic operation concurrently performed by another one.

# the above example is why its very important to deal with synchronisation when working with multiple threads to avoid inconsistencies

# synchronization makes sure that no 2 threads execute the same block of code (called the critical section)
# the critical section is the part of the program where the shared resources are being accessed
# race condition occurs when 2 or more threads can access these shared resources
# the state of the variables and resources are non-deterministic (depends on the context switching of threads), so every time we rerun the application, the values will be different because the threads finish in different orders
# synchronization and locks can deal with race conditions

# z = 0 # global variable
# lock = threading.Lock()  # instantiate the lock class
# # only a single thread may acquire the lock at a single time
#
# def l_increment():
#
#     global z  # global variable
#     lock.acquire()  # call the lock objects acquire method before the critical section, other threads will be in a 'blocked' state because they are waiting for the lock to be released
#     # when a lock is acquired, other threads must wait for it to be accessible again
#     z = z + 1  # so increment the value of the z variable we defined in the global scope, this is the critical section
#     lock.release()  # now release the critical section, other threads may now increment the value of x
#     # release can be called from any thread, not just the thread that acquired the lock
#
# def l_operation():
#     for _ in range(10000000):
#         l_increment()
#
# t6 = threading.Thread(target=l_operation, name='Thread #6')  # they both call this function to increment the heap object referenced by x
# t7 = threading.Thread(target=l_operation, name='Thread #7')
#
# t6.start()
# t7.start()
#
# t6.join()
# t7.join()
#
# print('this is z: ' + str(z))

# so every time a thread enters the l_increment function, it has to try to acquire the lock
# if the lock has already been acquired, then the thread waits until the lock is released by default
# we can also set a blocking argument in the lock object, so the waiting thread can either wait or return immediately when encountering a lock acquired by another thread

### In the previous lectures we have been talking about locks.
# We can use either the standard threading.Lock or threading.RLock class that is the re-entrant lock

# the standard Lock can be acquired once before it must be released
# on the other hand, RLocks can be acquired multiple times from the same thread (no matter that it has been already acquired)
#
# RLock must be released the same number of times it has been acquired
#
# with Locks: the acquired lock can be released by any thread
#
# RLocks can be released by the thread that acquired it exclusively
#
# Ok so a thread cannot acquire a lock owned by another thread.
# But a given thread can acquire a lock that it already owns.
# Allowing a thread to acquire the same lock more than once is called re-entrant synchronization.
# And this is exactly what is happening in Python with RLocks - the same thread may acquire the lock more than once.
#
# For example: let's consider recursive method calls.
# If a given thread calls a recursive and synchronized method several times then it is fine
# (note that in this case the same thread "enters" the synchronized block several times).
# There will be no deadlock because of re-entrant synchronization.

# standard locks cannot be acquired once they have already been acquired
# so a lock object is not able to call the acquire function after it has already done so, without releasing first

# # however, this is not the case with re-entrant locks
# rlock = threading.RLock()  # rlock object
#
# rlock.acquire()
# rlock.acquire()  # called multiple times, this is acceptable
# print('finished with this operation')
# rlock.release()
# rlock.release()  # you have to call release as many times as you called lock
#
# class Test:
#
#     def __init__(self):
#         self.num1 = 1
#         self.num2 = 2
#         self.lock = threading.Rlock()
#
#     def increment_first(self):
#         with self.lock:   # this is the same as:
#             # try: self.lock.acquire()
#             # finally self.lock.release(),  its a thread safe way of incrementing num1
#             self.num1 += 1
#
#     def increment_second(self):
#         with self.lock:
#             self.num2 += 1
#
#     def increment_both(self):  # this is where we need re-entrant locks, because we may need to increment first while a lock has already acquired it
#         with self.lock:
#             self.increment_first()  # we can acquire the lock in increment_first() again with no issue because we are using re-entrant locks
#             self.increment_second()

# deadlock occurs when threads are waiting for each other to release the lock
# deadlock means two or more threads are waiting forever for a lock or resource held by another of the threads
# deadlock is a situation where two or more competing actions are waiting for each other to finish, and thus neither ever does
# so a process or thread enters a waiting state because a resource is requested from another waiting process, which is in turn waiting for another resource held by another waiting process etc...

# livelock:
# a thread often acts in response to the action of another thread
# if the other thread's action is also a response to the action of another thread, then livelock may arise
# livelocked threads are unable to make further progress
# the threads are not blocked, they are simply too busy responding to each other to resume work

# lock.acquire(True)  # this means if the lock is acquired by another thread, wait for it to be free, danger of deadlock
# lock.acquire(False) # this means that if the lock is acquired by another thread, then return immediately
# lock.acquire(True,10)  # timeout passed in as 10 seconds, so thread will wait 10 seconds for the resource to be released, if it still can't be acquired then return

# semaphores are simple variables (or abstract data types) that are used for controlling access to a common resource
# important concept in operating systems as well
# they are considered a count of how many units of a particular resource are available
# counting semaphores: allows an arbitrary resource count
# binary semaphores: semaphores that are restricted to 1's and 0's

# semaphors tracks only how many resources are free, id does not keep track of which of the resources are free
# the semaphore count may be a useful trigger for a number of different events
# producer-consumer problem can be solved and implemented with the help of a semaphore
# semaphores control the number of threads that can perform or access a given action
# import time
# import random
# semaphore = threading.Semaphore(5)  # semaphore limit is 5
# operation_counter = 0
#
# def compute():
#     global operation_counter
#     semaphore.acquire() # whenever a given thread calls the semaphore acquire method, the semaphore checks that the counter value is greater than 0
#     # it will then decrease the limit by 1
#     # if the semaphore's internal counter value reaches 0, the given thread must wait for another thread to release their semaphore
#     operation_counter += 1
#     print(' total number of computations: ' + str(operation_counter))
#     time.sleep(random.randint(3,8))
#     semaphore.release() # semaphore then increments its internal counter
#     operation_counter -= 1

# while True:
#     time.sleep(0.1)
#     t = threading.Thread(target=compute) # create as many threads as possible
#     t.start()

# we can communicate between threads using the Event object
# capacity = 5
# items = []
# event = threading.Event()  # instantiate the event object
#
# class Producer(threading.Thread):
#     def __init__(self, nums):
#         threading.Thread.__init__(self)
#         self.nums = nums
#
#     def run(self) -> None:
#
#         while True:
#             if len(self.nums) == capacity:
#                 event.set() # sets the internal flag of the event object to be true
#                 # all threads waiting for it to become true are awakened
#
#             if not event.is_set():
#                 time.sleep(1)
#                 self.nums.append(random.randint(1,100))
#                 print('Producer: ' + str(self.nums) + '\n')
#
# class Consumer(threading.Thread):
#     def __init__(self, nums):
#         threading.Thread.__init__(self)
#         self.nums = nums
#
#     def run(self) -> None:
#
#         while True:
#             if len(self.nums) == 0:
#                 event.clear() # resets the internal flag to false
#
#
#             if event.is_set():
#                 time.sleep(1)
#                 self.nums.pop() # remove the last item from the data structure
#                 print('Consumer: ' + str(self.nums) + '\n')
#
#
# if __name__ == '__main__':
#     producer = Producer(items)
#     consumer = Consumer(items)

    # producer.start() # start fucntion executes the overrided run fucntion
    # consumer.start()

    # producer will keep adding items until we reach 5
    # the consumer will remove all items and reset the event flag



# it is not convienient to create large numbers of threads
# its also quite an expensive operation to create and destroy threads
# this is why we have thread pools, which don't destroy threads but reuse them
# so at the beginning of the program, we can define how many threads we are going to create and use
# and if a given thread finishes execution, python can reuse it instead of a costly destroy and recreate operation

from concurrent.futures import ThreadPoolExecutor

import threading
# executor = ThreadPoolExecutor(max_workers=4)
#
# def operation():
#     time.sleep(2)
#     print('operation is finished')
#
# executor.submit(operation) # because we have defined just one thread in the pool, this one thread is going to complete these operations one after another
# executor.submit(operation)
# executor.submit(operation)
# executor.submit(operation)
# executor.shutdown()  # makes sure the executor doesn't perform any more tasks
# shutdown() also acts as the join() method, it waits for the threads to finish before teh main thread continues

# if we have 4 workers and 4 tasks, these can be done simultaneously due to time slicing
# the submit function executes a given operation on a distinct thread
# we can create the thread pool executor with the with keyword so we dont have to bother shutting down

nums = [1,2,3,4,5]

def squares(x):

    print(' the result: ' + str(x*x) + ' and via thread: ' + str(threading.current_thread()))

with ThreadPoolExecutor(max_workers=5) as executor:
  #  executor.map(squares, nums)  # map function takes a function and iterable
    # will execute with a unique thread for each value in the iterable
    # map function will do a sequential execution
    for value in nums:
        executor.submit(squares, value)

# when we use the standard sequential approach, the programming anguage executes the operations one after another
# a multithreaded approach uses multiple threads but these threads are executed with the time slicing algorithm
# multithreading is used to execute independent tasks without blocking other tasks

# with parallel algorithms, we execute different tasks on different processors (or processor cores) simultaenously
# paralellisation is used to speed up a given application
# some problems are sequential by default and so we are not able to apply parallelisation

# the aim of multithreading is not to speed up the application itself
# if we want to reduce running time, we need to use paralellisation

# paralellism -> no timeslicing, each processor given its own process to own and run

# it depends on the operating system and hardware as to how the threads will be executed
# if there is just one processor core, then the time slicing algorithm executes the threads (multithrading)
# if there are multiple processor cores then the operating system may execute the threads in parallel

# GIL is a mutex that protexts access to python objects
# it prevents multiple threads from executing python bytecode at once
# so prevents multithreaded applications from taking full advantage of multiprocessing systems
# there is no real parallel computing in Python
# we can use parallel processes but it is not as efficient as threads
# this is because threads are lightweight processes
# multiprocessing has higher overheads
# switching between threads is expensive, switching between processes is even more expensive
# 
