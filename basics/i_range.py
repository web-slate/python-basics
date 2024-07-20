from stylepy import h1, h2, h3, h4, h5, h6

h1('\n >>>> Range Data Type Example')
h5('\n >>>> Print Until 7 `range(8)` wrap with list')
h5(list(range(8)))

h5('\n >>>> Print from 2 to 7 `range(2, 8)` wrap with list')
h6(list(range(2, 8)))

h4('\n >>>> Print from 0 to 20 increment 2 like 2 Table')
h5('Using `range(0, 13, 2)` wrap with list')
h6(list(range(0, 13, 2)))

h4('\n >>>> Print from 0 to 20 increment 2 like 4 Table')
h5('Using `range(0, 13, 4)` wrap with list')
h6(list(range(0, 13, 4)))

h4('\n >>>> Print from 0 to 20 increment 2 like 7 Table')
h5('Using `range(0, 13, 7)` wrap with list')
h6(list(range(0, 13, 7)))

h5('\n Type value of type(range(2, 8)) is below')
h6(type(range(2, 8)))


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
h4(fib_sequence)