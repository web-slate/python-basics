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

# n = 2
# arr_1 = [2, 1]
# output_1 = [2, 2]
# arr_2 = [1, 2]
# output_2 = [1, 1]

# def findSignatureCounts_1(arr):
#   n = len(arr)
#   output = [0] * n

#   for i in range(n):
#     signatures = 0
#     index = i
#     for _ in range(n):
#       signatures += 1
#       print(i, _)
#       index = arr[index] - 1
#       print('   >', index, arr[index])
#       if (index == i):
#         break

#     output[i] = signatures
#   return output

# print(arr_1, findSignatureCounts_1(arr_1) == output_1)
# print(arr_2, findSignatureCounts_1(arr_2) == output_2)


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
    
    
# def is_palindrome(s):
#     return s == s[::-1]

# def validPalindromeBruteForce(s):
#     for i in range(len(s)):
#         print('s[:i]: ', s[:i])
#         print('s[i + 1:]: ', s[i + 1:])
#         t = s[:i] + s[i + 1:]
#         if is_palindrome(t):
#             return True
#     return is_palindrome(s)  
  
# v = 'acbca'
# def iterateString(s):
#   half = (len(s)-1)//2;
#   for i in range(0, half):
#     print(s[i], s[i+1], s[i+2])

# print(v, validPalindromeBruteForce(v))
# iterateString(v)
# print(v, iterateString(v))

# zeros_count = 0
# while(zeros_count < 4):
#   print(zeros_count)
#   zeros_count += 1
# print('==========================================')

# moved_one = [0,1,0,3,12]
# non_zeros = [1, 3, 12]
# for i in range(len(non_zeros),len(moved_one)):
#   print(i)

# print('==========================================')
# j = 3
# while(j < 5):
#   print(j)
#   j += 1
# print('==========================================')
# for i in range(j,5):
#   print(i)

# k = 3
# while(k >= 0):
#   print(k)
#   k -= 1

# print('''
# # Given a string representing an arithmetic expression with only addition and
# # multiplication operators, return the result of the calculation.

# # Examples:
# # eval("2*3+4") -> 10
# # eval("1+2*3*4+5") -> 30  
# ''')

# def eval_expression_optimal(expr):
#     num = 0
#     current_mult = 1
#     total_sum = 0
    
#     for char in expr:
#         if char.isdigit():
#             num = num * 10 + int(char)
#         elif char == '+':
#             total_sum += current_mult * num
#             num = 0
#             current_mult = 1
#         elif char == '*':
#             if num:
#                 current_mult *= num
#                 num = 0
    
#     return total_sum + current_mult * num

# s1 = '2*3+4'
# s2 = '1+2*3*4+5'
# s3 = '1000+2*32*412+5'
# print(s1, '=', eval_expression_optimal(s1))
# print(s2, '=', eval_expression_optimal(s2))
# print(s3, '=', eval_expression_optimal(s3))


# import math


# name = "   praveen    "
# print('#' + name.lstrip().replace('p', 'Mr. P') + '#')

# 1 - 7
i = 11
# while(i <= 17):
#   print(i)
#   i+=1

# for i in range(90,80,-1):
#   print(i)
  
i = 90
while(i >= 81):
  print(i)
  i-=1