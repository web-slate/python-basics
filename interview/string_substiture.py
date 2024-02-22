from utilities.testUtils import solution_title, print_and_assert_new, getTestResult
from utilities.commonUtils import timeComplexity, spaceComplexity

print('\n >>> Substituting character')
print('''
     * Encodes text by substituting character with another one provided in the pair.
     * For example pair "ab" defines all "a" chars will be replaced with "b" and all "b" chars will be replaced with "a"
     * Examples:
     *      substitutions = ["ab"], input = "aabbcc", output = "bbaacc" 
     *      substitutions = ["ab", "cd"], input = "adam", output = "bcbm"  
     *      substitutions = ['ab', 'cd'], input = 'AdAm', output = 'BcBm'  
     *
     * @param list substitutions
     * @param string text
     * @return string
		 * NOTE: substitutions is lowercase but input can be mix char. So output must follow same case as input 
''')

class ProblemName(object):
    def quick(self, sub, text):
        def ucase(s):
            if 'a' <= s <= 'z':  # Check if the character is lowercase
                return chr(ord(s) - 32)
            return s

        def lcase(s):
            if 'A' <= s <= 'Z':  # Check if the character is uppercase
                return chr(ord(s) + 32)
            return s
        
        swapper = {}
        for char in sub: 
          swapper[char[0]] = char[1]
          swapper[char[1]] = char[0]
        op = ''

        for s in text:
          if ord(s) < 96 and lcase(s) in swapper:
            op += ucase(swapper[lcase(s)])
          elif s in swapper:
            op += swapper[s]
          else:
            op += s
        return op
    def brute_force(self, s):
        pass
    def sub_optimal(self, s):
        pass
    def optimal(self, s):
        pass

# Parameters and Expected Values.
param1 = ["ab"]
param11 = "aabbcc"
expect1 = "bbaacc"

param2 = ["ab", "cd"]
param22 = "adam"
expect2 = "bcbm"  

param3 = ['ab', 'cd']
param33 = 'AdAm'
expect3 = 'BcBm'

solution = ProblemName()
solution_title('ProblemName - Quick One')
print_and_assert_new(solution.quick, param1, param11, expected=expect1)
print_and_assert_new(solution.quick, param2, param22, expected=expect2)
print_and_assert_new(solution.quick, param3, param33, expected=expect3)
# getTestResult('ProblemName - Quick One')

# timeComplexity('O(n)', 'desc_goes_here')
# spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('ProblemName - Brute Force')
# print_and_assert_new(solution.brute_force, param1, param11, expected=expect1)
# print_and_assert_new(solution.brute_force, param2, param22, expected=expect2)
# print_and_assert_new(solution.brute_force, param3, param33, expected=expect3)
# getTestResult('ProblemName - Brute Force')

# timeComplexity('O(n)', 'desc_goes_here')
# spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('ProblemName - Sub Optimal')
# print_and_assert_new(solution.timeOptimized, param1, param11, expected=expect1)
# print_and_assert_new(solution.timeOptimized, param2, param22, expected=expect2)
# print_and_assert_new(solution.timeOptimized, param3, param33, expected=expect3)
# getTestResult('ProblemName - Sub Optimal')

# timeComplexity('O(n)', 'desc_goes_here')
# spaceComplexity('O(n)', 'desc_goes_here')

# solution_title('ProblemName - Optimal')
# print_and_assert_new(solution.timeOptimized, param1, param11, expected=expect1)
# print_and_assert_new(solution.timeOptimized, param2, param22, expected=expect2)
# print_and_assert_new(solution.timeOptimized, param3, param33, expected=expect3)
# getTestResult('ProblemName - Optimal')

# timeComplexity('O(n + m)', 'desc_goes_here')
# spaceComplexity('O(n + m)', 'desc_goes_here')