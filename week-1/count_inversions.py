def count_inversions(alist):
    if len(alist) == 1:
            return alist, 0

    split_index = len(alist) // 2
    left_list, left_inversions = count_inversions(alist[:split_index])
    right_list, right_inversions = count_inversions(alist[split_index:])
    return merge_list(left_list, right_list, left_inversions + right_inversions)

def merge_list(left_list, right_list, inversions):
    left_index = 0
    right_index = 0
    final = []

    # was using pop but this is O(n) from having to move each element left by one space
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            final.append(left_list[left_index])
            left_index += 1
        else:
            final.append(right_list[right_index])
            right_index += 1
            inversions += len(left_list) - left_index

    final.extend(left_list[left_index:])
    final.extend(right_list[right_index:])

    return [final, inversions]

print count_inversions([12, 11])
print count_inversions([9,8,7,6,5,4,3,2,1])
