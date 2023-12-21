from testUtils import print_and_assert_new, getTestResult

print('\n >>> 415. Add Two Strings')
print('''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
''')

class Solution(object):
    def addStrings(self, num1, num2):
        result, carry = '', 0
        num1_index, num2_index = len(num1) - 1, len(num2) - 1

        while(num1_index >= 0 or num1_index >= 0):
            first_num = int(num1[num1_index]) if num1_index >= 0 else 0
            second_num = int(num2[num2_index]) if num2_index >= 0 else 0
            value = (first_num + second_num + carry) % 10
            carry = (first_num + second_num + carry) // 10
            result = f'{value}{result}'
            print (' >> value in while ', value)
            print (' >> carry in while', carry)
            print (' >> result in while ', result, '\n')
            num1_index -= 1
            num2_index -= 1
            
        print ('out in carry ', carry)

        if (carry != 0):
            result = f'{carry}{result}'

        return result

print('\n >>> Add Two Strings')
solution = Solution()
print_and_assert_new(solution.addStrings, '11', '123', expected='134')
# print_and_assert_new(solution.addStrings, '456', '77', expected='533')
# print_and_assert_new(solution.addStrings, '0', '0', expected='0')
getTestResult('Add Two Strings')