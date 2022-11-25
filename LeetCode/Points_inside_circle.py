# You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple
# points can have the same coordinates.
# You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a
# radius of rj.For each query queries[j], compute the number of points inside the jth circle. Points on the border of
# the circle are considered inside.Return an array answer, where answer[j] is the answer to the jth query.
# Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
# Output: [3,2,2]

# Problem Number : 1828
# Solution : calculate the distance between center of the circle and the point and check if is less tha equal to radius

import math
def solution(points, queries):
    res = []
    for center in queries:
        centerX = center[0]
        centerY = center[1]
        radius = center[2]
        count = 0
        for point in points:
            pointX = point[0]
            pointY = point[1]
            rX, rY = centerX-pointX, centerY-pointY
            if math.sqrt(rX**2 + rY**2) <= radius:
                count += 1
        res.append(count)
    return res


points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]
print(solution(points, queries))
