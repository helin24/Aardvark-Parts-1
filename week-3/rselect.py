import random

def rselect(alist, index):
    end = len(alist) - 1

    if index > end:
        raise ValueError('index of %s exceeds length of list' % (index))

    if end == 0:
        return alist[0]

    pivot_index = random.randint(0, end)

    alist[0], alist[pivot_index] = alist[pivot_index], alist[0]

    pivot = alist[0]
    last_lower = 1

    for i in range(1, end + 1):
        if alist[i] < pivot:
            alist[last_lower], alist[i] = alist[i], alist[last_lower]
            last_lower += 1

    if last_lower - 1 == index:
        return pivot
    elif last_lower - 1 > index:
        return rselect(alist[1 : last_lower], index)
    elif last_lower - 1 < index:
        return rselect(alist[last_lower : end + 1], index - last_lower)

print rselect([3,8,2,5,1,4,7,6], 3)
print rselect([3,8,2,5,1,4,7,6], 5)
 
print rselect([3,8,2,5,1,4,7,6], 9)

