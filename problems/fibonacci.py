from stylepy import h1,h2,h3,h4,h5,h6
import time

def getMinutes(elapsed_time):
    minutes = int(elapsed_time // 60)
    return minutes

def getSeconds(elapsed_time):
    seconds = elapsed_time % 60
    return seconds

# recursive_fibonacci Function
h1('\n >>>> recursive_fibonacci Function to return fibonacci until n');
h3('\n This one time complexity is O(2^n) Exponential and have redundant calculations');

def recursive_fibonacci(n):
    if (n < 2):
        return n;

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2);

start_time = time.time() # Start time
n = 41;
h4('Note: Recursive approach without memoization is highly inefficient for large values of n due to the exponential growth of recursive calls and redundant computations.');
h5(f"recursive_fibonacci({n}) is {recursive_fibonacci(n)}");
end_time = time.time() # End time

print(f"This function took {getMinutes(end_time - start_time)} minutes and {getSeconds(end_time - start_time):.2f} seconds")

# memoized_recursive_fibonacci Function
h1('\n >>>> memoized_recursive_fibonacci Function to return fibonacci until n')
h4('\n This one optimized now so Time and Space Complexity is O(n)')

def memoized_recursive_fibonacci(n, memoized={0: 0, 1:1}):
    if n not in memoized:
        memoized[n] = memoized_recursive_fibonacci(n - 1, memoized) + memoized_recursive_fibonacci(n - 2, memoized)
    return memoized[n]

start_time = time.time() # Start time
n = 41
h4(f"memoized_recursive_fibonacci({n}) is {recursive_fibonacci(n)}")
end_time = time.time() # End time
h5(f"This function took {getMinutes(end_time - start_time)} minutes and {getSeconds(end_time - start_time):.2f} seconds")

# iterative_fibonacci Function
"""
"""
h1('\n >>>> iterative_fibonacci Function to return fibonacci until n')
def iterative_fibonacci(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.

    :param n: The position in the Fibonacci sequence.
    :return: The Fibonacci number at position n.
    """
    if n <= 1:
        return n

    prev, curr = 0, 1 # Start with zero and increment by 1.
    for i in range(2, n + 1): # iterate until n + 1 if n is 7 it will be 2 to 8 = 6 times
        prev, curr = curr, prev + curr
        # print(f"prev: {prev} and curr: {curr}")

    return curr

start_time = time.time() # Start time
n = 7
h4(f"iterative_fibonacci({n}) is {iterative_fibonacci(n)}")
h5('\n This one optimized now so Time Complexity is O(n) and Space Complexity is O(1)');
end_time = time.time() # End time
h6(f"This function took {getMinutes(end_time - start_time)} minutes and {getSeconds(end_time - start_time):.2f} seconds")
