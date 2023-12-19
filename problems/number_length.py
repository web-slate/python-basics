print('\n >>>> Number Length Example without using len() def')

def number_length(number):
    if number == 0:
        return 1
    count = 0
    
    while number:
        number //= 10
        count += 1
    
    return count;


print('number_length(0): ', number_length(0))
print('number_length(25): ', number_length(25))
print('number_length(725): ', number_length(725))
print('number_length(4325): ', number_length(4325))
print('number_length(734250): ', number_length(734250))
print('number_length(52734250): ', number_length(52734250))