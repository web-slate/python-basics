# python module.py basics/e_strings.py
import sys

from data_types.commonUtils import timeComplexity
print('\n >>>> String Type Example')

def format_size(size_bytes):
    # Define the conversion constants
    KB_FACTOR = 1024
    MB_FACTOR = KB_FACTOR ** 2
    GB_FACTOR = KB_FACTOR ** 3
    TB_FACTOR = KB_FACTOR ** 4

    # Perform the conversions and format the output
    if size_bytes >= TB_FACTOR:
        return f"{size_bytes / TB_FACTOR:.2f} TB"
    elif size_bytes >= GB_FACTOR:
        return f"{size_bytes / GB_FACTOR:.2f} GB"
    elif size_bytes >= MB_FACTOR:
        return f"{size_bytes / MB_FACTOR:.2f} MB"
    elif size_bytes >= KB_FACTOR:
        return f"{size_bytes / KB_FACTOR:.2f} KB"
    else:
        return f"{size_bytes} bytes"

print('\n >>>> What is maximum value can be stored inside python string variable?')
print('Below is the Max size')
max_size = sys.maxsize
formatted_size = format_size(max_size)
print(f"Max size: {formatted_size}")

print('\n >>>> Single line using single quote')
print('Single quote is same as double quote for string data type')

print('\n >>>> Single line using double quote')
print("Single quote is same as double quote for string data type");

print('\n >>>> Multi line using single quote')
print('''
      Multi line statement can be
      created using 3 single quotes.
''');

print('\n >>>> Multi line using double quote')
print("""
      Multi line statement can be
      created using 3 double quotes.      
""")

greet = 'welcome';

print('\n >>>> Slicing Example')
print('>>>> Accessing one specific character in string variable')
print(' >>>> Find the 3rd character from 0th index')
print(greet[3]); # return `c`

print('\n >>>> number after colon executed with `-1` which will considered as start:stop');
print('\n >>>> Accessing 3rd to 5th specific character in the string variable')
print(' >>>> Find the characters from 0th index to 5th index')
print(greet[3:6]); # return `com`

print('\n >>>> Accessing from 0 to 5th specific character in the string variable')
print(' >>>> Find the characters from 0th index to 5th index')
print(greet[:6]); # return `welcom`

print('\n >>>> Accessing from 3rd to end of the string variable')
print(' >>>> Find the characters from 0th index to last index')
print(greet[3:]); # return `come`

print('\n >>>> Accessing from last to 4 characters in the string variable')
print(' >>>> Find the characters from last index to 4 characters')
print(greet[-4:]); # return `come`

print('\n >>>> Accessing from last to 4 characters but skip last character in the string variable')
print(' >>>> Find the characters from last index to 4 characters with skipping last character')
print(greet[-4:-1]); # return `come`

print('\n >>>> Iteration Example')
print(' >>>> Iterate the Greet String and print each charactor')
for character in greet:
    print(f"character: {character}")

print('\n >>>> Find Length Example')
print(' >>>> Find a Length of greet String')
print('greet length', len(greet))

print('\n >>>> `in / not in` Exist Check Example')
print(' >>>> Find whether `w` string exist in greet variable using `in` keyword')
timeComplexity('O(n)', 'In Python, strings are typically implemented as arrays of characters. The operation \'w\' in greet is essentially a search operation where Python checks each character in the string greet to see if it matches \'w\'')
print('w' in greet) 

print('\n >>> Use `in` statement in `if` statement as well')
if 'w' in greet:
    print('w exist in greet variable')
    
print('\n >>> Use `in` statement in `if` statement as well')
if 'u' not in greet:
    print('u Not exist in greet variable')

print('\n >>>> Format Example')
designation = 'Full Stack engineer'
company = 'Meta Inc'
location = 'Singapore'
product = 'Meta Enterprise Platform'
print(' >>>> format() method takes unlimited number of argument. Example');
about = 'I am currently {} at {} and working in {}.'
print(about.format(designation, company, location))

print('\n >>>> format() with index numbers')
info = 'hey i work for {1} in {0} as {2}'
print(info.format(location, company, designation))

print('\n >>>> format() with missing index numbers, means not giving all the index')
print('>>>> Error: cannot switch from manual field specification to automatic field numbering')
# info1 = 'hey i work for {1} in {} as {}'
# print(info1.format(location, company, designation))
# print('''>>>> Below String code throws Error: g\n
# hey i work for {1} in {} as {}\nthrows: Value
# Error: cannot switch from manual field specification to automatic field numbering
# '''.format(location, company, designation))