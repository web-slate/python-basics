from utilities.testUtils import solution_title, print_and_assert_new, getTestResult
from utilities.commonUtils import timeComplexity, spaceComplexity

print('\n >>> Find Sum of Duplicated Integer Array')
print('''
##############################################
#
# Given an array nums, write a function to calculate the sum of distinct elements in the array.
#
# Example
# Input: [7,8,1,7,1,7] Output: 16
# why: Because the distinct numbers in the array are 1,7,8, the sum of which is 16
#
##############################################
''')

class FindSumOfIntegerArray(object):
    def quick(self, numbers_list):
        unique_numbers = set(numbers_list)
        sum = 0
        for number in unique_numbers:
          sum += number
        return sum
    def brute_force(self, numbers_list):
        unique_number_keys = {}
        sum = 0
        for number in numbers_list:
          if number not in unique_number_keys:
            unique_number_keys[number] = 1
            sum += number
        return sum
    def sub_optimal(self, numbers_list):
        pass
    def optimal(self, numbers_list):
        pass

# Parameters and Expected Values.
param1 = [7,8,1,7,1,7]
expect1 = 16

param2 = [7,8,1,7,1,7,4,5]
expect2 = 25

param3 = [7,8,1,7,1,7,9,6,3]
expect3 = 34

solution = FindSumOfIntegerArray()
solution_title('FindSumOfIntegerArray - Using Set')
print_and_assert_new(solution.quick, param1, expected=expect1)
print_and_assert_new(solution.quick, param2, expected=expect2)
print_and_assert_new(solution.quick, param3, expected=expect3)
getTestResult('FindSumOfIntegerArray - Using Set')

timeComplexity('O(n)', 'Creating Set and Iterating over the elements for sum')
spaceComplexity('O(n)', 'In  worst case (all elements are unique), the set will contain as many elements as the original list.')

solution_title('FindSumOfIntegerArray - Using Hash Table')
print_and_assert_new(solution.brute_force, param1, expected=expect1)
print_and_assert_new(solution.brute_force, param2, expected=expect2)
print_and_assert_new(solution.brute_force, param3, expected=expect3)
getTestResult('FindSumOfIntegerArray - Using Hash Table')

# timeComplexity('O(n)', 'desc_goes_here')
# spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('FindSumOfIntegerArray - Sub Optimal')
# print_and_assert_new(solution.timeOptimized, param1, expected=expect1)
# print_and_assert_new(solution.timeOptimized, param2, expected=expect2)
# print_and_assert_new(solution.timeOptimized, param3, expected=expect3)
# getTestResult('FindSumOfIntegerArray - Sub Optimal')

# timeComplexity('O(n)', 'desc_goes_here')
# spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('FindSumOfIntegerArray - Optimal')
# print_and_assert_new(solution.timeOptimized, param1, expected=expect1)
# print_and_assert_new(solution.timeOptimized, param2, expected=expect2)
# print_and_assert_new(solution.timeOptimized, param3, expected=expect3)
# getTestResult('FindSumOfIntegerArray - Optimal')

# timeComplexity('O(n + m)', 'desc_goes_here')
# spaceComplexity('O(n + m)', 'desc_goes_here')