from stylepy import h1,h2,h3,h4,h5,h6
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    lesser_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for value in arr[:-1]:
        if value < pivot:
            lesser_than_pivot.append(value)
        elif value == pivot:
            equal_to_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    if lesser_than_pivot and greater_than_pivot:
        return quick_sort(lesser_than_pivot) + [pivot] + equal_to_pivot + quick_sort(greater_than_pivot)
    elif lesser_than_pivot:
        return quick_sort(lesser_than_pivot) + [pivot] + equal_to_pivot
    else:
        return [pivot] + equal_to_pivot + quick_sort(greater_than_pivot)


h4('Sorted', quick_sort([5,3,1,8]));
h4('Sorted with duplicates', quick_sort([8,1,1,8,1,1,1,1]));
