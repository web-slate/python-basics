from testUtils import print_and_assert, getTestResult

print('\n >>> Number Length Example without using len() def')
print(' >>> number_length(0)')

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
