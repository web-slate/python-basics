# employee = {
#     'name': 'Alice',
#     'age': 30,
#     'items': ['book', 'pen', 'notebook'],
#     'nested_dict': {
#         'key1': 'value1',
#         'key2': 'value2'
#     }
# }

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

n = 2
arr_1 = [2, 1]
output_1 = [2, 2]
arr_2 = [1, 2]
output_2 = [1, 1]

def findSignatureCounts_1(arr):
  n = len(arr)
  output = [0] * n

  for i in range(n):
    signatures = 0
    index = i
    for _ in range(n):
      signatures += 1
      print(i, _)
      index = arr[index] - 1
      print('   >', index, arr[index])
      if (index == i):
        break

    output[i] = signatures
  return output

print(arr_1, findSignatureCounts_1(arr_1) == output_1)
print(arr_2, findSignatureCounts_1(arr_2) == output_2)


    # n = len(arr)
    # signatures = [0] * n
    # visited = [False] * n

    # for i in range(n):
    #     if not visited[i]:
    #         count = 0
    #         j = i
    #         while not visited[j]:
    #             visited[j] = True
    #             j = arr[j] - 1
    #             count += 1
    #         while arr[j] - 1 != i:
    #             signatures[j] = count
    #             j = arr[j] - 1
    #         signatures[j] = count
    # return signatures