# python module.py data_types/dictionaries/basics.py
# python -m data_types.dictionaries.basics data_types/dictionaries/basics.py

import data_types.commonUtils as utils

utils.print_h1('Dictionary Basics')
utils.print_ordered_list([
    'Dictionary is Key pair values, Ordered (order will not be changed)',
    'Dictionary is Changeable',
    'Dictionary will not contain duplicate key',
    'In Python 3.6, is unordered Python 3.7 is Ordered',
    'Its good for fast lookups',
    'Insertions, and deletions by using keys',
    'Every Keys will be hashed using Hashing Algorithm'
])

utils.print_h3('Hashing Algorithm by Data Types')
hashing_algorithm_by_data_types = [
    (" Key Type", " Hashing Algorithm/Method"),
    (" String", " SipHash variant"),
    (" Integer", " Identity hash (value itself with exceptions)"),
    (" Float", " Based on internal representation"),
    (" Boolean", " Same as Integer (True is 1, False is 0)"),
    (" Tuple", " Combination of hashes of contents"),
    (" Custom Object", " Defined by `__hash__` method (if implemented)"),
    (" None", " Fixed hash value")
]

# Print the table
utils.print_tabular_list(hashing_algorithm_by_data_types)

employee = {
    'name': 'Alice',
    'age': 30,
    'items': ['book', 'pen', 'notebook'],
    'nested_dict': {
        'key1': 'value1',
        'key2': 'value2'
    }
}

utils.print_blockquote([
    'Lets take a example of below dictionary for employee.'
])

utils.pretty_json(employee)

utils.print_blockquote([
    'Lets add list and tuple as key and printing the employee again'
])

marks = [100,70,90]
subjects = ('english', 70)
# employee[marks] = 10 #throws TypeError: unhashable type: 'list'
employee[subjects] = 20

utils.pretty_json(employee)

utils.print_h1('Access')
utils.print_blockquote([
    'By Key: employee[\'name\']: ' + employee['name'],
    
    'By get method: employee.get(\'name\'): ' + employee.get('name')
])


utils.print_h1('Exist Check / Search')

name_key_exist = 'Yes' if('name' in employee) else 'No'
name_key_exist_key_list = 'Yes' if('not_exist_key' in employee.keys()) else 'No'

try_catch_block_exist_check = ''

try:
    value = employee['not_exist_key']
    try_catch_block_exist_check = 'Yes'
    # Key exists
except KeyError:
    try_catch_block_exist_check = 'No, got Key Error'
    # Key doesn't exist

utils.print_blockquote([
    'By IN Operator: (\'name\' in employee): ' + name_key_exist,
    'By keys() Method: (\'notname\' in employee.keys()): ' + name_key_exist_key_list,
    'By Try Catch Block (not recommended): ' + try_catch_block_exist_check
])

utils.print_h1('Add / Insert')

employee['designation'] = 'Software Engineer'
employee.update({
  'age': '34'
})
utils.print_blockquote([
    'By key-value assignment: employee[\'designation\'] = \'Software Engineer\': ' + employee['designation'],
    'By key-value assignment: employee.update({\'age\': \'34\'}): ' + employee['age'],
])


utils.print_h1('Remove / Delete')
utils.print_h1('Iteration')
