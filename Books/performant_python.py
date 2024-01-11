# high performance programming can be thought of as the act of minimizing these operations either by reducing the overhead 
# (i.e., writing more efficient code) or by changing the way that we do these operations to make each one more meaningful (i.e., finding a more suitable algorithm).

# the bottleneck in any parallel calculation is always the smaller serial tasks that are being spread out.

#  major hurdle with utilizing multiple cores in Python is Python’s use of a global interpreter lock (GIL). The GIL makes sure that a Python process can run
# only one instruction at a time, regardless of the number of cores it is currently using. 
# This means that even though some Python code has access to multiple cores at a time, only one core is running a Python instruction at any given time. 
# While this may seem like quite a hurdle, especially if the current trend in computing is to have multiple computing units rather than having faster ones, this problem can be avoided
# by using other standard library tools, like multiprocessing (Chapter 9), technologies like numpy or numexpr, Cython, or distributed models of computing.

# The frontside bus, for example, is the connection between the RAM and the L1/L2 cache. It moves data that is ready to be transformed by the processor into the staging
# ground to get ready for calculation, and it moves finished calculations out. There are other buses, too, such as the external bus that acts as the main route from hardware
# devices (such as hard drives and networking cards) to the CPU and system memory. This external bus is generally slower than the frontside bus.
# In fact, many of the benefits of the L1/L2 cache are attributable to the faster bus. Being able to queue up data necessary for computation in large chunks on a slow bus
# (from RAM to cache) and then having it available at very fast speeds from the cache lines (from cache to CPU) enables the CPU to do more calculations without waiting such a long time

# This theme of keeping data where it is needed and moving it as little as possible is very important when it comes to optimization.
#The concept of “heavy data” refers to the time and effort required to move data around, which is something we would like to avoid.

#try to take advantage of a CPU’s ability to vectorize a calculation, or run one instruction on multiple data in one clock cycle.
# This concept of vectorization is illustrated by the following code:
import math

def check_prime(number):
    sqrt_number = math.sqrt(number)
    numbers = range(2, int(sqrt_number)+1)
    for i in range(0, len(numbers), 5):
         # the following line is not valid Python code
         result = (number / numbers[i:(i + 5)]).is_integer()
         if any(result):
             return False
    return True

# Here, we set up the processing such that the division and the checking for integers are done on a set of five values of i at a time.
#  If properly vectorized, the CPU can do this line in one step as opposed to doing a separate calculation for every i. 


# before optimising, profile first!
# By profiling first, you can quickly identify the bottlenecks that need to be solved, and then you can solve just enough of these to achieve
# the performance you need. If you avoid profiling and jump to optimization, you’ll quite likely do more work in the long run. Always be driven by the results of profiling

# Robert Kern’s line_profiler is the strongest tool for identifying the cause of CPU-bound problems in Python code. It works by profiling individual
# functions on a line-by-line basis, so you should start with cProfile and use the highlevel view to guide which functions to profile with line_profiler.

# If you haven’t thought about the complexity of Python’s dynamic machinery before,
# do think about what happens in that n += 1 operation. Python has to check that the n
# object has an __add__ function (and if it didn’t, it’d walk up any inherited classes to
# see if they provided this functionality), and then the other object (1 in this case) is
# passed in so that the __add__ function can decide how to handle the operation.
# Remember that the second argument might be a float or other object that may or
# may not be compatible. This all happens dynamically.

# Just as Robert Kern’s line_profiler package measures CPU usage, the memory_profiler module by Fabian Pedregosa and Philippe Gervais measures memory usage on a line-by-line basis. 

def fn_expressive(upper=1_000_000):
    total = 0
    for n in range(upper):
       total += n
    return total

def fn_terse(upper=1_000_000):  # this version is twice as fast!
    return sum(range(upper))

assert fn_expressive() == fn_terse(), "Expect identical results from both functions"
# Both functions calculate the sum of a range of integers. 
# A simple rule of thumb (but one you must back up using profiling!) is that more lines of bytecode will execute more slowly than fewer equivalent lines of bytecode that use built-in functions. 
# The difference between the two code blocks is striking. Inside fn_expressive(), we maintain two local variables and iterate over a list using a for statement. The for
# loop will be checking to see if a StopIteration exception has been raised on each loop. Each iteration applies the total.__add__ function, which will check the type of 
# the second variable (n) on each iteration. These checks all add a little expense. Inside fn_terse(), we call out to an optimized C list comprehension function that
# knows how to generate the final result without creating intermediate Python objects. This is much faster, although each iteration must still check for the types of the
# objects that are being added together (in Chapter 4, we look at ways of fixing the type so we don’t need to check it on each iteration).
# As noted previously, you must profile your code—if you just rely on this heuristic, you will inevitably write slower code at some point. It is definitely worth learning
# whether a shorter and still readable way to solve your problem is built into Python. If so, it is more likely to be easily readable by another programmer, and it will probably run faster

