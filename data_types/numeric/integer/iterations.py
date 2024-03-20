# python module.py data_types/numeric/integer/iterations.py
# python -m data_types.numeric/integer data_types/numeric/integer/iterations.py

import data_types.commonUtils as utils

utils.print_h1('Integer Iterations')

utils.print_blockquote([
  'Types are short, long, int32, int64',
  'Binary, Octal, and Hexadecimal Integers',
  'Underscores in Numeric Literals (Python 3.6+) ex: large_num = 1_000_000'
])

salary = 9000
increment = 500

print('\n >>>> Iterate using for loop with type casting')
print(' >>>> Follow this approach on demand and Its not recommended')
for text in str(salary):
    print(text)
    
# print('\n >>>> Iterate using while loop')
# def iterateInteger(integer_number):
#     stack = []
#     while integer_number > 0:
#         digit = integer_number % 10
#         stack.append(digit)
#         integer_number //= 10
    
#     while stack:
#         print(stack.pop())
            
# iterateInteger(salary)

# def iterateInteger(integer_number):
#     stack = []
#     while integer_number > 0:
#         digit = integer_number % 10
#         stack.append(digit)
#         integer_number //= 10
    
#     while stack:
#         print(stack.pop())

def find_digit_position(number, digit_to_find):
    original_number = number
    position = 1
    while number >= 10:
        if number % 10 == digit_to_find:
            return len(str(original_number)) - position + 1
        number //= 10
        position += 1
    # Check the last digit
    return 1 if number == digit_to_find else -1

# Test the function with the number 9000 and digit 9
find_digit_position_number = 8778890942
find_number = 0
print(f'Position of {find_number} from {find_digit_position_number} is ', find_digit_position(find_digit_position_number, find_number))
