import random

def quick_sort(alist):
    # if size of list is 1 then return list
    # choose random pivot
    # move pivot to front
    # for each number from 0 through end of array
        # if number less than pivot move to end of lower region
    # swap in pivot to proper place
    # quick_sort what's left of pivot and right of pivot

    if len(alist) <= 1:
        return alist

    print "starting quick sort"
    print alist
    pivot_index = random.randint(0, len(alist) - 1)

    swap(alist, 0, pivot_index)
    
    pivot = alist[0]
    print "pivot is " , pivot
    last_lower = 1 # last index lower than pivot
    for index in range(1,len(alist)):
        if alist[index] < pivot:
            print "lower than pivot, swapping"
            swap(alist, last_lower, index)
            last_lower += 1
        print alist

    swap(alist, 0, last_lower - 1)
    print "after moving pivot back"
    print alist
    alist[0 : last_lower - 1] = quick_sort(alist[0 : last_lower - 1])
    alist[last_lower : len(alist)] = quick_sort(alist[last_lower : len(alist)])
    return alist
            

def swap(alist, first_index, second_index):
    if first_index == second_index:
        return alist

    swap = alist[first_index]
    alist[first_index] = alist[second_index]
    alist[second_index] = swap
    return alist

print quick_sort([3,8,2,5,1,4,7,6])
