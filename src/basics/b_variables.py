
from stylepy import h1, h2, h3, h4, h5, h6
from stylepy import spaceComplexity
from stylepy import timeComplexity
h1('\n >>>> Variable Example');
h2("Variable name should start with alpha-numeric characters, _ or string")
h3("Variable name should not start with numbers, hyphen")
h4("Variable names are case sensitive");

# Below code throws `SyntaxError: invalid decimal literal`.
# 1fruit = 'hello'

# Below code throws `SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?`
# -adhi = 'graduated'
# SyntaxError: invalid syntax
# =adhi = 'graduated'

# Multiple Variables
h5("\n>>>> Multiple Variables with String literal");
x, y, z = 1, 2, "Three"
h5(f"X is {x}, Y is {y}, Z is {z}")

# Swapping example
h6("\n>>>> Swapping String Variables Using unpacking return with String literal");
a = 'apple'
b = 'bat'
b, a = a, b # Time and Space complexity is O(1), Constant Time, which is faster.
timeComplexity("O(1)", "Because the operation is simply swapping references to the string objects")
spaceComplexity("O(1)", "No additional space is needed to perform the swap.")

h4(f"After Unpacking: A value is {a}, B value is {b}")
# Alternative solution using Additional memory
h5("\n>>>> Alternative solution using Additional memory with String literal");
c = b
b = a
a = c
h4(f"After using additional memory: A value is {a}, B value is {b}")
timeComplexity('O(1)', 'Each of the assignments (c = b, b = a, a = c) is a constant-time operation.')
spaceComplexity('O(1)', 'This method introduces a single additional variable c. The space used by c does not depend on the size of the strings a and b')
# Alternative solution without using Additional memory
h5("\n>>>> Alternative solution without using Additional memory which is slicing and return in String literal");
a = a + b
b = a[:len(a) - len(b)] # which is :5, so start from begining and stop before 5th position.
a = a[len(b):] # which is start from 5: and the rest.
h4(f"After Slicing: A value is {a}, B value is {b}")
timeComplexity('O(n + m)', 'where N is the length of string a and M is the length of string b.')
spaceComplexity('O(n + m)', 'slicing operations also create new strings that require additional space.')


# How about in integer swapping values?
h4("\n>>>> Swapping Integer Variables Using unpacking return in String literal");
a = 1
b = 2
b, a = a, b # Unpacking in Python and Destruction in JS
h4(f"Now Integer A position is {a}, B position is {b}")
a = a + b
b = a - b
a = a - b
h4(f"\n>>>> After computation of a+b, a-b, a-b ==== Now Integer A position is {a}, B position is {b}")
a ^= b
b ^= a
a ^= b
h5(f"\n>>>> After XOR Approach of a ^= b; b ^= a; a ^= b ==== Now Integer A position is {a}, B position is {b}")

# One Value to Multiple Variables
h4("\n>>>> One Value to Multiple Variables");
previous = current = next = 1
h5(f"previous: {previous}, current: {current}, next: {next}")

# Unpack a Collection
h4("\n>>>> Unpack a Collection: list, tuple")
fruits = ["apple", "banana", "cherry"]
firstFruit, secondFruit, thirdFruit = fruits
h5(f"firstFruit: {firstFruit}, secondFruit: {secondFruit}, thirdFruit: {thirdFruit}")
