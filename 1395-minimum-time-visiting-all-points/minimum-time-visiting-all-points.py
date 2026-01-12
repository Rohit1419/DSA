class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        total_time = 0

        for i in range(len(points) -1 ):
            x, y = points[i]
            x1, y1 = points[i+ 1]

            total_time += max(abs(x1 - x) , abs(y1 - y))
        
        return total_time