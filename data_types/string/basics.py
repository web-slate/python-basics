import data_types.commonUtils as utils

utils.print_h1('String Basics Example')

language = 'Python'

mid_index = (len(language) // 2) - 1 # decrement by 1 since length is 6 and index from 0 - 5

utils.print_ordered_list([
  f'Finding Length using len(str): "{language}" is , {len(language)}',
  f'Middle character index of "{language}" is {mid_index} and char is {language[mid_index]} Using ',
  f'6 different ways of String concatenations (+, %, join, format, fstring, += Operator)'
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