# Basic Statement
print('\n # Basic Example')

# Print Statement without parenthesis.
print('\n >>>> Print Statement without parenthesis throws SyntaxError')
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# print "Concatenation with variable";

# Print Statement
print('\n >>>> Print Statement ')
print('hello venkat, welcome to python')

# Print Statement support comma separated arguments.
print('\n >>>> Print Statement support n number of comma separated arguments.')
print('hello venkat,', 'welcome to ', 'python')

# Concatenation
print('\n >>>> Print Statement Simple Concatenation')
print('hello venkat, welcome to python' + '3')

# Concatenation with int variable
print('\n >>>> Concatenation with int variable and string throws TypeError')
version = 3;
# Your will get TypeError: can only concatenate str (not "int") to str.
# print('hello venkat, welcome to python' + version)
print('\n >>>> Concatenation of int variable and string Issue fix should be with str() function')
# Fix is below.
print('hello venkat, welcome to python' + str(version))

# Concatenation with string variable
print('\n >>>> Concatenation with string variable')
version = '3';
print('hello venkat, welcome to python' + version)

# Concatenation with string variable wrapped in String literal.
print('\n >>>> String variable wrapped in String literal.')
version = '3';
print(f"hello venkat, welcome to python{version}")


# Simple Hello World Function throws IndentationError when function body statement with zero indentation.
print('\n >>>> Simple Hello World Function throws IndentationError when function body statement with zero indentation.');
print(' >>>> Fix is 4 tabs after def statement');
def helloWorld():
# You will get IndentationError: expected an indented block after function definition on line 47
# In Python, the execution order is typically from top to bottom, line by line.
# Python first compiles your code into bytecode before it executes it. During the compilation phase, it checks for syntax errors. 
# if there is an IndentationError during compilation anywhere in your code, Python will not execute any part of the script because the error is caught during the compilation phase.
#print('\nHello World from helloWorld()')
    print('\nHello World from helloWorld()')

# Calling the function
helloWorld()

fruits = 'Apple'

print(fruits[::-1])