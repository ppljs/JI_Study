from math import sqrt, pow
import heapq


REFERENCE_POINT = (0, 0)


k_closest(points, k):
    k_closest = []
    for point in points:
        if len(k_closest) >= k:
            curr_dist = negative_distance(point)
            top_dist = k_closest[0][0]
            if curr_dist > top_dist:
                heapq.heappushpop(k_closest, [curr_dist, *point])

        else:
            heapq.heappush(k_closest, [negative_distance(point), *point])

    return [[x, y] for _, x, y in k_closest]


def negative_distance(xy):
    return -sqrt(pow(xy[0] - REFERENCE_POINT[0], 2) + pow(xy[1] - REFERENCE_POINT[1], 2))
