import data_types.commonUtils as utils

utils.print_h1('String Basics Example')

language = 'Python'

mid_index = (len(language) // 2) - 1 # decrement by 1 since length is 6 and index from 0 - 5

utils.print_ordered_list([
  f'Finding Length using len(str): "{language}" is , {len(language)}',
  f'Middle character index of "{language}" is {mid_index} and char is {language[mid_index]} Using ',
  f'6 different ways of String concatenations (+, %, join, format, fstring, += Operator)',
  f'6 different ways of String Substring (slicing, find, index, regEx, strip, partition)'
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


substring_methods = [
    (" Approach", " Example Code", " Time Complexity", " Space Complexity"),
    (" Slicing", " 'Python'[1:4]", " O(k)", " O(k)"),
    (" str.split() & Indexing", " 'a,'.split(',')[1]", " O(n)", " O(n)"),
    (" str.find() or str.index() & Slicing", " s = 'P'; s[s.find('th'):]", " O(n)", " O(k)"),
    (" Regular Expression (re module)", " re.search('y.*o', 'Python').group()", " O(n)", " O(k)"),
    (" str.strip()/str.rstrip()/str.lstrip()", "' P '.strip()", " O(n)", " O(n)"),
    (" str.partition() & Indexing", " 'P'.partition('-')[0]", " O(n)", " O(n)")
]

utils.print_tabular_list(substring_methods)


word = 'An Apple'
utils.print_h6('We have word variable hold "An Apple"')
utils.print_span('Using Slicing: [start:stop:step]', word[3:])
utils.print_span('Using Split Function returns list:', word.split(' ')[1])
utils.print_span('Using find() return index, -1 when not found:', word[word.find('A'):])
utils.print_span('Using index() return index, ValueError when not found:', word[word.index(' A'):])
import re
utils.print_span('Using Regular Expression():', re.search('Ap.*e', word).group())
utils.print_span('Using strip():', word.strip('An '))
utils.print_span('Using partition Function returns list:', word.partition(' ')[1])

def char_and_ascii(s):
    return [(char, ord(char)) for char in s]

# Example usage
result = char_and_ascii("An Apple")
print(result)