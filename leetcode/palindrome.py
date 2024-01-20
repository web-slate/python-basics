from tabulate import tabulate
print("frute force solution")
print("""===================""")

def is_valid_polindrome(s: str) -> bool:
  string = remove_alpha_numeric(s)
  return  string == string[::-1]


def remove_alpha_numeric(s: str) -> str :
  string = ''.join(char.lower() for char in s if char.isalnum())
  return string

s = 'mam , () test'
print(f"given {s} { ' palindrome ' if is_valid_polindrome(s) else ' is not palindrome'}")
s = 'mam ()'
print(f"given {s} { ' palindrome ' if is_valid_polindrome(s) else ' is not palindrome'}")
print(""" """)
print("Optimised solution")
print("""===================""")

def is_valid(s: str) -> bool:
  s = ''.join(char.lower() for char in s if char.isalnum())
  left, right = 0 , len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return False
    else:
      left += 1
      right -= 1
  return True

s = 'mam , () test'
print(f"given {s} { ' palindrome ' if is_valid(s) else ' is not palindrome'}")
s = 'mam ()'
print(f"given {s} { ' palindrome ' if is_valid(s) else ' is not palindrome'}")

table_data = [
    ["Approach", "Time Complexity", "Example Code"],
    ["Brute-Force", "O(n)", "is_palindrome_bruteforce_string(s)"],
    ["Optimized", "O(n/2) = O(n)", "is_palindrome_optimized_string(s)"]
]

table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")

print(table)