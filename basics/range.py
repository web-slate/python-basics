from stylepy import h1, h2, h3, h4, h5, h6

h1('\n >>>> Range Data Type Example')
print('\n >>>> Print Until 7 `range(8)` wrap with list')
print(list(range(8)))

print('\n >>>> Print from 2 to 7 `range(2, 8)` wrap with list')
print(list(range(2, 8)))

print('\n >>>> Print from 0 to 20 increment 2 like 2 Table')
print('Using `range(0, 13, 2)` wrap with list')
print(list(range(0, 13, 2)))

print('\n >>>> Print from 0 to 20 increment 2 like 4 Table')
print('Using `range(0, 13, 4)` wrap with list')
print(list(range(0, 13, 4)))

print('\n >>>> Print from 0 to 20 increment 2 like 7 Table')
print('Using `range(0, 13, 7)` wrap with list')
print(list(range(0, 13, 7)))

print('\n Type value of type(range(2, 8)) is below')
print(type(range(2, 8)))


# def square(number):
#     return number ** 2

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))

h2('\n >>>> Print Fibonacci Sequence until 10th Number')

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example: Generate first 10 Fibonacci numbers
fib_sequence = list(fibonacci(10))
print(fib_sequence)