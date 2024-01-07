text = """

What is lambda in python? 

It is anonymous function 
It can take many number of arguments
It can only have one expression
It is written as a single line of execution
It does not support type annotations
It can be immediately invoked (IIFE)


Lambda functions are frequently used with
higher-order functions, which take one or more functions as arguments 
or return one or more functions.
filter(), sort(), sorted(), min(), and max()

A lambda function can't contain any statements.
Statements like return, pass, assert, or
raise will raise a Syntax Error exception
"""
print(text)
print("""  """ )
print("anonymous function")
print("--------------------------------")
add_value = lambda x : x + 10
print("Add Value", add_value(2))

print("""  """ )
print("More than one arguments for lambda")
print("--------------------------------")
add_value_more_arguments = (lambda x, y ,z : x + y + z)(2, 5, 7)
print("Add Value(more arguments)", add_value_more_arguments)

print("""  """ )
print("Type annotation is not supported")
print("--------------------------------")
# type_annotation = (lambda x: int, y: int ,z: int : x + y + z)(2, 5, 7)
# print("Type annotation is not supported", type_annotation)

print("""  """ )
print("Square number without lambda")
print("--------------------------------")
def square(a ):
  return a**2

numbers = [1, 2, 3, 4, 5,]
squared = list(map(square, numbers))
print("Numbers: ", numbers,)
print("Squared Numbers", squared)

print("""  """ )
print("Square number with lambda")
print("--------------------------------")
numbers = [1, 2, 3, 4, 5,]
squared = list(map((lambda x: x**2), numbers))
print("Squared numbers", squared)

print("""  """ )
print("Exception traceback with lamda")
print("--------------------------------")
div_by_zero = (lambda x: x / 0)(10)
print("Lambda: Divide by Zero", div_by_zero)

print("""  """ )
print("Exception traceback with function")
print("--------------------------------")
def div_by_zero_func(x):
  return  x / 0
print("Function: Divide by Zero", div_by_zero_func(10))

print("""  """ )
print("A lambda function can't contain any statements")
print("--------------------------------")
test = lambda x:  x + 10 
print("Test ", test(2))

