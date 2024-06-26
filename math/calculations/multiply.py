
from stylepy import h1,h2,h3,h4,h5,h6
def multiplyWithAddTest(a, b):
    try:
        # Perform an arithmetic operation that will fail for non-numeric types
        test = (a + b) - b
        return a * b
    except TypeError as e:
        # If an error occurs, return the error message
        return f"Invalid parameter value {a}, {b}"

h1(' >>> multiplyWithAddTest')
h4(multiplyWithAddTest(7, 5))      # Valid numerical input
h4(multiplyWithAddTest(7, "abc"))  # Invalid input
h4(multiplyWithAddTest("xyz", 3))  # Invalid input


def multiplyWithTypeCheck(a, b):
    try:
        # Perform an arithmetic operation that will fail for non-numeric types
        # if (isinstance(a, int) and isinstance(b, int)): #below is alternative check statement
        if type(a) is int and type(b) is int:
            return a * b
        else:
            raise TypeError('Parameter is not valid data type')
    except TypeError as e:
        # If an error occurs, return the error message
        # return f"Invalid parameter value {a}, {b}"
        return f"{e}: {a}, {b}"

h1(' >>> multiplyWithTypeCheck')
h4(multiplyWithTypeCheck(7, 5))      # Valid numerical input
h4(multiplyWithTypeCheck(7, "abc"))  # Invalid input
h4(multiplyWithTypeCheck("xyz", 3))  # Invalid input
h4(multiplyWithTypeCheck(7.5, 3))  # Invalid input

