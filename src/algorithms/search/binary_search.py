from stylepy import h1,h2,h3,h4,h5,h6
def binary_search_in_recursive(input_array, search_value, left, right):
    if(left > right): # Reached the end and unable to search.
        return False
    
    mid_point = (left + right) // 2 # 6 is midpoint first time.
    if (input_array[mid_point] == search_value):
        return True
    elif(input_array[mid_point] > search_value):
        return binary_search_in_recursive(input_array, search_value, left, mid_point -1)
    
    return binary_search_in_recursive(input_array, search_value, mid_point + 1, right)


def binary_search_in_iterative(input_array, search_value):
    left = 0
    right = len(input_array) - 1
    
    while(left <= right):
            mid_point = (left + right) // 2
            if (input_array[mid_point] == search_value):
                return True
            elif (input_array[mid_point] > search_value):
                right = mid_point - 1
            else:
                left = mid_point + 1
    
    return False

h3("""
>>> Sample Problem: Imagine you are working with a dataset of recorded temperatures in a city, logged every hour over a week. 
This dataset is sorted by the temperature values. You want to find the first occurrence of a specific temperature, say 15°C, in this dataset.
""")

h1('>>> Binary Search in Recursive');

input_array = [10, 11, 12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 20]
left_index = 0
right_index = len(input_array) - 1
print(f"binary_search_in_recursive(19) is {binary_search_in_recursive(input_array, 19, left_index, right_index)}");
print(f"binary_search_in_recursive(18) is {binary_search_in_recursive(input_array, 18, left_index, right_index)}");

h1('\n\n>>> Binary Search in Recursive');

print(f"binary_search_in_iterative(15) is {binary_search_in_iterative(input_array, 15)}");
print(f"binary_search_in_iterative(21) is {binary_search_in_iterative(input_array, 21)}");