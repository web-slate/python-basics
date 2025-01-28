# Variable Examples in Python

## Variable Naming Rules

- Variable names should start with alphanumeric characters, an underscore (`_`), or a string.
- Variable names must not start with numbers or hyphens.
- Variable names are case-sensitive.

### Invalid Variable Examples

```python
# Throws `SyntaxError: invalid decimal literal`
# 1fruit = 'hello'

# Throws `SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?`
# -adhi = 'graduated'
# =adhi = 'graduated'
```

## Multiple Variables

### Assigning Multiple Values

```python
x, y, z = 1, 2, "Three"
print(f"X is {x}, Y is {y}, Z is {z}")
```

## Swapping Variables

### Using Unpacking

```python
a = 'apple'
b = 'bat'
b, a = a, b  # Time and Space complexity is O(1)
print(f"After Unpacking: A value is {a}, B value is {b}")
```
- **Time Complexity:** `O(1)` - Simply swapping references to the string objects.
- **Space Complexity:** `O(1)` - No additional space is required.

### Using Additional Memory

```python
c = b
b = a
a = c
print(f"After using additional memory: A value is {a}, B value is {b}")
```
- **Time Complexity:** `O(1)` - Each assignment is a constant-time operation.
- **Space Complexity:** `O(1)` - Introduces a single additional variable `c`.

### Using Slicing Without Additional Memory

```python
a = a + b
b = a[:len(a) - len(b)]
a = a[len(b):]
print(f"After Slicing: A value is {a}, B value is {b}")
```
- **Time Complexity:** `O(n + m)` - Where `n` is the length of string `a` and `m` is the length of string `b`.
- **Space Complexity:** `O(n + m)` - Slicing operations create new strings.

## Integer Swapping

### Using Unpacking

```python
a = 1
b = 2
b, a = a, b
print(f"Now Integer A position is {a}, B position is {b}")
```

### Using Arithmetic Operations

```python
a = a + b
b = a - b
a = a - b
print(f"After computation of a+b, a-b, a-b ==== Now Integer A position is {a}, B position is {b}")
```

### Using XOR Approach

```python
a ^= b
b ^= a
a ^= b
print(f"After XOR Approach ==== Now Integer A position is {a}, B position is {b}")
```

## One Value to Multiple Variables

```python
previous = current = next = 1
print(f"previous: {previous}, current: {current}, next: {next}")
```

## Unpack a Collection

### List Example

```python
fruits = ["apple", "banana", "cherry"]
firstFruit, secondFruit, thirdFruit = fruits
print(f"firstFruit: {firstFruit}, secondFruit: {secondFruit}, thirdFruit: {thirdFruit}")
```

