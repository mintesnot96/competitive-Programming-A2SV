class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min=False
        mindist=10
        minIndex=10
        for i in range(len(points)):
            print('min ',min)
            print('minIndex ', minIndex)
            print('mindist ', mindist)
            if points[i][0]==x or points[i][1]==y:
                if not min:
                    mindist = (abs(points[i][0] - x) + abs(points[i][1] - y))
                    minIndex=i
                    min=True
                elif mindist>(abs(points[i][0]-x)+abs(points[i][1]-y)):
                    mindist = (abs(points[i][0] - x) + abs(points[i][1] - y))
                    minIndex = i

                else:
                    continue
        if min:
            return minIndex
        else:
            return -1
# qlink
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/
