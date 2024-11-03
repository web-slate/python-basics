# python module.py operators/bit_wise/shift_left/basics.py

import data_types.commonUtils as utils

utils.print_h1('Shift Left Basics')

utils.print_h2('Shift Left can be used in ..')
utils.print_ordered_list([
    'Efficient Multiplication',
    'Power of Two Operations',
    'Setting and Clearing Bits'
])

utils.print_h2('Using Leet code problems ..')
utils.print_ordered_list([
    'Two Sum',
    'Valid Parentheses',
    'Maximum Subarray',
    'LRU Cache',
    'Middle of Linked List'
])

n = 1
original_value = 3
# original_value * (2^n)
multiplication_without_shift_operator = original_value * 2**n
multiplication_with_shift_left_operator = original_value << n

print('\n')
print('n is', n, ' = multiplication_without_shift_operator: ', multiplication_without_shift_operator)
print('n is', n, ' = multiplication_with_shift_left_operator: ', multiplication_with_shift_left_operator)


m = 2
multiplication_without_shift_operator_m = original_value * 2**m
multiplication_with_shift_operator_m = original_value << m

print('m is', m, ' = multiplication_without_shift_operator_m: ', multiplication_without_shift_operator_m)
print('m is', m, ' = multiplication_with_shift_operator_m: ', multiplication_with_shift_operator_m)

print('''
| Decimal | Binary |
|---------|--------|
| 0       | 0000   |
| 1       | 0001   |
| 2       | 0010   |
| 3       | 0011   |
| 4       | 0100   |
| 5       | 0101   |
| 6       | 0110   |
| 7       | 0111   |
| 8       | 1000   |
| 9       | 1001   |
| 10      | 1010   |
| 11      | 1011   |
| 12      | 1100   |
''')