from testUtils import solution_title, print_and_assert_new, getTestResult
from commonUtils import timeComplexity, spaceComplexity

print('\n >>> 415. Add Two Strings')
print('''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
''')

class addTwoStrings(object):
    def quick(self, num1, num2):
        result = str(int(num1) + int(num2))
        return result
    def brute_force(self, num1, num2):
        result, carry = '', 0
        num1_index, num2_index = len(num1) - 1, len(num2) - 1

        while(num1_index >= 0 or num2_index >= 0):
            first_num = int(num1[num1_index]) if num1_index >= 0 else 0
            second_num = int(num2[num2_index]) if num2_index >= 0 else 0
            value = (first_num + second_num + carry) % 10
            carry = (first_num + second_num + carry) // 10
            result = f'{value}{result}'
            num1_index -= 1
            num2_index -= 1

        if (carry != 0):
            result = f'{carry}{result}'

        return result
    def timeOptimized(self, num1, num2):
        result_list = []
        carry = 0
        num1_index, num2_index = len(num1) - 1, len(num2) - 1

        while num1_index >= 0 or num2_index >= 0 or carry:
            first_num = int(num1[num1_index]) if num1_index >= 0 else 0
            second_num = int(num2[num2_index]) if num2_index >= 0 else 0

            total = first_num + second_num + carry
            carry = total // 10
            result_list.append(str(total % 10))

            num1_index -= 1
            num2_index -= 1

        return ''.join(reversed(result_list))


solution = addTwoStrings()
solution_title('Add Two Strings - Quick One')
print_and_assert_new(solution.quick, '11', '123', expected='134')
print_and_assert_new(solution.quick, '456', '77', expected='533')
print_and_assert_new(solution.quick, '0', '0', expected='0')
getTestResult('Add Two Strings - Quick One')

timeComplexity('O(n)', 'Near Linear but + Operators can be expensive for larger numbers')
spaceComplexity('O(n)', 'Linear for storing the result string.')

solution_title('Add Two Strings - Brute Force')
print_and_assert_new(solution.brute_force, '11', '123', expected='134')
print_and_assert_new(solution.brute_force, '456', '77', expected='533')
print_and_assert_new(solution.brute_force, '0', '0', expected='0')
getTestResult('Add Two Strings - Brute Force')

solution_title('Add Two Strings - Time Optimized')
print_and_assert_new(solution.timeOptimized, '11', '123', expected='134')
print_and_assert_new(solution.timeOptimized, '456', '77', expected='533')
print_and_assert_new(solution.timeOptimized, '0', '0', expected='0')
getTestResult('Add Two Strings - Time Optimized')

timeComplexity('O(n + m)', 'Linear by doing key changes like Using a List (result_list), reversed and joined into a single string.\n    Reversing a list is O(n), and joining is also O(n), resulting in an overall O(n)')
spaceComplexity('O(n + m)', 'Linear due to primary space consumption is from result_list, which grows to size O(n + m). ')