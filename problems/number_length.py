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

failures = None

def flag_failure():
    global failures
    failures = (failures or 0) + 1
    
def failure_count():
    return failures

def print_and_assert(param, expected):
    try:
        assert number_length(param) == expected
        print(f'✅ Pass: number_length({param}) is returning {expected}')
    except AssertionError:
        flag_failure()
        print(f'❌ AssertionError: number_length({param}) is returning {expected}')

print('\n >>> Number Length Test Cases')
print_and_assert(0, 2)
print_and_assert(25, 2)
print_and_assert(725, 3)
print_and_assert(4325, 4)
print_and_assert(734250, 6)
print_and_assert(52734250, 8)

if (failure_count() > 0):
    print(f"{failure_count()} Failure in Number Length Example tests")
else:
    print("Number Length Example tests are passed!")