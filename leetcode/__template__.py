from utilities.testUtils import solution_title, print_and_assert_new, getTestResult
from utilities.commonUtils import timeComplexity, spaceComplexity

print('\n >>> 00. <Title>')
print('''
Desc goes here
''')

class ProblemName(object):
    def quick(self, s):
        pass
    def brute_force(self, s):
        pass
    def sub_optimal(self, s):
        pass
    def optimal(self, s):
        pass

# Parameters and Expected Values.
param1 = 'param1'
param11 = 'param11'
expect1 = 'expect1'

param2 = 'param2'
param22 = 'param22'
expect2 = 'expect2'

param3 = 'param3'
param33 = 'param33'
expect3 = 'expect3'

solution = ProblemName()
solution_title('ProblemName - Quick One')
print_and_assert_new(solution.quick, param1, param11, expected=expect1)
print_and_assert_new(solution.quick, param2, param22, expected=expect2)
print_and_assert_new(solution.quick, param3, param33, expected=expect3)
getTestResult('ProblemName - Quick One')

timeComplexity('O(n)', 'desc_goes_here')
spaceComplexity('O(n)', 'desc_goes_here')

solution_title('ProblemName - Brute Force')
print_and_assert_new(solution.brute_force, param1, param11, expected=expect1)
print_and_assert_new(solution.brute_force, param2, param22, expected=expect2)
print_and_assert_new(solution.brute_force, param3, param33, expected=expect3)
getTestResult('ProblemName - Brute Force')

timeComplexity('O(n)', 'desc_goes_here')
spaceComplexity('O(n)', 'desc_goes_here')

solution_title('ProblemName - Sub Optimal')
print_and_assert_new(solution.sub_optimal, param1, param11, expected=expect1)
print_and_assert_new(solution.sub_optimal, param2, param22, expected=expect2)
print_and_assert_new(solution.sub_optimal, param3, param33, expected=expect3)
getTestResult('ProblemName - Sub Optimal')

timeComplexity('O(n)', 'desc_goes_here')
spaceComplexity('O(n)', 'desc_goes_here')

solution_title('ProblemName - Optimal')
print_and_assert_new(solution.optimal, param1, param11, expected=expect1)
print_and_assert_new(solution.optimal, param2, param22, expected=expect2)
print_and_assert_new(solution.optimal, param3, param33, expected=expect3)
getTestResult('ProblemName - Optimal')

timeComplexity('O(n + m)', 'desc_goes_here')
spaceComplexity('O(n + m)', 'desc_goes_here')