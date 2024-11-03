# python -m data_types.commonUtils data_types/tuples/basics.py
# python -m data_types.tuples.basics data_types/tuples/basics.py

import data_types.commonUtils as utils

utils.print_h1('Tuple Basics')
utils.print_ordered_list([
    'Tuple is Ordered (order will not be changed)',
    'Tuple is Immutable',
    'Convert to List for Mutation (Changing / Removing)'
])


fruits = ('apple','banana', 'guava')
subjects = ('english', 'science', 'maths', 'scoial')
daily_cycle = ('morning', 'afternoon', 'dinner')
exam_result = ('english', 80)


fruit_list = list(fruits)

fruits_subjects = fruits + subjects
print(fruits_subjects)

'''
convert to the list
[].(fruits)
need to check whether order in place
'''