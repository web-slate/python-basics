from tabulate import tabulate
def fibonacci_recursive(n: int): 
  if n <= 1:
    return n
  return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print("Reccursive Fibonacci")
n = 10
print([fibonacci_recursive(value) for value in range(n)])


def fibonacci_memoized(n, memo={}):
  if n <= 1:
    return n
  if n not in memo:
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
  return memo[n]
print("Reccursive memoized")
n = 10
print([fibonacci_memoized(value) for value in range(n)])

def fibonacci_optimised(n):
  if n <= 1:
    return n
  prev = 0
  current = 1
  for _ in range(2, n+1 ):
    temp = current
    current = current + prev
    prev = temp
  return current 

print("Reccursive optimised")
n = 10
print([fibonacci_optimised(value) for value in range(n)])

table = (["Solution", "Time complexity", "Space complexity"], 
         ["Recursive", "O(2^n)", "O(2^n)"], 
         ["Recursive memoized" , "O(n)" , "O(n)"],
         ["Optimised" , "O(n)" , "O(1)"])

print(tabulate(table, headers="firstrow"))

