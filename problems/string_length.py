from stylepy import h1,h2
from testUtils import print_and_assert, getTestResult

h1('\n >>> String Length Example without using len() def')
print(' >>> string_length()')
def string_length(text):
    count = 0;
    for character in text:
        count += 1
    return count;

h2('\n >>> String Length Test Cases')
print_and_assert(string_length, 'Venkat', 6)
print_and_assert(string_length, 'R.Venkat', 8)
print_and_assert(string_length, 'Python', 6)
print_and_assert(string_length, 'Full Stack Development', 10)
print_and_assert(string_length, '734250', 6)
print_and_assert(string_length, '52734250', 9);

getTestResult('String Length')