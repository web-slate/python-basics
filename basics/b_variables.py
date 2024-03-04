print('\n >>>> Variable Example');
print("Variable name should start with alpha-numeric characters, _ or string")
print("Variable name should not start with numbers, hyphen")
print("Variable names are case sensitive");

# Below code throws `SyntaxError: invalid decimal literal`.
# 1fruit = 'hello'

# Below code throws `SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?`
# -adhi = 'graduated'
# SyntaxError: invalid syntax
# =adhi = 'graduated'

# Multiple Variables
print("\n>>>> Multiple Variables with String literal");
x, y, z = 1, 2, "Three"
print(f"X is {x}, Y is {y}, Z is {z}")

# Swapping example
print("\n>>>> Swapping Variables with String literal");
a = 'apple'
b = 'bat'
# b, a = a, b
# Alternative solution using Additional memory
c = b
b = a
a = c
print(f"A value is {a}, B value is {b}")
# Better Solution is using `Bitwise XOR` 

# How about in integer swapping values?
print("\n>>>> Swapping Integer Variables with String literal");
a = 1
b = 2
b, a = a, b
print(f"Now Integer A position is {a}, B position is {b}")
a = a + b
b = a - b
a = a - b
print(f"\n>>>> After computation of a+b, a-b, a-b ==== Now Integer A position is {a}, B position is {b}")
a ^= b; b ^= a; a ^= b
print(f"\n>>>> After XOR Approach of a ^= b; b ^= a; a ^= b ==== Now Integer A position is {a}, B position is {b}")

# One Value to Multiple Variables
print("\n>>>> One Value to Multiple Variables");
previous = current = next = 1
print(f"previous: {previous}, current: {current}, next: {next}")

# Unpack a Collection
print("\n>>>> Unpack a Collection: list, tuple")
fruits = ["apple", "banana", "cherry"]
firstFruit, secondFruit, thirdFruit = fruits
print(f"firstFruit: {firstFruit}, secondFruit: {secondFruit}, thirdFruit: {thirdFruit}")
