from testUtils import print_and_assert, getTestResult, solution_title
from stylepy import h1,h2,h3,h4
h1('\n >>> Is Palindrome Example')
h2('\n >>> The concept of a palindrome focuses solely on the sequence of characters, disregarding spaces and letter casing.')
h3(' >>> palindrome(word)')

class palindromSolutions(object):
    def using_string_solution(self, word):
        return word[::-1]

    def using_iteration_with_range(self, word):
        last_index = len(word) - 1
        text = ''
        for i in range(last_index, -1, -1):
            text += word[i]
        return text

palindrome = palindromSolutions()
using_string_solution = palindrome.using_string_solution
solution_title('Using String Slicing')
print_and_assert(using_string_solution, 'madam', 'madam')
print_and_assert(using_string_solution, 'kayak', 'kayak')
# print_and_assert(using_string_solution, 'EVIL OLIVE', 'EVIL OLIVE')
# print_and_assert(using_string_solution, 'DO GEESE SEE GOD', 'DO GEESE SEE GOD')

getTestResult('Simple Palindrome')

# using_iteration_with_range = palindrome.using_iteration_with_range
# solution_title('Using Iteration with Range')
# print_and_assert(using_iteration_with_range, 'madam', 'madam')
# print_and_assert(using_string_solution, 'kayak', 'kayak')
# print_and_assert(using_string_solution, 'EVIL OLIVE', 'EVIL OLIVE')
# # print_and_assert(using_string_solution, 'DO GEESE SEE GOD', 'DO GEESE SEE GOD')

# getTestResult('Using Iteration with Range')

