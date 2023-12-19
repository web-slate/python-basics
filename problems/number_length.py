print('\n >>> Number Length Example without using len() def')
print(' >>> number_length()')
def number_length(number):
    if number == 0:
        return 1
    count = 0
    
    while number:
        number //= 10
        count += 1
    
    return count;


assert number_length(0) == 1
assert number_length(25) == 2
assert number_length(725) == 3
assert number_length(4325) == 4
assert number_length(734250) == 6
assert number_length(52734250) == 8
print("Number Length Example tests are passed!")
