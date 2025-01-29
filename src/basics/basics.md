# Python Basic Statement Examples

## 1. Print Statement without Parenthesis
### Issue
Using a print statement without parentheses throws a **SyntaxError**:
```python
# print "Concatenation with variable"
```
**Error Message:**  
```
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

---

## 2. Print Statement
### Correct Usage
```python
print('hello venkat, welcome to python')
```

---

## 3. Print Statement with Comma-Separated Arguments
The `print()` statement supports multiple comma-separated arguments. The maximum number depends on the available system memory.
```python
print('hello venkat,', 'welcome to', 'python')
```

---

## 4. Print Statement Simple Concatenation
Concatenation of string literals can be done using the `+` operator:
```python
print('hello venkat, welcome to python' + '3')
```

---

## 5. Concatenation with Integer Variable
### Issue
Using `+` between an integer and a string throws a **TypeError**:
```python
version = 3
# print(version + 'hello venkat, welcome to python')  # Throws TypeError
# print('hello venkat, welcome to python' + version)  # Throws TypeError
```
**Error Message:**  
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Fix
Use the `str()` function to convert the integer to a string:
```python
print('hello venkat, welcome to python' + str(version))
```

---

## 6. Concatenation with String Variable
Concatenation works without any issues when both variables are strings:
```python
version = '3'
print('hello venkat, welcome to python' + version)
```

---

## 7. String Variable Wrapped in String Literal
Using **f-strings** for clean and readable string interpolation:
```python
version = '3'
print(f"hello venkat, welcome to python{version}")
```

---

## 8. Simple Hello World Function and IndentationError
### Issue
A function body statement without proper indentation throws **IndentationError**:
```python
def helloWorld():
# print('Hello World from helloWorld()')  # IndentationError
```
**Error Message:**  
```
IndentationError: expected an indented block after function definition
```

### Explanation
In Python, the execution order is from top to bottom, line by line. Python compiles the code into bytecode before execution. If there is an **IndentationError**, the compilation phase fails, and the code is not executed.

### Fix
Indent the function body correctly:
```python
def helloWorld():
    print('Hello World from helloWorld()')
```

### Function Call
```python
helloWorld()
```

---

## 9. Reversing String Value Using Slicing
Reversing a string using slicing:
```python
fruits = 'Apple'
print(fruits[::-1])  # Output: elppA
```

