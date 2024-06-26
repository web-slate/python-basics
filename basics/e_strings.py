# python module.py basics/e_strings.py
import sys
from stylepy import timeComplexity
from stylepy import h1, h2, h3, h4, h5, h6

h1('\n >>>> String Type Example')

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

h2('\n >>>> What is maximum value can be stored inside python string variable?')
h3('Below is the Max size')
max_size = sys.maxsize
formatted_size = format_size(max_size)
h6(f"Max size: {formatted_size}")

h4('\n >>>> Single line using single quote')
h5('Single quote is same as double quote for string data type')

h5('\n >>>> Single line using double quote')
h6("Single quote is same as double quote for string data type");

h4('\n >>>> Multi line using single quote')
h5('''
      Multi line statement can be
      created using 3 single quotes.
''');

h6('\n >>>> Multi line using double quote')
print("""
      Multi line statement can be
      created using 3 double quotes.      
""")

greet = 'welcome';

h2('\n >>>> Slicing Example')
h3('>>>> Accessing one specific character in string variable')
h4(' >>>> Find the 3rd character from 0th index')
h5(greet[3]); # return `c`

h5('\n >>>> number after colon executed with `-1` which will considered as start:stop');
h6('\n >>>> Accessing 3rd to 5th specific character in the string variable')
h5(' >>>> Find the characters from 0th index to 5th index')
h6(greet[3:6]); # return `com`

h5('\n >>>> Accessing from 0 to 5th specific character in the string variable')
h6(' >>>> Find the characters from 0th index to 5th index')
h5(greet[:6]); # return `welcom`

h5('\n >>>> Accessing from 3rd to end of the string variable')
h6(' >>>> Find the characters from 0th index to last index')
h5(greet[3:]); # return `come`

h4('\n >>>> Accessing from last to 4 characters in the string variable')
h5(' >>>> Find the characters from last index to 4 characters')
h6(greet[-4:]); # return `come`

h4('\n >>>> Accessing from last to 4 characters but skip last character in the string variable')
h5(' >>>> Find the characters from last index to 4 characters with skipping last character')
h6(greet[-4:-1]); # return `come`

h4('\n >>>> Iteration Example')
h5(' >>>> Iterate the Greet String and print each charactor')
for character in greet:
    h6(f"character: {character}")

h4('\n >>>> Find Length Example')
h5(' >>>> Find a Length of greet String')
h6('greet length', len(greet))

h4('\n >>>> `in / not in` Exist Check Example')
h5(' >>>> Find whether `w` string exist in greet variable using `in` keyword')
timeComplexity('O(n)', 'In Python, strings are typically implemented as arrays of characters. The operation \'w\' in greet is essentially a search operation where Python checks each character in the string greet to see if it matches \'w\'')
h6('w' in greet) 

h5('\n >>> Use `in` statement in `if` statement as well')
if 'w' in greet:
    h6('w exist in greet variable')
    
h5('\n >>> Use `in` statement in `if` statement as well')
if 'u' not in greet:
    h6('u Not exist in greet variable')

h4('\n >>>> Format Example')
designation = 'Full Stack engineer'
company = 'Meta Inc'
location = 'Singapore'
product = 'Meta Enterprise Platform'
h5(' >>>> format() method takes unlimited number of argument. Example');
about = 'I am currently {} at {} and working in {}.'
h6(about.format(designation, company, location))

h5('\n >>>> format() with index numbers')
info = 'hey i work for {1} in {0} as {2}'
h6(info.format(location, company, designation))

h5('\n >>>> format() with missing index numbers, means not giving all the index')
h6('>>>> Error: cannot switch from manual field specification to automatic field numbering')
# info1 = 'hey i work for {1} in {} as {}'
# print(info1.format(location, company, designation))
# print('''>>>> Below String code throws Error: g\n
# hey i work for {1} in {} as {}\nthrows: Value
# Error: cannot switch from manual field specification to automatic field numbering
# '''.format(location, company, designation))