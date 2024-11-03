from utilities.testUtils import solution_title, print_and_assert_new, getTestResult
from utilities.commonUtils import timeComplexity, spaceComplexity

print('\n >>> 67. Add Binary')
print('''
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
''')

class AddBinary(object):
    def quick(self, a, b):
      sum = int(a, 2) + int(b, 2)
      return bin(sum)[2:]
    def brute_force(self, a, b):
      result, carry, i, j = "", 0, len(a) - 1, len(b) - 1

      while i >= 0 or j >= 0 or carry:
          total = carry
          if i >= 0:
              total += int(a[i])
              i -= 1
          if j >= 0:
              total += int(b[j])
              j -= 1
          carry = total // 2
          result = str(total % 2) + result

      return result
    def sub_optimal(self, a, b):
      x, y = int(a, 2), int(b, 2)
      while y:
          answer = x ^ y
          carry = (x & y) << 1
          x, y = answer, carry
      return bin(x)[2:]
    def optimal(self, a, b):
      result, carry = "", 0
      p1, p2 = len(a) - 1, len(b) - 1

      while p1 >= 0 or p2 >= 0 or carry:
          if p1 >= 0:
              carry += int(a[p1])
              p1 -= 1
          if p2 >= 0:
              carry += int(b[p2])
              p2 -= 1
          carry, bit = divmod(carry, 2)
          result = str(bit) + result

      return result

# Parameters and Expected Values.
param1 = '11'
param11 = '1'
expect1 = '100'

param2 = '1010'
param22 = '1011'
expect2 = '10101'

param3 = '0'
param33 = '0'
expect3 = '0'

solution = AddBinary()
solution_title('AddBinary - Quick One')
print_and_assert_new(solution.quick, param1, param11, expected=expect1)
print_and_assert_new(solution.quick, param2, param22, expected=expect2)
print_and_assert_new(solution.quick, param3, param33, expected=expect3)
getTestResult('AddBinary - Quick One')

timeComplexity('O(N + M)', 'where N and M are the lengths of strings a and b, respectively. The conversion functions (int and bin) run in linear time relative to the length of the input strings.')
spaceComplexity('O(1)', 'as we only use a fixed amount of extra space.')

solution_title('AddBinary - Brute Force')
print_and_assert_new(solution.brute_force, param1, param11, expected=expect1)
print_and_assert_new(solution.brute_force, param2, param22, expected=expect2)
print_and_assert_new(solution.brute_force, param3, param33, expected=expect3)
getTestResult('AddBinary - Brute Force')

timeComplexity('O(max(N, M))', 'where N and M are the lengths of strings a and b.')
spaceComplexity('O(max(N, M))', 'as we store the result which can be as long as the longer string plus one for the carry bit.')

solution_title('AddBinary - Sub Optimal using Bit Manipulation')
print_and_assert_new(solution.sub_optimal, param1, param11, expected=expect1)
print_and_assert_new(solution.sub_optimal, param2, param22, expected=expect2)
print_and_assert_new(solution.sub_optimal, param3, param33, expected=expect3)
getTestResult('AddBinary - Sub Optimal using Bit Manipulation')

timeComplexity('O(N + M)', 'depends on the lengths of the binary representations.')
spaceComplexity('O(1)', 'space used does not depend on the input size.')

solution_title('AddBinary - Optimal using Two-Pointer Approach')
print_and_assert_new(solution.optimal, param1, param11, expected=expect1)
print_and_assert_new(solution.optimal, param2, param22, expected=expect2)
print_and_assert_new(solution.optimal, param3, param33, expected=expect3)
getTestResult('AddBinary - Optimal using Two-Pointer Approach')

timeComplexity('O(max(N, M))', 'optimal because we have to inspect each character of both strings in the worst case.')
spaceComplexity('O(max(N, M))', 'resulting string size will be at most max(N, M) + 1')