# Variable Scope in Python

## Variable Scope Example

## helloWorld Function with Outside Variable

The function `helloWorld()` uses an outside variable called `type`.

```python
# helloWorld Function with outside variable
type = 'World'
def helloWorld():
    print('Hello ' + type + ' from helloWorld()')

# Calling the function
helloWorld()
```

## helloWorld Function with Hoisting Variable

If we try to access a variable before its declaration within a function, Python will throw a `NameError` because variable hoisting is not supported.

```python
# This code throws a NameError due to the use of a hoisted variable
# def helloWorld():
#     print('Hello ' + hoistedVariable + ' from helloWorld()')

# helloWorld()
# hoistedVariable = 'hoisted world'
```

## Greet Function with Parameter

A function that requires an argument throws a `TypeError` if no argument is provided.

```python
# Greet Function
name = 'John'
def greet(name):
    print('Hello ' + name)

# Uncommenting this line will throw an error
# greet() # TypeError: greet() missing 1 required positional argument: 'name'

# Correct usage
greet(name)
```

## Global and Local Variable Samples

Python allows functions to define variables that may shadow variables from the outer/global scope.

```python
myAge = 21

def afterGraduation():
    myAge = 24  # myAge will be overwritten locally as 24.
    print(f"Inside afterGraduation: I'm {myAge} years old")

print(f"Outside before afterGraduation call: I'm {myAge} year old")
afterGraduation()
print(f"Outside after afterGraduation call: I'm {myAge} year old")
```

### Output:
```
Outside before afterGraduation call: I'm 21 year old
Inside afterGraduation: I'm 24 years old
Outside after afterGraduation call: I'm 21 year old
```

## Global Variable with `global` Keyword

To modify a global variable inside a function, you must use the `global` keyword.

```python
manhood = "bachelor"

def afterMarriage():
    global manhood
    print(f"Inside afterMarriage before change: I'm {manhood}")
    manhood = "Husband"
    print(f"Inside afterMarriage after change: I'm {manhood}")

print(f"Outside before afterMarriage: I'm {manhood}")
afterMarriage()
print(f"Outside after afterMarriage: I'm {manhood}")
```

### Output:
```
Outside before afterMarriage: I'm bachelor
Inside afterMarriage before change: I'm bachelor
Inside afterMarriage after change: I'm Husband
Outside after afterMarriage: I'm Husband
```

