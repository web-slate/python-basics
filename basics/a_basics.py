# Basic Statement
from stylepy import h1, h2, h3, h4, h5, h6

h1('\n # Basic Example')

# Print Statement without parenthesis.
h2('\n >>>> Print Statement without parenthesis throws SyntaxError')
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# print "Concatenation with variable"

# Print Statement
h3('\n >>>> Print Statement ')
h6('hello venkat, welcome to python')

# Print Statement support comma separated arguments.
h4('\n >>>> Print Statement support n number of comma separated arguments.')
#  Maximum number of parameters you can pass to a function like print()
#  It is primarily limited by the amount of memory available on your system.
h4('hello venkat,', 'welcome to ', 'python')

# Concatenation
h5('\n >>>> Print Statement Simple Concatenation')
h6('hello venkat, welcome to python' + '3')

# Concatenation with int variable
h6('\n >>>> Concatenation with int variable and string throws TypeError')
version = 3
# Your will get TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(version + 'hello venkat, welcome to python')
# Your will get TypeError: can only concatenate str (not "int") to str.
# print('hello venkat, welcome to python' + version)
h5('\n >>>> Concatenation of int variable and string Issue fix should be with str() function')
# Fix is below.
h6('hello venkat, welcome to python' + str(version))

# Concatenation with string variable
h5('\n >>>> Concatenation with string variable')
version = '3'
print('hello venkat, welcome to python' + version)

# Concatenation with string variable wrapped in String literal.
h5('\n >>>> String variable wrapped in String literal.')
version = '3'
h6(f"hello venkat, welcome to python{version}")


# Simple Hello World Function throws IndentationError when function body statement with zero indentation.
h5('\n >>>> Simple Hello World Function throws IndentationError when function body statement with zero indentation.')
h6(' >>>> Fix is 4 tabs after def statement')
def helloWorld():
# You will get IndentationError: expected an indented block after function definition on line 47
# In Python, the execution order is typically from top to bottom, line by line.
# Python first compiles your code into bytecode before it executes it. During the compilation phase, it checks for syntax errors. 
# if there is an IndentationError during compilation anywhere in your code, Python will not execute any part of the script because the error is caught during the compilation phase.
# print('\nHello World from helloWorld()')
  h5('\nHello World from helloWorld()')

# Calling the function
helloWorld()

fruits = 'Apple'

h4('\nReversing fruit value using slicing')
h6(fruits[::-1])