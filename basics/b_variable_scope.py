from stylepy import h1, h2, h3, h4, h5, h6

# Variable Scope
h1('\n >>>> Variable Scope Example')

# helloWorld Function with outside variable
h2('\n >>>> helloWorld Function with outside variable')

type = 'World'
def helloWorld():
    print('Hello ' + type + ' from helloWorld()')

# Calling the function
helloWorld()

# helloWorld Function with hoisting variable throws `NameError: name 'hoistedVariable' is not defined`
print('\n >>>> helloWorld Function with hoisting variable throws `NameError`')
# def helloWorld():
#     print('Hello ' + hoistedVariable + ' from helloWorld()')

# helloWorld()
# hoistedVariable = 'hoisted world'

# Greet Function
print('\n >>>> Greet Function passed with `name` variable')
def greet(name):
    print('Hello ' + name)

# greet() # will throws TypeError: greet() missing 1 required positional argument: 'name'
# print(" >>>> when no parameter passed throws TypeError: greet() missing 1 required positional argument: 'name'")

print(" >>>> passing name parameter returns Hello John")
name = 'John'
greet(name)

# Global Variable
h4('\n >>>> Global and Local Variable Samples')
myAge = 21

def afterGraduation():
    myAge = 24
    # myAge will be overwritten as 24.
    print(f"inside afterGraduation: I'm {myAge} years old") 
    
# myAge will return global value 21.
print(f"outside before afterGraduation call: I'm {myAge} year old") 
afterGraduation()
print(f"outside after afterGraduation call: I'm {myAge} year old") 

# Global Variable with global keyword.
h4('\n >>>> Global Variable with global keyword')

manhood = "bachelor"

def afterMarriage():
    global manhood
    print(f"inside afterMarriage before change: I'm {manhood}") 
    manhood = "Husband"
    print(f"inside afterMarriage after change: I'm {manhood}") 
    
# manhood will return global value Husband.
print(f"outside before afterMarriage: I'm {manhood}")
afterMarriage()
print(f"outside after afterMarriage: I'm {manhood}")