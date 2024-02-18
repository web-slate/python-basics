from utilities.testUtils import solution_title, reason_points, print_and_assert_new, getTestResult
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
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return s == ''
    def brute_force(self, s):
        # Using replace function.
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
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

param4 = '{[()]}'
expect4 = True

param5 = '{}()'
expect5 = True

param6 = '{(})'
expect6 = False

param7 = ')'
expect7 = False

solution = ValidParenthesis()
solution_title('Valid Parenthesis - Quick One')
reason_points('''
1. Uses a straightforward loop and string replacement to solve the problem.
2. lacks the sophistication of using data structures like stacks.
''')
print_and_assert_new(solution.quick, param1, expected=expect1)
print_and_assert_new(solution.quick, param2, expected=expect2)
print_and_assert_new(solution.quick, param3, expected=expect3)
print_and_assert_new(solution.quick, param4, expected=expect4)
print_and_assert_new(solution.quick, param5, expected=expect5)
print_and_assert_new(solution.quick, param6, expected=expect6)
print_and_assert_new(solution.quick, param7, expected=expect7)
getTestResult('Valid Parenthesis - Quick One')

timeComplexity('O(n^3)', 'Multiple passes through the string, each of which could be O(n^2)')
spaceComplexity('O(n)', 'Need to store the entire string')

solution_title('Valid Parenthesis - Brute Force')
reason_points('''
1. It involves repeatedly scanning and modifying the string without any sophisticated method.
2. It does redundant work for each pair of brackets.
''')
print_and_assert_new(solution.brute_force, param1, expected=expect1)
print_and_assert_new(solution.brute_force, param2, expected=expect2)
print_and_assert_new(solution.brute_force, param3, expected=expect3)
print_and_assert_new(solution.brute_force, param4, expected=expect4)
print_and_assert_new(solution.brute_force, param5, expected=expect5)
print_and_assert_new(solution.brute_force, param6, expected=expect6)
print_and_assert_new(solution.brute_force, param7, expected=expect7)
getTestResult('Valid Parenthesis - Brute Force')

timeComplexity('O(n^3)', 'Each pair of brackets, we potentially scan through the entire string (O(n))')
spaceComplexity('O(n)', 'In Worst case, might need to store the entire string in memory.')

solution_title('Valid Parenthesis - Sub Optimal')
reason_points('''
1. Efficient than the brute force approach.
2. Not optimal because it might involve storing all characters in the stack in worst case.
''')
print_and_assert_new(solution.sub_optimal, param1, expected=expect1)
print_and_assert_new(solution.sub_optimal, param2, expected=expect2)
print_and_assert_new(solution.sub_optimal, param3, expected=expect3)
print_and_assert_new(solution.sub_optimal, param4, expected=expect4)
print_and_assert_new(solution.sub_optimal, param5, expected=expect5)
print_and_assert_new(solution.sub_optimal, param6, expected=expect6)
print_and_assert_new(solution.sub_optimal, param7, expected=expect7)
getTestResult('Valid Parenthesis - Sub Optimal')

timeComplexity('O(n)', 'we go through each character in the string exactly once.')
spaceComplexity('O(n)', 'all characters are opening brackets, and they all get pushed onto the stack.')

solution_title('Valid Parenthesis - Optimal')
reason_points('''
1. Efficiently verifies the string with a single pass
2. Space usage is as minimal
''')
print_and_assert_new(solution.optimal, param1, expected=expect1)
print_and_assert_new(solution.optimal, param2, expected=expect2)
print_and_assert_new(solution.optimal, param3, expected=expect3)
print_and_assert_new(solution.optimal, param4, expected=expect4)
print_and_assert_new(solution.optimal, param5, expected=expect5)
print_and_assert_new(solution.optimal, param6, expected=expect6)
print_and_assert_new(solution.optimal, param7, expected=expect7)
getTestResult('Valid Parenthesis - Optimal')

timeComplexity('O(n)', 'we scan each character once.')
spaceComplexity('O(n)', 'O(n) for the stack and O(1) for the hashmap')
