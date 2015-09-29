def merge_sort(array):
    if (len(array) == 1):
        return array
    
    split_index = len(array) // 2
    left = merge_sort(array[:split_index])
    right = merge_sort(array[split_index:])

    final = []

    while (len(left) > 0 and len(right) > 0):
        if (left[0] < right[0]):
            final.append(left.pop(0))
        else:
            final.append(right.pop(0))

    final.extend(left)
    final.extend(right)

    return final

print merge_sort([3,5,76,3,2,3,4,5])
print merge_sort([9,8,7,6,5,4,3,2,1])
