from merge_sort import merge_sort

def dselect(alist, index):
    print "initial"
    print alist
    end = len(alist) - 1

    if index > end:
        raise ValueError('index of %s exceeds length of list' % (index))

    if end == 0:
        return alist[0]

    pivot = choose_pivot(alist)
    print pivot

    print alist

    last_lower = 0

    found_pivot = False
    for i in range(0, end + 1):
        if alist[i] < pivot:
            alist[last_lower], alist[i] = alist[i], alist[last_lower]
            last_lower += 1
        if alist[i] == pivot and not found_pivot:
            alist[last_lower], alist[i] = alist[i], alist[last_lower]
        print alist
    print "final"
    print alist

    if last_lower == index:
        return pivot
    elif last_lower > index:
        return dselect(alist[0 : last_lower], index)
    elif last_lower < index:
        return dselect(alist[last_lower : end + 1], index - last_lower)

def choose_pivot(alist):
    medians = []
    index = 0
    length = len(alist)
    while length > index:
        sorted_group = merge_sort(alist[index:index + 5])
        #print "sorted_group"
        #print sorted_group
        medians.append(sorted_group[len(sorted_group) / 2])
        index += 5
      
#    print "medians"
#    print medians

    sorted_medians = merge_sort(medians)
    return sorted_medians[len(sorted_medians) / 2]
    
print dselect([14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5)
