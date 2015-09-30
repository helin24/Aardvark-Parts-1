def count_inversions(alist):
    # if size of list is 1, then return list with 0 inversions
    # if there are two items in list and rigth goes before left then count as an inversion
    # add inversions from components

    if (len(alist) == 1):
            return [alist, 0]

    split_index = len(alist) // 2
    left = count_inversions(alist[:split_index])
    right = count_inversions(alist[split_index:])
    left_list = left[0]
    right_list = right[0]
    final = []
    inversions = left[1] + right[1]

    while (len(left_list) > 0 and len(right_list) > 0):
        if (left_list[0] <= right_list[0]):
            final.append(left_list.pop(0))
        else:
            final.append(right_list.pop(0))
            inversions += len(left_list)

    final.extend(left_list)
    final.extend(right_list)

    print [final, inversions]
    return [final, inversions]

count_inversions([12, 11])
count_inversions([9,8,7,6,5,4,3,2,1])
