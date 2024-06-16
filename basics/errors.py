from stylepy import h1,h2,h3,h4,h5,h6

h1('\nSyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers')

print("\nModuleNotFoundError: No module named 'utils'")
h5("soluton: \nimport sys \n sys.path.append('../')")

h5("\n ImportError: cannot import name 'failure_count' from 'testUtils'")
h6("Soluton: Actual issue, function was missing")

h5("SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?")

h6('TypeError: can only concatenate str (not "int") to str')

h5("NameError: name 'hoistedVariable' is not defined")
h6('undefined errors')

h5("TypeError: greet() missing 1 required positional argument: 'name'")

h6('SyntaxError: non-default argument follows default argument')

h5("TypeError: isEligibleToVote() missing 1 required positional argument: 'aaaa'")
h6('Solution: We should provide default value else it will be considered required parameter')

h5('ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5000 digits; use sys.set_int_max_str_digits() to increase the limit')
h6('Solution: you need to set like `sys.set_int_max_str_digits(10000)`')

h5('SyntaxError: trailing comma not allowed without surrounding parentheses')
h6('Import statement should not end with comma')

h5("AttributeError: 'str' object has no attribute 'reversed'")
h6('There is no method called reversed')

h5("TypeError: 'palindromSolutions' object is not callable")
h6("when you simply try to call the class as function")