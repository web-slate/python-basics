from utilities.testUtils import solution_title, print_and_assert_new, getTestResult
from utilities.commonUtils import timeComplexity, spaceComplexity

print('\n >>> 65. Valid Number')
print('''
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
''')

class problemName(object):
    def quick(self, s):
        pass
    def brute_force(self, s):
        pass
    def sub_optimal(self, s):
        pass
    def optimal(self, s):
        pass

# Parameters and Expected Values.
param1 = '0'
param11 = 'param11'
expect1 = True

param2 = 'e'
param22 = 'param22'
expect2 = False

param3 = '.'
param33 = 'param33'
expect3 = False

solution = problemName()
solution_title('ProblemName - Quick One')
print_and_assert_new(solution.quick, param1, expected=expect1)
print_and_assert_new(solution.quick, param2, expected=expect2)
print_and_assert_new(solution.quick, param3, expected=expect3)
getTestResult('ProblemName - Quick One')

timeComplexity('O(n)', 'desc_goes_here')
spaceComplexity('O(n)', 'desc_goes_here')

solution_title('ProblemName - Brute Force')
print_and_assert_new(solution.brute_force, param1, expected=expect1)
print_and_assert_new(solution.brute_force, param2, expected=expect2)
print_and_assert_new(solution.brute_force, param3, expected=expect3)
getTestResult('ProblemName - Brute Force')

timeComplexity('O(n)', 'desc_goes_here')
spaceComplexity('O(n)', 'desc_goes_here')

solution_title('ProblemName - Sub Optimal')
print_and_assert_new(solution.timeOptimized, param1, expected=expect1)
print_and_assert_new(solution.timeOptimized, param2, expected=expect2)
print_and_assert_new(solution.timeOptimized, param3, expected=expect3)
getTestResult('ProblemName - Sub Optimal')

timeComplexity('O(n)', 'desc_goes_here')
spaceComplexity('O(n)', 'desc_goes_here')

solution_title('ProblemName - Optimal')
print_and_assert_new(solution.timeOptimized, param1, expected=expect1)
print_and_assert_new(solution.timeOptimized, param2, expected=expect2)
print_and_assert_new(solution.timeOptimized, param3, expected=expect3)
getTestResult('ProblemName - Optimal')

timeComplexity('O(n + m)', 'desc_goes_here')
spaceComplexity('O(n + m)', 'desc_goes_here')