import math

def closest_pair(alist):
    if len(alist) == 2:
        return alist, euclidean_distance(alist[0], alist[1])
    elif len(alist) == 1:
        return None, None

    sorted_by_x = merge_sort_points(alist, 0)
    sorted_by_y = merge_sort_points(alist, 1)

    split_index = len(sorted_by_x) // 2
    left, min_dist_left = closest_pair(sorted_by_x[:split_index])
    right, min_dist_right = closest_pair(sorted_by_x[split_index:])
 
    split, min_dist_split = closest_split_pair(sorted_by_x, sorted_by_y, min(i for i in [min_dist_left, min_dist_right] if i is not None))

    distances = [(min_dist_left, left), (min_dist_right, right), (min_dist_split, split)]
    not_none_dist = [i for i in distances if i[0] is not None]
    not_none_dist.sort()
    return not_none_dist[0][1], not_none_dist[0][0]

def closest_split_pair(sorted_by_x, sorted_by_y, min_dist):
    midpoint = sorted_by_x[int(math.ceil(len(sorted_by_x) / 2))]

    relevant_points = []
    for point in sorted_by_y:
        if abs(midpoint[0] - point[0] <= min_dist):
            relevant_points.append(point)

    best = min_dist
    best_pair = None 

    for i in range(len(relevant_points) - 1):
        for j in range(1, min(7,len(relevant_points) - i)):
            if euclidean_distance(relevant_points[i], relevant_points[i+j]) < best:
                best = euclidean_distance(relevant_points[i], relevant_points[i+j])
                best_pair = [relevant_points[i], relevant_points[i+j]]

    if best_pair is None:
        return None, None
    else:
        return best_pair, best

def euclidean_distance(point_one, point_two):
    return math.sqrt((point_two[0] - point_one[0])**2 + (point_two[1] - point_one[1])**2)

def merge_sort_points(alist, dim = 0):
    if len(alist) == 1:
        return alist

    split_index = len(alist) // 2
    left = merge_sort_points(alist[:split_index], dim)
    right = merge_sort_points(alist[split_index:], dim)

    final = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][dim] < right[right_index][dim]:
            final.append(left[left_index])
            left_index += 1
        else:
            final.append(right[right_index])
            right_index += 1

    final.extend(left[left_index:])
    final.extend(right[right_index:])
    return final

# print closest_pair([[4,5],[3,4],[2,1],[1,2]])
# print closest_pair([[4,5],[3,4],[2,1]])
print closest_pair([[-45,49],[-28,30],[-7,21],[-9,21],[-12,-1],[26,12],[10,10],[22,17],[7,1],[-41,-34],[-34,-49],[-7,15],[45,-38],[49,12],[41,11],[43,-42],[-27,38],[34,38],[-31,8],[42,-12],[-41,-10],[1,33],[-20,-50],[-14,-40],[-38,40],[-14,2],[-24,-29],[-35,-16],[-13,-3]])
