# python module.py data_types/boolean/basics.py
# python -m data_types.boolean.basics data_types/boolean/basics.py

import data_types.commonUtils as utils

utils.print_h1('Boolean Basics')

show_gender = False
actively_looking_for_job = True

utils.print_blockquote([
    'Can Show Gender details in general? ' + 'No' if show_gender == False else 'Yes',
    'Are you looking for job? ' + 'Yes' if actively_looking_for_job == True else 'No'
])