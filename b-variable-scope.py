# Variable Scope
print('\n >>>> Variable Scope Example');

# helloWorld Function with outside variable
print('\n >>>> helloWorld Function with outside variable');

type = 'World';
def helloWorld():
    print('Hello ' + type + ' from helloWorld();');

# Calling the function
helloWorld();

# helloWorld Function with hoisting variable throws `NameError: name 'hoistedVariable' is not defined`
print('\n >>>> helloWorld Function with hoisting variable throws `NameError`');
# def helloWorld():
#     print('Hello ' + hoistedVariable + ' from helloWorld();');

# helloWorld();
# hoistedVariable = 'World';


# Greet Function
print('\n >>>> Greet Function passed with `name` variable');
def greet(name):
    print('Hello ' + name);

# greet(); // will throws TypeError: greet() missing 1 required positional argument: 'name'
print(" >>>> when no parameter passed throws TypeError: greet() missing 1 required positional argument: 'name'");

print(" >>>> passing name parameter returns Hello John");
name = 'John';
greet(name);
