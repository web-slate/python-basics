# Range Data Type Example

## Print Until 7 `range(8)` wrap with list
- Output: `[0, 1, 2, 3, 4, 5, 6, 7]`

## Print from 2 to 7 `range(2, 8)` wrap with list
- Output: `[2, 3, 4, 5, 6, 7]`

## Print from 0 to 20 increment by 2 (2 Table)
- Using `range(0, 13, 2)` wrap with list
- Output: `[0, 2, 4, 6, 8, 10, 12]`

## Print from 0 to 20 increment by 4 (4 Table)
- Using `range(0, 13, 4)` wrap with list
- Output: `[0, 4, 8, 12]`

## Print from 0 to 20 increment by 7 (7 Table)
- Using `range(0, 13, 7)` wrap with list
- Output: `[0, 7]`

## Type value of `type(range(2, 8))`
- Output: `<class 'range'>`

---

##  Print Fibonacci Sequence until 10th Number
- Example:
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generate first 10 Fibonacci numbers
fib_sequence = list(fibonacci(10))
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]