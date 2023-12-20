from testUtils import print_and_assert, getTestResult

def is_prime_using_power_of_point_5(n):
    if n <= 1:
        return False
    # for i in range(2, int(n**0.5) + 1):
    for i in range(2, (n//2) + 1):
        if n % i == 0:
            return False
    return True
            
def is_prime_using_floor_division(number_in_element):
    if number_in_element < 2:
        return False
    for i in range(2, (number_in_element//2) + 1):
        if number_in_element % i == 0:
            return False
    return True

def is_prime(number_in_element):
    if number_in_element < 2:
        return False
    for i in range(2, number_in_element):
        if number_in_element % i == 0:
            return False
    return True

def print_all_primes_from_array(array):
    prime_numbers = []
    for k in array:
        if is_prime(k):
            prime_numbers.append(k)
    return prime_numbers

def print_all_primes_from_range(number_range):
    prime_numbers = []
    for k in range(0, number_range + 1):
        if is_prime(k):
            prime_numbers.append(k)
    return prime_numbers

print('\n >>> Print All Prime Numbers from Range Test Cases')
print_and_assert(print_all_primes_from_range, 5, [2,3,5])
print_and_assert(print_all_primes_from_range, 10, [2,3,5,7])
print_and_assert(print_all_primes_from_range, 20, [2,3,5,7,11,13,17,19])
print_and_assert(print_all_primes_from_range, 20, [2,3,5,7,11,13,17,19,21])
getTestResult('Print All Prime Numbers from Range')

print('\n >>> Print All Prime Numbers from Input Array Test Cases')
print_and_assert(print_all_primes_from_array, [1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,19,20], [2,3,5,7,11,13,17,19])
getTestResult('Print All Prime Numbers from Input Array')