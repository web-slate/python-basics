from data_types.commonUtils import spaceComplexity, timeComplexity


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
print("\n>>>> Swapping String Variables Using unpacking return with String literal");
a = 'apple'
b = 'bat'
b, a = a, b # Time and Space complexity is O(1), Constant Time, which is faster.
timeComplexity('O(1)', 'Because the operation is simply swapping references to the string objects')
spaceComplexity('O(1)', 'No additional space is needed to perform the swap.')

print(f"After Unpacking: A value is {a}, B value is {b}")
# Alternative solution using Additional memory
print("\n>>>> Alternative solution using Additional memory with String literal");
c = b
b = a
a = c
print(f"After using additional memory: A value is {a}, B value is {b}")
timeComplexity('O(1)', 'Each of the assignments (c = b, b = a, a = c) is a constant-time operation.')
spaceComplexity('O(1)', 'This method introduces a single additional variable c. The space used by c does not depend on the size of the strings a and b')
# Alternative solution without using Additional memory
print("\n>>>> Alternative solution without using Additional memory which is slicing and return in String literal");
a = a + b
b = a[:len(a) - len(b)] # which is :5, so start from begining and stop before 5th position.
a = a[len(b):] # which is start from 5: and the rest.
print(f"After Slicing: A value is {a}, B value is {b}")
timeComplexity('O(n + m)', 'where N is the length of string a and M is the length of string b.')
spaceComplexity('O(n + m)', 'slicing operations also create new strings that require additional space.')


# How about in integer swapping values?
print("\n>>>> Swapping Integer Variables Using unpacking return in String literal");
a = 1
b = 2
b, a = a, b # Unpacking in Python and Destruction in JS
print(f"Now Integer A position is {a}, B position is {b}")
a = a + b
b = a - b
a = a - b
print(f"\n>>>> After computation of a+b, a-b, a-b ==== Now Integer A position is {a}, B position is {b}")
a ^= b
b ^= a
a ^= b
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
