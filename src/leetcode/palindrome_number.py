
from tabulate import tabulate
class Solution:
    #log10(n)
    def brute_force(self, x: int) -> bool:
      number_str = str(number)
      reversed_str = number_str[::-1]
      return number_str == reversed_str

    #log10(n)
    def is_palindrome_suboptimal(number):
      number_str = str(number)
      for i in range(len(number_str) // 2):
        if number_str[i] != number_str[len(number_str) - 1 - i]:
          return False
      return True
    
    #log10(n))
    def isPalindrome(self, x: int) -> bool:
        number = x
        reversed = 0
        while(x != 0 ):
            digit = x % 10
            reversed = reversed * 10 + digit
            x = x // 10 
        return reversed == number 
    
a = Solution()
number = 121
is_valid = a.isPalindrome(x = number)
print(f"given numbe {number} is {'Palindrome' if is_valid else 'Not palidrome'} ")


def print_solution_table(solutions_info):
    table = tabulate(solutions_info, headers="keys", tablefmt="pipe")
    print(table)

# Example usage
solutions_info = [
    {"Solution": "Brute-Force (String Conversion)", "Time Complexity": "O(log10(n))", "Space Complexity": "O(log10(n))", "Notes": "Conversion to string and comparison of reversed string contribute to time and space."},
    {"Solution": "Suboptimal", "Time Complexity": "O(log10(n))", "Space Complexity": "O(1)", "Notes": "Iterating over half of the string, but potential issues with odd-length strings."},
    {"Solution": "Optimized", "Time Complexity": "O(log10(n))", "Space Complexity": "O(1)", "Notes": "Direct comparison of digits without converting to a string, more efficient overall."},
]
print_solution_table(solutions_info)
