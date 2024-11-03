from testUtils import print_and_assert, getTestResult
from stylepy import h1,h2,h3,h4
h2('\n >>> Number Length Example without using len() def')
h3(' >>> number_length(0)')

def number_length(number):
    if number == 0:
        return 1
    count = 0
    
    while number:
        number //= 10
        count += 1
    
    return count;

print('\n >>> Number Length Test Cases')
print_and_assert(number_length, 0, 2)
print_and_assert(number_length, 25, 2)
print_and_assert(number_length, 725, 3)
print_and_assert(number_length, 4325, 4)
print_and_assert(number_length, 734250, 6)
print_and_assert(number_length, 52734250, 8)

getTestResult('Number Length')
