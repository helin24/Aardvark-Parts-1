import random

def quick_sort(alist):
    end = len(alist) - 1

    if end < 1:
        return alist

    pivot_index = random.randint(0, end)

    alist[0], alist[pivot_index] = alist[pivot_index], alist[0]
    
    pivot = alist[0]
    last_lower = 1 # last index lower than pivot
    for index in range(1, end + 1):
        if alist[index] < pivot:
            alist[last_lower], alist[index] = alist[index], alist[last_lower]
            last_lower += 1

    alist[0], alist[last_lower - 1] = alist[last_lower - 1], alist[0]
    
    alist[0 : last_lower - 1] = quick_sort(alist[0 : last_lower - 1])
    alist[last_lower : end + 1] = quick_sort(alist[last_lower : end + 1])
    return alist


print quick_sort([3,8,2,5,1,4,7,6])
