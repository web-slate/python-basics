# python module.py data_types/boolean/basics.py
# python -m data_types.boolean.basics data_types/boolean/basics.py

import data_types.commonUtils as utils

utils.print_h1('Boolean Basics')

show_gender = False
actively_looking_for_job = True

utils.print_blockquote([
  'Can Show Gender details in general? ' +
  'No' if show_gender == False else 'Yes',
  'Are you looking for job? ' + 'Yes' if actively_looking_for_job == True else 'No',
  'True is treated as the integer 1 print(True == 1)   # Outputs: True ',
  'False is treated as the integer print(False == 0)   # Outputs: True'
])

utils.print_blockquote([
  'Arithmetic with booleans',
  'print(True + True)  # Outputs: 2 (equivalent to 1 + 1)',
  'print(True * 10)    # Outputs: 10 (equivalent to 1 * 10)',
])

post_graduated = False

utils.print_blockquote([
  'I have variable called post_graduated set to False'
  'Trying to delete post_graduated by `del post_graduated` ',
  'Try to print (print(post_graduated)) then system throws NameError: name post_graduated is not defined',
  'Use Try/Catch to make sure if its deleted '
])

del post_graduated

# Throws NameError: name post_graduated is not defined
# print(post_graduated)

try:
    print(post_graduated)  # Try to access the variable
except NameError:
    utils.print_span("post_graduated has been deleted.")


