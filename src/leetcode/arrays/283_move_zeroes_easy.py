from utilities.testUtils import solution_title, print_and_assert_reference, getTestResult
from utilities.commonUtils import timeComplexity, spaceComplexity

print('\n >>> 283. Move Zeroes')
print('''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
''')

class MoveZeroesItemInArrayToLast(object):
    def quick(self, nums):
      j = 0
      for num in nums:
          if num != 0:
              nums[j] = num
              j += 1
      for i in range(j, len(nums)):
          nums[i] = 0
    def brute_force(self, s):
        pass
    def sub_optimal(self, s):
        pass
    def optimal(self, s):
        pass

# Parameters and Expected Values.
param1 = [0,1,0,3,12]
expect1 = [1,3,12,0,0]

param2 = [0]
expect2 = [0]

param3 = [0,1,0]
expect3 = [1,0,0]

solution = MoveZeroesItemInArrayToLast()
solution_title('MoveZeroesItemInArrayToLast - Quick One')
print_and_assert_reference(solution.quick, param1, expected=expect1)
print_and_assert_reference(solution.quick, param2, expected=expect2)
print_and_assert_reference(solution.quick, param3, expected=expect3)
getTestResult('MoveZeroesItemInArrayToLast - Quick One')

timeComplexity('O(n)', 'desc_goes_here')
spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('MoveZeroesItemInArrayToLast - Brute Force')
# print_and_assert_reference(solution.brute_force, param1, expected=expect1)
# print_and_assert_reference(solution.brute_force, param2, expected=expect2)
# print_and_assert_reference(solution.brute_force, param3, expected=expect3)
# getTestResult('MoveZeroesItemInArrayToLast - Brute Force')

# timeComplexity('O(n)', 'desc_goes_here')
# spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('MoveZeroesItemInArrayToLast - Sub Optimal')
# print_and_assert_reference(solution.timeOptimized, param1, expected=expect1)
# print_and_assert_reference(solution.timeOptimized, param2, expected=expect2)
# print_and_assert_reference(solution.timeOptimized, param3, expected=expect3)
# getTestResult('MoveZeroesItemInArrayToLast - Sub Optimal')

# timeComplexity('O(n)', 'desc_goes_here')
# spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('MoveZeroesItemInArrayToLast - Optimal')
# print_and_assert_reference(solution.timeOptimized, param1, expected=expect1)
# print_and_assert_reference(solution.timeOptimized, param2, expected=expect2)
# print_and_assert_reference(solution.timeOptimized, param3, expected=expect3)
# getTestResult('MoveZeroesItemInArrayToLast - Optimal')

# timeComplexity('O(n + m)', 'desc_goes_here')
# spaceComplexity('O(n + m)', 'desc_goes_here')