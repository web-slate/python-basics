from testUtils import print_and_assert, getTestResult

print('\n >>> Find Two Sum is equal Max Number in list')
print(' >>>> Count Pairs for Sum of 2 numbers = Max Number')

def count_pairs_which_sum_to_max(number_list):
    max_number = max(number_list)
    count = 0
    
    for left in range(0, len(number_list)):
        # print('left is', left)
        for right in range(left + 1, len(number_list)):
            left_value = number_list[left]
            right_value = number_list[right]
            if (left_value + right_value == max_number):
                print(left_value, right_value, max_number)
                count += 1
    
    return count

print('\n >>> Test Cases')
print_and_assert(count_pairs_which_sum_to_max, [1,2,3,4,5,6], [2,4,6])

getTestResult('Find Two Sum is equal Max Number in list')