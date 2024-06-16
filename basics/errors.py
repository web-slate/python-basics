from stylepy import h1

h1('\nSyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers')

print("\nModuleNotFoundError: No module named 'utils'")
print("soluton: \nimport sys \n sys.path.append('../')")

print("\n ImportError: cannot import name 'failure_count' from 'testUtils'")
print("Soluton: Actual issue, function was missing")

print("SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?")

print('TypeError: can only concatenate str (not "int") to str')

print("NameError: name 'hoistedVariable' is not defined")
print('undefined errors')

print("TypeError: greet() missing 1 required positional argument: 'name'")

print('SyntaxError: non-default argument follows default argument')

print("TypeError: isEligibleToVote() missing 1 required positional argument: 'aaaa'")
print('Solution: We should provide default value else it will be considered required parameter')

print('ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5000 digits; use sys.set_int_max_str_digits() to increase the limit')
print('Solution: you need to set like `sys.set_int_max_str_digits(10000)`')

print('SyntaxError: trailing comma not allowed without surrounding parentheses')
print('Import statement should not end with comma')

print("AttributeError: 'str' object has no attribute 'reversed'")
print('There is no method called reversed')

print("TypeError: 'palindromSolutions' object is not callable")
print("when you simply try to call the class as function")