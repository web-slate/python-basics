from utilities.testUtils import solution_title, print_and_assert_new, getTestResult
from utilities.commonUtils import timeComplexity, spaceComplexity

print('\n >>> 20. Valid Parentheses')
print('''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
''')

class ValidParenthesis(object):
    def quick(self, s):
         # Using length and replace function.
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            s = s.replace(param1, '').replace('{}', '').replace('[]', '')
        return s == ''
    def brute_force(self, s):
        # Using replace function.
        while param1 in s or '{}' in s or '[]' in s:
            s = s.replace(param1, '').replace('{}', '').replace('[]', '')
        return s == ''
    def sub_optimal(self, s):
        # Using Stack DS through List.
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] != '(':
                    return False
                if char == '}' and stack[-1] != '{':
                    return False
                if char == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        return not stack
    def optimal(self, s):
      # Using Hash Map.
      stack = []
      bracket_map = {')': '(', '}': '{', ']': '['}
      for char in s:
          if char in bracket_map.values():
              stack.append(char)
          elif char in bracket_map.keys():
              if stack == [] or bracket_map[char] != stack.pop():
                  return False
          else:
              return False
      return stack == []

# Parameters and Expected Values.
param1 = '()'
expect1 = True

param2 = '()[]{}'
expect2 = True

param3 = '(]'
expect3 = False

solution = ValidParenthesis()
solution_title('Valid Parenthesis - Quick One')
print_and_assert_new(solution.quick, param1, expected=expect1)
print_and_assert_new(solution.quick, param2, expected=expect2)
print_and_assert_new(solution.quick, param3, expected=expect3)
getTestResult('Valid Parenthesis - Quick One')

timeComplexity('O(n^3)', 'desc goes here')
spaceComplexity('O(n)', 'desc goes here')

solution_title('Valid Parenthesis - Brute Force')
print_and_assert_new(solution.brute_force, param1, expected=expect1)
print_and_assert_new(solution.brute_force, param2, expected=expect2)
print_and_assert_new(solution.brute_force, param3, expected=expect3)
getTestResult('Valid Parenthesis - Brute Force')

timeComplexity('O(n)', 'desc goes here')
spaceComplexity('O(n)', 'desc goes here')

solution_title('Valid Parenthesis - Sub Optimal')
print_and_assert_new(solution.sub_optimal, param1, expected=expect1)
print_and_assert_new(solution.sub_optimal, param2, expected=expect2)
print_and_assert_new(solution.sub_optimal, param3, expected=expect3)
getTestResult('Valid Parenthesis - Sub Optimal')

timeComplexity('O(n)', 'desc goes here')
spaceComplexity('O(n)', 'desc goes here')

solution_title('Valid Parenthesis - Optimal')
print_and_assert_new(solution.optimal, param1, expected=expect1)
print_and_assert_new(solution.optimal, param2, expected=expect2)
print_and_assert_new(solution.optimal, param3, expected=expect3)
getTestResult('Valid Parenthesis - Optimal')

timeComplexity('O(n + m)', 'desc goes here')
spaceComplexity('O(n + m)', 'desc goes here')

# class ValidParenthesis:
#   def is_valid(self, x: str ):
#     stack = []
#     parenthesis = {'[' : ']', '(' : ')', '{' : '}'}
#     for char in x:
#       if char in parenthesis:
#         stack.append(parenthesis[char])
#       elif not stack or stack.pop() != char:
#         return False
#     return not stack
# a = ValidParenthesis()
# string_value = '()[(]'
# print(f"given string {string_value} is { 'valid ' if a.is_valid(string_value) else 'not valid '} paranthesis")
