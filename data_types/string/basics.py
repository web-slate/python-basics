import data_types.commonUtils as utils

utils.print_h1('String Basics Example')

language = 'Python'

mid_index = (len(language) // 2) - 1 # decrement by 1 since length is 6 and index from 0 - 5

utils.print_ordered_list([
  f'Finding Length using len(str): "{language}" is , {len(language)}',
  f'Middle character index of "{language}" is {mid_index} and char is {language[mid_index]} Using ',
  f'6 different ways of String concatenations (+, %, join, format, fstring, += Operator)',
  f'6 different ways of String Substring (slicing, find, index, regEx, strip, partition)'
  f'7 different ways of Contains String check (in, find, index, count, regEx, startswith, endswith)'
  f'In Python, strings are immutable in nature'
])

greet = 'Hello'
name = 'Venkat.R'

print('\n')
six_ways_of_string_concatenation = [
    (" Approach", " Example Code", " Time Complexity", " Space Complexity"),
    (" Using + Operator", " greet + name", " O(n + m)", " O(n + m)"),
    (" Using % Operator", " '%s%s' % (greet, name)", " O(n + m)", " O(n + m)"),
    (" Using join() Method", " ''.join([greet, name])", " O(n)", " O(n)"),
    (" Using format() Method", " '{}{}'.format(greet, name)", " O(n + m)", " O(n + m)"),
    (" Using f-String (Python 3.6+)", " f'{greet}{name}'", " O(n + m)", " O(n + m)"),
    (" Using String Concatenation with +=", " greet += name", " O(n*m)", " O(n*m)")
]

utils.print_tabular_list(six_ways_of_string_concatenation)

utils.print_h6('We have greet variable hold "Hello" and name hold "Venkat.R"')
concatenated_by_plus_operator = greet + ' ' + name
utils.print_span('Using + Operator: ', concatenated_by_plus_operator)
utils.print_span('Using String join method: ', ''.join([greet, ' ', name]))
utils.print_span('Using % Operator: ', "%s %s" % (greet, name))
utils.print_span('Using String format() Method: ', '{} {}'.format(greet, name))
utils.print_span('Using f-String (Python 3.6+): ', f'{greet} {name}')
greet += name
utils.print_span('Using String Concatenation with +=: ', greet, '\n')

six_ways_of_substring_methods = [
    (" Approach", " Example Code", " Time Complexity", " Space Complexity"),
    (" Slicing", " 'Python'[1:4]", " O(k)", " O(k)"),
    (" str.split() & Indexing", " 'a,'.split(',')[1]", " O(n)", " O(n)"),
    (" str.find() or str.index() & Slicing", " s = 'P'; s[s.find('th'):]", " O(n)", " O(k)"),
    (" Regular Expression (re module)", " re.search('y.*o', 'Python').group()", " O(n)", " O(k)"),
    (" str.strip()/str.rstrip()/str.lstrip()", "' P '.strip()", " O(n)", " O(n)"),
    (" str.partition() & Indexing", " 'P'.partition('-')[0]", " O(n)", " O(n)")
]

utils.print_tabular_list(six_ways_of_substring_methods)

word = 'An Apple'
utils.print_h6('We have word variable hold "An Apple"')
utils.print_span('Using Slice Notation: [start:stop:step]', word[3:])
slice_object = slice(3, None)
utils.print_span('Using Slice Object (it is flexibility assiging as variable, argument, dynamic slicing):', word[slice_object])
utils.print_span('Using split() split multiple occurrence, returns list: ', word.split(' ')[1])
utils.print_span('Using partition() split first occurrence, returns tuple: ', word.partition(' ')[1])
utils.print_span('Using find() return index, -1 when not found:', word[word.find('A'):])
utils.print_span('Using index() return index, ValueError when not found:', word[word.index(' A'):])
import re
utils.print_span('Using Regular Expression():', re.search('Ap.*e', word).group())
utils.print_span('Using strip():', word.strip('An'))

seven_ways_of_contain_check = [
    (" Approach", " Example Code", " Time Complexity", " Space Complexity"),
    (" in Operator", " 'apple' in 'apple pie'", " O(n)", " O(1)"),
    (" str.find() Method", " 'apple pie'.find('apple') != -1", " O(n)", " O(1)"),
    (" str.index() Method", " try: 'apple'.index('pl') except ValueError: pass", " O(n)", " O(1)"),
    (" str.count() Method", " 'apple'.count('pl') > 0", " O(n)", " O(1)"),
    (" Regular Expression (re module)", " import re; bool(re.search('pl', 'apple'))", " O(n)", " O(1)"),
    (" str.startswith() Method", " 'apple pie'.startswith('apple')", " O(k)", " O(1)"),
    (" str.endswith() Method", " 'apple pie'.endswith('pie')", " O(k)", " O(1)")
]

utils.print_tabular_list(seven_ways_of_contain_check)

utils.print_span('Most Efficient Method is `in`: apple pie contain apple?', 'apple' in 'apple pie')

seven_ways_of_string_comparison_methods = [
    (" Approach", " Example Code", " Time Complexity", " Space Complexity"),
    (" Equality Operator ==", " str1 == str2", " O(n)", " O(1)"),
    (" str.casefold() for Case-Insensitive Comparison", " str1.casefold() == str2.casefold()", " O(n)", " O(n)"),
    (" str.lower() or str.upper() for Case-Insensitive Comparison", " str1.lower() == str2.lower()", " O(n)", " O(n)"),
    (" locale.strcoll() for Locale-Aware Comparison", " import locale; locale.strcoll(str1, str2)", " Locale-Specific", " Locale-Specific"),
    (" Comparing with str.startswith() or str.endswith()", " str1.startswith(str2) or str1.endswith(str2)", " O(k)", " O(1)"),
    (" Lexicographical Comparison using > or <", " str1 > str2 or str1 < str2", " O(n)", " O(1)"),
    (" Identity Operator Not for value is", " str1 is str2", " O(1)", " O(1)")
]

utils.print_tabular_list(seven_ways_of_string_comparison_methods)

def char_and_ascii(s):
    return [(char, ord(char)) for char in s]

# Example usage
result = char_and_ascii("An Apple")
print(result)

str1 = "apple"
str2 = "apple pie"

utils.print_h6('Compare the strings lexicographically str1, str2 ', str1, str2)
if str1 < str2:
    utils.print_span(f"{str1} comes before {str2} lexicographically")
elif str1 > str2:
    utils.print_span(f"{str1} comes after {str2} lexicographically")
else:
    utils.print_span("The strings are equal")   
    
char_conversion_functions = [
    (" Function", " Description", " Example Input", " Example Output"),
    (" `ord()`", " Converts a character to its Unicode code point.", " `ord('A')`", " 65"),
    (" `chr()`", " Converts a Unicode code point to its character.", " `chr(65)`", " 'A'"),
    (" `hex()`", " Converts an integer to a lowercase hexadecimal string.", " `hex(255)`", " '0xff'"),
    (" `bin()`", " Converts an integer to a binary string.", " `bin(7)`", " '0b111'"),
    (" `int()`", " Converts a string or number to an integer (base 10 by default, can specify base).", " `int('0xff', 16)`", " 255"),
    (" `format()`", " Formats a number into a string, can specify format (like hexadecimal).", " `format(255, 'x')`", " 'ff'")
]

utils.print_tabular_list(char_conversion_functions)

utils.print_h6('Palindrome Check using StringIO')

import io

def is_palindrome(s):
    # Create a StringIO object to manipulate the string
    buffer = io.StringIO()

    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Write the string in reverse to the buffer
    for char in reversed(s):
        buffer.write(char)

    # Get the reversed string from the buffer
    reversed_s = buffer.getvalue()

    # Close the buffer
    buffer.close()

    # Check if the original string and the reversed string are the same
    return s == reversed_s

# Example usage
utils.print_span("'A man a plan a canal Panama' is", is_palindrome("A man a plan a canal Panama"))  # True
utils.print_span("'Hello is'", is_palindrome("Hello"))                      # False


print('''
+----------------------+------------------------+
|       Category       |      Decimal Range     |
+----------------------+------------------------+
|      Basic Latin     |        0 to 127        |
|         Latin-1      |       128 to 255       |
|    Latin-Extended    |       256 to 383       |
|         Greek        |       913 to 969       |
|       Cyrillic       |      1024 to 1279      |
|        Symbols       |      8192 to 11263     |
|   Numbers & Digits   |        48 to 57        |
|       Exponents      |      8304 to 8343      |
|        Complex       |    119808 to 120831    |
|      Upper Case      |        65 to 90        |
|      Lower Case      |        97 to 122       |
+----------------------+------------------------+

''')


def get_unicode_characters(string):
    unicode_characters = []
    for char in string:
        unicode_characters.append(ord(char))
    return unicode_characters
  
char = 'A'
print(char, get_unicode_characters(char))