from utilities.testUtils import solution_title, print_and_assert_new, getTestResult
from utilities.commonUtils import timeComplexity, spaceComplexity

print('\n >>> 680. Valid Palindrome II By Remove One Char')
print('''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
''')

class ValidPalindrome2ByRemoveOneChar(object):
    def quick(self, s):
        pass
    def brute_force(self, s):
        pass
    def sub_optimal(self, s):
        pass
    def optimal(self, s):
        pass

# Parameters and Expected Values.
param1 = 'aba'
expect1 = True

param2 = 'abca'
expect2 = True

param3 = 'abc'
expect3 = False

solution = ValidPalindrome2ByRemoveOneChar()
solution_title('ValidPalindrome2ByRemoveOneChar - Quick One by Initialize two pointers')
print_and_assert_new(solution.quick, param1, expected=expect1)
print_and_assert_new(solution.quick, param2, expected=expect2)
print_and_assert_new(solution.quick, param3, expected=expect3)
getTestResult('ValidPalindrome2ByRemoveOneChar - Quick One')

timeComplexity('O(n)', 'desc_goes_here')
spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('ValidPalindrome2ByRemoveOneChar - Brute Force')
# print_and_assert_new(solution.brute_force, param1, expected=expect1)
# print_and_assert_new(solution.brute_force, param2, expected=expect2)
# print_and_assert_new(solution.brute_force, param3, expected=expect3)
# getTestResult('ValidPalindrome2ByRemoveOneChar - Brute Force')

# timeComplexity('O(n)', 'desc_goes_here')
# spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('ValidPalindrome2ByRemoveOneChar - Sub Optimal')
# print_and_assert_new(solution.timeOptimized, param1, expected=expect1)
# print_and_assert_new(solution.timeOptimized, param2, expected=expect2)
# print_and_assert_new(solution.timeOptimized, param3, expected=expect3)
# getTestResult('ValidPalindrome2ByRemoveOneChar - Sub Optimal')

# timeComplexity('O(n)', 'desc_goes_here')
# spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('ValidPalindrome2ByRemoveOneChar - Optimal')
# print_and_assert_new(solution.timeOptimized, param1, expected=expect1)
# print_and_assert_new(solution.timeOptimized, param2, expected=expect2)
# print_and_assert_new(solution.timeOptimized, param3, expected=expect3)
# getTestResult('ValidPalindrome2ByRemoveOneChar - Optimal')

# timeComplexity('O(n + m)', 'desc_goes_here')
# spaceComplexity('O(n + m)', 'desc_goes_here')