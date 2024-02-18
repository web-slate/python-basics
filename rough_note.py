employee = {
    'name': 'Alice',
    'age': 30,
    'items': ['book', 'pen', 'notebook'],
    'nested_dict': {
        'key1': 'value1',
        'key2': 'value2'
    }
}

# for key in employee:
#   print('key: ', key)

# for key, value in employee.items():
#   print(key, ': ', value);

# for index, key in enumerate(employee):
#   print(index, ': ', key, employee.get(key));

# for key in employee.keys():
#   print('key: ', key)
# print(employee.keys());

# for value in employee.values():
#   print('value: ', value)
# print(list(employee.values()));

# import math


# def sin(x):
#     if(x * 2 == pi):
#         return 0.9999
#     else:
#         return None

# pi = math.pi

# print('1.57: ', sin(1.57))
# print('1', sin(1))
# print('math.pi: ', math.pi)

# def is_palindrome_optimal(text):
#   """
#   Checks if a text is a palindrome using an optimal approach.

#   Args:
#     text: The text to check.

#   Returns:
#     True if the text is a palindrome, False otherwise.
#   """
#   left, right = 0, len(text) - 1
#   while left < right:
#     if text[left] != text[right]:
#       return False
#     left += 1
#     right -= 1
#   return True

# print('racecar: ', is_palindrome_optimal("racecar"))  # True
# print('hello: ', is_palindrome_optimal("hello"))  # False
# print('A man, a plan, a canal: Panama: ', is_palindrome_optimal("A man, a plan, a canal: Panama"))

# def is_palindrome_brute_force(text):
#   """
#   Checks if a text is a palindrome using a brute force approach.

#   Args:
#     text: The text to check.

#   Returns:
#     True if the text is a palindrome, False otherwise.
#   """
#   left, right = 0, len(text) - 1
#   while left < right:
#     if text[left].lower() != text[right].lower():  # Ignore case
#       return False
#     left += 1
#     right -= 1
#   return True

# # Test the function with different inputs.
# print('racecar: ', is_palindrome_brute_force("racecar"))  # True
# print('hello: ', is_palindrome_brute_force("hello"))  # False
# print('A man, a plan, a canal: Panama: ', is_palindrome_brute_force("A man, a plan, a canal: Panama"))  # True