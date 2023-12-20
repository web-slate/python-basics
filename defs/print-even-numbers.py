from testUtils import print_and_assert, getTestResult

def print_event_numbers(number_list):
    even_numbers = []
    for number in number_list:
        if (number % 2 == 0): 
            even_numbers.append(number)
    return even_numbers

print('\n >>> Print Event Numbers List Test Cases')
print_and_assert(print_event_numbers, [1,2,3,4,5,6], [2,4,6])
print_and_assert(print_event_numbers, [0], [0])
print_and_assert(print_event_numbers, [], [])
print_and_assert(print_event_numbers, [], [])
print_and_assert(print_event_numbers, [], [])
print_and_assert(print_event_numbers, [], [])

getTestResult('Print Event Numbers List')